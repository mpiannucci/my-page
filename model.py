from google.appengine.ext import db

class BlogPost(db.Model):
    '''Blog post entries with title, content, date, and tags'''
    author = db.UserProperty()
    title = db.StringProperty()
    content = db.StringProperty(indexed=False)
    tag = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)

def get_all_posts():
    '''Return all of the blog posts'''
    blog_query = db.Query(BlogPost).order('-date')
    return blog_query

def get_post(key):
    '''Return a post with a given key'''
    blog_query = db.Query(BlogPost).order('-date')
    return blog_query.filter('key =', key)

def get_posts(offsetNum):
    '''Return a post with a given key'''
    blog_query = db.Query(BlogPost).order('-date')
    return blog_query.fetch(6, offset=offsetNum)

def get_tagged_posts(tag):
    '''Return all of the blog posts with a given tag'''
    blog_query = db.Query(BlogPost)
    return blog_query.filter('tag =', tag)

def update_post(post_key, author, title, content, tag):
    '''Update the given blog post entry'''
    blog_query = db.Query(BlogPost)
    blog_query.filter('key =', post_key)

def del_post(key):
    '''Delete the given blog post'''
    blog_query = db.Query(BlogPost)
    blog_query.filter('key =', key)
    blog_query.delete()