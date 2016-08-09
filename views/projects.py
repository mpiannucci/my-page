import web
import models
import json

render = web.render

class Apps:
    ''' Create the apps page '''
    def GET(self):
        return render.apps()

class Github:
    ''' Redirect to Github '''
    def GET(self):
        raise web.redirect('https://github.com/mpiannucci')

class HackWinds:
    ''' Show the HackWinds page'''
    def GET(self):
        return render.hackwinds()

class HackWindsLogin:
    ''' Check if a user has premium access to hackwinds '''
    def POST(self):
        data = web.input()
        email = data['username']

        user_response = {}
        user_response['email'] = email
        if models.does_hackwinds_user_exist(email):
            user = models.get_hackwinds_user(email)
            user_response['exists'] = True
            user_response['premium'] = user.premium_access
        else:
            user_response['exists'] = False
            user_response['premium'] = False

        web.header('Content-Type', 'application/json')
        return json.dumps(user_response)

class HackWindsCreate:
    ''' Create a new user account '''
    def POST(self):
        data = web.input()
        email = data['username']
        code = data['code']

        user_response = {}
        user_response['email'] = email
        if models.does_hackwinds_user_exist(email):
            user = models.get_hackwinds_user(email)
            user_response['success'] = True
            user_response['premium'] = user.premium_access
        elif code == '109485':
            models.add_hackwinds_user(email, True)
            user_response['success'] = True
            user_response['premium'] = True
        elif code == '1000':
            models.add_hackwinds_user(email, False)
            user_response['success'] = True
            user_response['premium'] = False
        else:
            user_response['success'] = False
            user_response['premium'] = False

        web.header('Content-Type', 'application/json')
        return json.dumps(user_response)
