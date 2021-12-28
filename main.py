from pony.orm import *


db = Database(provider='sqlite', filename='pony.db', create_db=True)

class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    age = Required(int)



db.generate_mapping(create_tables=True)

with db_session:
    User(name="alex",age=32)
    User(name="bob",age=18)
    User(name="carl",age=25)