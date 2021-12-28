from pony.orm import *


db = Database(provider='sqlite', filename='post.db', create_db=True)

class Post(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    content = Required(str)



db.generate_mapping(create_tables=True)

with db_session:
    Post(title="summer",content="some poem about summer")
    Post(title="winter",content="some poem about winter")
    Post(title="spring",content="some poem about spring")