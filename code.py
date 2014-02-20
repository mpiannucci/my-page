import web
import model

from google.appengine.api import users

### Map out the urls
urls = (
    '/', 'Index',
    '/blog/(\d+)', 'Blog',
    '/blog', 'Blog',
    '/view/(.+)', 'View',
    '/new', 'New',
    '/delete/(.+)', 'Delete',
    '/edit/(.+)', 'Edit',
    '/admin', 'Admin',
    '/apps', 'Apps',
    '/github', 'Github',
    '/bio', 'Bio',
    '/logout', 'Logout',
    '/resume', 'Resume',
    '/archive', 'Archive',
    '/tag/(.+)', 'Tagged'
)

### Toggle the web debug (to test sessions)
#web.config.debug = False

### Define the web templates
t_globals = {
    'datestr': web.datestr,
    'get_posts': model.get_posts
}
render = web.template.render('templates', base='base', globals=t_globals)

### Create the web app and the sessions
app = web.application(urls, globals())

### Start the Web page class definitions
class Index:
    """ Show the home page """
    def GET(self):
        return render.index()

class Blog:
    """ Create the layout for the blog """
    def GET(self, pageNum=1):
        """ Show all page """
        return render.blog(int(pageNum))

class Archive:
    """ Create the archive """
    def GET(self):
        """ Get all the posts """
        posts = model.get_all_posts()
        return render.archive(posts)

class View:
    """ Create a single post view for testing """
    def GET(self, post_url):
        """ View single post """
        post = model.get_post(post_url)
        return render.view(post)

class Tagged:
    """ Display posts with a specific tag """
    def GET(self, tag):
        posts = model.get_tagged_posts(tag)
        return render.tagged(tag, posts)

class New:
    """ Create the new post form """
    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull,
            size=30,
            description="Post title:"),
        web.form.Textbox('tag', web.form.notnull,
            size=30,
            description="Post tags"),
        web.form.Textbox('url', web.form.notnull,
            size=30,
            description="Post url"),
        web.form.Textarea('content', web.form.notnull,
            rows=30, cols=60,
            description="Post content:"),
        web.form.Button('Post entry'),
    )

    """ Create the page used to create new blog posts """
    def GET(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            form = self.form()
            return render.new(form)
        else:
            raise web.seeother('/admin')

    def POST(self):
        form = self.form()
        if not form.validates():
            return render.new(form)
        model.new_post(form.d.url, form.d.title, form.d.content, form.d.tag)
        raise web.seeother('/admin')

class Delete:
    """ Create the method to delete posts """
    def POST(self, post_url):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            model.del_post(post_url)
            raise web.seeother('/admin')
        else:
            raise web.seeother('/admin')

class Edit:
    """ Create the method to edit posts """
    def GET(self, post_url):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            post = model.get_post(post_url)
            form = New.form()
            form.fill(post)
            return render.edit(post, form)
        else:
            raise web.seeother('/admin')

    def POST(self, post_url):
        form = New.form()
        post = model.get_post(post_url)
        if not form.validates():
            return render.edit(post, form)
        model.update_post(post_url, form.d.title, form.d.content, form.d.tag)
        raise web.seeother('/admin')

class Admin:
    """ Create the Admin interface """
    def GET(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin(): 
            posts = model.get_all_posts()
            return render.admin(user.nickname(), posts)
        else:
            raise web.redirect(users.create_login_url('/admin'))

class Logout:
    """ Create the logout method """
    def GET(self):
        raise web.redirect(users.create_logout_url('/'))

class Github:
    """ Redirect to Github """
    def GET(self):
        raise web.redirect('https://github.com/mpiannucci')

class Resume:
    """ Serve the resume """
    def GET(self):
        raise web.seeother('/static/Docs/MatthewIannucciResume.pdf')

class Bio:
    """ Create a contact page """
    def GET(self):
        return render.bio()

class Apps:
    """ Create the apps page """
    def GET(self):
        return render.apps()

def notfound():
    """ Create the not found page """
    return web.notfound("Sorry, the page you were looking for was not found.")
    # You can use template result like below, either is ok:
    #return web.notfound(render.notfound())
    #return web.notfound(str(render.notfound()))

def internalerror():
    """ Create the internal error page """
    return web.internalerror("The server says: No soup for you!")

### Create the not found app
app.notfound = notfound
app.internalerror = internalerror

main = app.cgirun()