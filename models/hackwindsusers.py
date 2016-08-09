from google.appengine.ext import ndb

class HackWindsUser(ndb.Model):
    ''' HackWinds user includes their email and whether they are premium or not '''
    email = ndb.StringProperty()
    premium_access = ndb.BooleanProperty()

def get_all_hackwinds_users():
    user_query = HackWindsUser.query()
    return user_query

def get_hackwinds_user(user_email):
    user_query = HackWindsUser.query(HackWindsUser.email == user_email)
    return user_query.get()

def does_hackwinds_user_exist(user_email):
    user_query = HackWindsUser.query(HackWindsUser.email == user_email)
    return user_query.count(limit=1) > 0

def add_hackwinds_user(user_email, premium = False):
    user = HackWindsUser()
    user.email = user_email
    user.premium_access = premium
    user.put()