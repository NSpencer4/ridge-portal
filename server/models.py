from google.appengine.ext import ndb
import logging

'''
User: a model to contain information about users and their roles, used for permissions as well
'''


class User(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()

    @classmethod
    def create(cls, name, email):
        user = cls(name=name, email=email)

        user.put()

        return user.key.id()

    @classmethod
    def get(cls, user_id):
        user = User.get_by_id(user_id)
        if user is None:
            raise ValueError("User not found")

        return user

    @classmethod
    def update(cls, user_id, user_updates):
        user = User.get_by_id(user_id)

        if user is None:
            raise ValueError("User not found")

        if user_updates.get('name'):
            user.name = user_updates.get('name')
        if user_updates.get('email'):
            user.email = user_updates.get('email')
        user.put()

        return user

    @classmethod
    def delete(cls, user_id):
        user = User.get_by_id(user_id)

        if user is None:
            ValueError("User not found")

        user.key.delete()
