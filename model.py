import web
import datetime
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('db.cfg')

db = web.database(dbn='mysql', db=config.get('blog-database', 'db-name'), user=config.get('blog-database', 'db-user'), pw=config.get('blog-database', 'db-pass'), host=config.get('blog-database', 'db-host'))

def get_users():
    return db.select('users', order='id DESC')

def get_posts(offsetVal):
    return db.select('entries', order='id DESC', limit=6, offset=offsetVal)

def get_all_posts():
    return db.select('entries', order='id DESC')

def get_post(id):
    try:
        return db.select('entries', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def get_tagged_posts(tag):
    return db.select('entries', where='tag LIKE $tag', vars=locals(), order='id DESC')

def new_post(title, text, tag):
    db.insert('entries', title=title, content=text, tag=tag, posted_on=datetime.datetime.utcnow(), likes=0, dislikes=0)

def del_post(id):
    db.delete('entries', where="id=$id", vars=locals())

def update_post(id, title, text, tag):
    db.update('entries', where="id=$id", vars=locals(),
        title=title, content=text, tag=tag)