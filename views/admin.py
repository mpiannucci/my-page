import web
import models
import markdown

from google.appengine.api import users

render = web.render

class New:
    ''' Create the new post form '''
    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull,
            size=30,
            description='Post title:',
            class_='form-control'),
        web.form.Textbox('tag', web.form.notnull,
            size=30,
            description='Post tags',
            class_='form-control'),
        web.form.Textbox('url', web.form.notnull,
            size=30,
            description='Post url',
            class_='form-control'),
        web.form.Textarea('editor_content', web.form.notnull,
            rows=10, cols=100,
            description='Post content:',
            class_='form-control'),
        web.form.Button('Submit Post', class_='btn btn-primary', style='margin-top:10px;'),
    )

    ''' Create the page used to create new blog posts '''
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
        parsed_content = markdown.markdown(form.d.editor_content)
        models.new_post(form.d.url, form.d.title, parsed_content, form.d.editor_content, form.d.tag)
        raise web.seeother('/admin')

class Delete:
    ''' Create the method to delete posts '''
    def POST(self, post_url):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            models.del_post(post_url)
            raise web.seeother('/admin')
        else:
            raise web.seeother('/admin')

class Edit:
    ''' Create the method to edit posts '''
    def GET(self, post_url):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            post = models.get_post(post_url)
            if (post.editor_content is None):
                post.editor_content = post.content
            form = New.form()
            form.title.value = post.title
            form.tag.value = ",".join(post.tag)
            form.url.value = post.url
            form.editor_content.value = post.editor_content
            return render.edit(post, form)
        else:
            raise web.seeother('/admin')

    def POST(self, post_url):
        form = New.form()
        post = models.get_post(post_url)
        if not form.validates():
            return render.edit(post, form)
        parsed_content = markdown.markdown(form.d.editor_content)
        models.update_post(post_url, form.d.title, parsed_content, form.d.editor_content, form.d.tag)
        raise web.seeother('/admin')

class Admin:
    ''' Create the Admin interface '''
    def GET(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin(): 
            posts = models.get_all_posts()
            return render.admin(user.nickname(), posts)
        else:
            raise web.redirect(users.create_login_url('/admin'))

class Logout:
    ''' Create the logout method '''
    def GET(self):
        raise web.redirect(users.create_logout_url('/'))