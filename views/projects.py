import web

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