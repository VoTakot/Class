from flask import jsonify
from data import db_session
from flask_restful import abort, Resource

from data.users import User


def abort_if_news_not_found(user_id):
    session = db_session.create_session()
    jobs = session.query(User).get(user_id)
    if not jobs:
        abort(404, message=f"News {user_id} not found")


class UserResource(Resource):
    def get(self, user_id):
        abort_if_news_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify(user.to_dict(only=(
            'id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password',
            'modified_date'
        )))

    def delete(self, user_id):
        abort_if_news_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'ok'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({
            'users': [
                user.to_dict(only=('id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email',
                                   'hashed_password', 'modified_date')) for user in users
            ]
        })
