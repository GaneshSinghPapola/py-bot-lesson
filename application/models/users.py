import os
# from pymongo import MongoClient
from ..models import db, client
from application import bcrypt
from mongokat import Collection, Document


class UserDocument(Document):
    def my_sum(self):
        return self["a"] + self["b"]


class UserCollection(Collection):

    document_class = UserDocument

    __collection__ = 'users'
    structure = {'email': str, 'password': str, 'firstname':str, 'lastname':str }
    protected_fields = ('password')

    def __init__(self, db, *args, **kwargs):
            Collection.__init__(self, collection=db[self.__collection__], *args, **kwargs)

    @staticmethod
    def hashed_password(password):
        return bcrypt.generate_password_hash(password)

    def get_user_with_email_and_password(self, email, password):
        user = self.find_one({'email': email})
        if user and bcrypt.check_password_hash(user['password'], password):
            return user
        else:
            return None


# Then use it in your code like this:
User = UserCollection(db)