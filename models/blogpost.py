from google.appengine.ext import ndb

class BlogPost(ndb.Model):
    '''Blog post entries with title, content, date, and tags'''
    title = ndb.StringProperty()
    content = ndb.TextProperty()
    editor_content = ndb.TextProperty()
    tag = ndb.StringProperty(repeated=True)
    date = ndb.DateTimeProperty(auto_now_add=True)
    url = ndb.StringProperty()

def get_all_posts():
    '''Return all of the blog posts'''
    blog_query = BlogPost.query().order(-BlogPost.date)
    return blog_query

def get_post(post_url):
    '''Return a post with a given key'''
    blog_query = BlogPost.query().order(-BlogPost.date)
    blog_query.filter('url =', post_url)
    return blog_query.get()

def get_posts(offsetNum):
    '''Return a post with a given key'''
    blog_query = BlogPost.query().order(-BlogPost.date)
    return blog_query.fetch(6, offset=offsetNum)

def get_tagged_posts(tag):
    '''Return all of the blog posts with a given tag'''
    blog_query = BlogPost.query(BlogPost.tag == tag)
    return blog_query

def update_post(post_url, title, content, editor_content, tag):
    '''Update the given blog post entry'''
    blog_query = BlogPost.query(BlogPost.url == post_url)
    blog_update = blog_query.get()
    blog_update.title = title
    blog_update.content = content
    blog_update.editor_content = editor_content
    blog_update.tag = tag.split(',') 
    blog_update.put()

def del_post(post_url):
    '''Delete the given blog post'''
    blog_query = BlogPost.query(BlogPost.url == post_url)
    blog_query.get().key.delete()

def new_post(url, title, content, editor_content, tag):
    '''Create a new blog post'''
    post = BlogPost()
    post.title = title
    post.content = content
    post.editor_content = editor_content
    post.tag = tag.split(',')
    post.url = url
    post.put()