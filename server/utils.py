import webapp2
import json
from google.appengine.ext import ndb
from datetime import datetime
import logging

DEFAULT_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'


class APIRequest(webapp2.RequestHandler):
    def __init__(self, request, response):
        # super(APIRequest, self).__init__()  # pycharm really wants me to add this
        self.initialize(request=request, response=response)

    def to_json(self, o):
        if isinstance(o, list):
            return [self.to_json(l) for l in o]
        if isinstance(o, dict):
            x = {}
            for l in o:
                x[l] = self.to_json(o[l])
            return x
        if isinstance(o, datetime):
            return o.strftime(DEFAULT_TIME_FORMAT)
        if isinstance(o, ndb.GeoPt):
            return {'lat': o.lat, 'lon': o.lon}
        if isinstance(o, ndb.Key):
            return o.urlsafe()
        if isinstance(o, ndb.Model):
            dct = o.to_dict()
            dct['datastore_id'] = o.key.id()
            return self.to_json(dct)
        return o

    def options(self):
        self.response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE'
        self.response.set_status(200)

    def check_params(self, params):
        for param in params:
            if param not in self.request.params:
                self.abort(code=400,
                           detail="Missing parameter: {param}.".format(param=param))

    def check_body(self, fields):
        if self.request.body:
            body = json.loads(self.request.body)
            missing_fields = []
            for field in fields:
                if field not in body:
                    missing_fields.append(field)
            if missing_fields:
                self.abort(code=400,
                           detail="Missing Fields: {missing_fields}".format(missing_fields=missing_fields))
            else:
                return body
        else:
            self.abort(code=400,
                       detail="Request body not found.")
