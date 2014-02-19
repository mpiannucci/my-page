from google.appengine.ext import ndb

BLOG_NAME = 'mattsblog'

def blog_key(blog_name=BLOG_NAME):
    '''Constructs a Datastore key for a blog entity with blog_name'''
    return ndb.key('mattsBlog', blog_name)

class BlogPost(ndb.Model):
    '''Blog post entries with title, content, date, and tags'''
    author = ndb.UserProperty()
    title = ndb.StringProperty()
    content = ndb.StringProperty(indexed=False)
    tag = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

def get_all_posts():
    '''Return all of the blog posts'''
    blog_query = BlogPost.query(
            ancestor=blog_key(BLOG_NAME)).order(-BlogPost.date)
    return blog_query.fetch() 

def get_post(key):
    '''Return a post with a given key'''
    blog_query = BlogPost.query(
            ancestor=blog_key(BLOG_NAME)).order(-BlogPost.date)
    return blog_query.filter(BlogPost.key==key)

def get_posts(num):
    '''Return a post with a given key'''
    blog_query = BlogPost.query(
            ancestor=blog_key(BLOG_NAME)).order(-BlogPost.date)
    return blog_query(num)

def get_tagged_posts(tag):
    '''Return all of the blog posts with a given tag'''
    blog_query = BlogPost.query(
            ancestor=blog_key(BLOG_NAME)).order(-BlogPost.date)
    return blog_query.filter(BlogPost.tag==tag)

def update_post(post_key, author, title, content, tag):
    '''Update the given blog post entry'''
    blog_query = BlogPost.query(
            ancestor=blog_key(BLOG_NAME)).order(-BlogPost.date)
    blog_query.filter(BlogPost.key==post_key)

def del_post(key):
    '''Delete the given blog post'''
    blog_query = BlogPost.query(
            ancestor=blog_key(BLOG_NAME)).order(-BlogPost.date)
    blog_query.filter(BlogPost.key==key)
    blog_query.delete()