from data import db_session
from data.users import User

db_session.global_init("../db/mars_explorer.db")
session = db_session.create_session()

captain = User(
    surname='Scott', name='Ridley',
    age=21, position='captain',
    speciality='research engineer', address='module_1',
    email='scott_chief@mars.org'
)
session.add(captain)

chief = User(
    surname='Quick', name='Gleb',
    age=19, position='chief',
    speciality='manage working', address='module_1',
    email='mark_quick@mars.org'
)
session.add(chief)

warrior = User(
    surname='Borisov', name='Gleb',
    age=26, position='warrior',
    speciality='defeating country', address='module_1',
    email='gleb_warrior@mars.org'
)
session.add(warrior)

monster = User(
    surname='Roundov', name='Shurik',
    age=563, position='monster',
    speciality='rounding', address='module_1',
    email='shurik_searching@mars.org'
)
session.add(monster)

session.commit()
