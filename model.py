import web, datetime, ConfigParser
config = ConfigParser.RawConfigParser()
config.read('db.cfg')

db = web.database(dbn='mysql', db=config.get('blog-database', 'db-name'), user=config.get('blog-database', 'db-user'), pw=config.get('blog-database', 'db-pass'), host=config.get('blog-database', 'db-host')

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

def new_post(title, text):
    db.insert('entries', title=title, content=text, posted_on=datetime.datetime.utcnow(), likes=0, dislikes=0)

def del_post(id):
    db.delete('entries', where="id=$id", vars=locals())

def update_post(id, title, text):
    db.update('entries', where="id=$id", vars=locals(),
        title=title, content=text)

def like_post(id, like):
    db.update('entries', where="id=$id", vars=locals(), likes=like+1)

def dislike_post(id, dlike):
    db.update('entries', where="id=$id", vars=locals(), dislikes=dlike+1)
