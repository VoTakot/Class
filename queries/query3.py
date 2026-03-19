from data.db_session import global_init, create_session
from data.users import User

global_init(input())
session = create_session()

users = session.query(User).filter(User.position.like('%chief%') | User.position.like('%middle%')).all()
for user in users:
    print(f'{user} {user.position}')