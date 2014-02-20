from google.appengine.ext import db

class BlogPost(db.Model):
    '''Blog post entries with title, content, date, and tags'''
    title = db.StringProperty()
    content = db.StringProperty(indexed=False)
    tag = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    url = db.StringProperty()

def get_all_posts():
    '''Return all of the blog posts'''
    blog_query = db.Query(BlogPost).order('-date')
    return blog_query

def get_post(post_url):
    '''Return a post with a given key'''
    blog_query = db.Query(BlogPost).order('-date')
    blog_query.filter('url =', post_url)
    return blog_query.get()

def get_posts(offsetNum):
    '''Return a post with a given key'''
    blog_query = db.Query(BlogPost).order('-date')
    return blog_query.fetch(6, offset=offsetNum)

def get_tagged_posts(tag):
    '''Return all of the blog posts with a given tag'''
    blog_query = db.Query(BlogPost)
    return blog_query.filter('tag =', tag)

def update_post(post_url, title, content, tag):
    '''Update the given blog post entry'''
    blog_query = db.Query(BlogPost)
    blog_query.filter('url =', post_url)
    blog_update = blog_query.get()
    blog_update.title = title
    blog_update.content = content
    blog_update.tag = tag 
    blog_update.put()

def del_post(post_url):
    '''Delete the given blog post'''
    blog_query = db.Query(BlogPost)
    blog_query.filter('url =', post_url)
    db.delete(blog_query.get())

def new_post(url, title, content, tag):
    '''Create a new blog post'''
    post = BlogPost()
    post.title = title
    post.content = content
    post.tag = tag
    post.url = url
    post.put()