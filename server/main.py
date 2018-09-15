# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Sample Google App Engine application that demonstrates using the Users API

For more information about App Engine, see README.md under /appengine.
"""

# [START all]

from google.appengine.api import users
import webapp2
import os
from google.appengine.ext.webapp import template



'''
REST API to render the main page index.html
'''


class MainPage(webapp2.RequestHandler):
    def get(self):
        """
        Function: Renders the main html template for the application
        :return: Html page from index_path
        """
        template_values = {}
        index_path = "index.html"
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), index_path)
        self.response.out.write(template.render(path, template_values))

'''
Routing to redirect requests to / to MainPage class
'''
app = webapp2.WSGIApplication([
    ('/.*', MainPage),
], debug=True)

# [END all]
