import web

render = web.render

class Index:
    ''' Show the home page '''
    def GET(self):
        return render.index()

class Resume:
    ''' Serve the resume '''
    def GET(self):
        raise web.seeother('/static/Docs/MatthewIannucciResume.pdf')