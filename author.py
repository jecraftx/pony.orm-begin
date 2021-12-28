from pony.orm import *


db = Database(provider='sqlite', filename='author.db', create_db=True)

class Author(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    age = Required(int)



db.generate_mapping(create_tables=True)

with db_session:
    Author(name="rick",age=31)
    Author(name="edward",age=29)
    Author(name="marx",age=28)