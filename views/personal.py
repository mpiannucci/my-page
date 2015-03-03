import web

render = web.render

class Resume:
    ''' Serve the resume '''
    def GET(self):
        raise web.seeother('/static/Docs/MatthewIannucciResume.pdf')