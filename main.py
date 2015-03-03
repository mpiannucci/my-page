import web
import models
from config import urls

# Toggle the web debug (to test sessions)
# web.config.debug = False

# Define the web templates
t_globals = {
    'datestr': web.datestr,
    'get_posts': models.get_posts,
    'len': len
}
web.render = render = web.template.render('templates', base='base', globals=t_globals)

# Now that the templates are loaded, import the view controllers
from views import *

# Create the web app and the sessions
app = web.application(urls, globals())

def notfound():
    ''' Create the not found page '''
    return web.notfound('Sorry, the page you were looking for was not found.')
    # You can use template result like below, either is ok:
    # return web.notfound(render.notfound())
    # return web.notfound(str(render.notfound()))

def internalerror():
    ''' Create the internal error page '''
    return web.internalerror('The server says: No soup for you!')

# Create the not found app
app.notfound = notfound
app.internalerror = internalerror

main = app.cgirun()