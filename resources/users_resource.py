from flask import jsonify
from data import db_session
from flask_restful import abort, Resource, reqparse

from data.users import User


parser = reqparse.RequestParser()
parser.add_argument('surname', required=True, type=str)
parser.add_argument('name', required=True, type=str)
parser.add_argument('age', required=True, type=int)
parser.add_argument('position', required=False, type=str)
parser.add_argument('speciality', required=False, type=str)
parser.add_argument('address', required=False, type=str)
parser.add_argument('hashed_password', required=True, type=str)
parser.add_argument('email', required=False, type=str)
parser.add_argument('modified_date', required=True)


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

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            name=args['name'],
            surname=args['surname'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            hashed_password=args['hashed_password'],
            modified_date=args['modified_date']
        )
        session.add(user)
        session.commit()
        return jsonify({'user_id': user.id})