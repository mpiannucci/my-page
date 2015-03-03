import web
import models

render = web.render

class Blog:
    ''' Create the layout for the blog '''
    def GET(self, pageNum=1):
        ''' Show all page '''
        return render.blog(int(pageNum))

class Archive:
    ''' Create the archive '''
    def GET(self):
        ''' Get all the posts '''
        posts = models.get_all_posts()
        return render.archive(posts)

class View:
    ''' Create a single post view for testing '''
    def GET(self, post_url):
        ''' View single post '''
        post = models.get_post(post_url)
        return render.view(post)

class Tagged:
    ''' Display posts with a specific tag '''
    def GET(self, tag):
        posts = models.get_tagged_posts(tag)
        return render.tagged(tag, posts)