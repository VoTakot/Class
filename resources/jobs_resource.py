from flask import jsonify
from data import db_session
from flask_restful import abort, Resource

from data.jobs import Jobs


def abort_if_news_not_found(jobs_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(jobs_id)
    if not jobs:
        abort(404, message=f"News {jobs_id} not found")


class JobsResource(Resource):
    def get(self, jobs_id):
        abort_if_news_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        return jsonify(jobs.to_dict(only=(
            'id', 'team_leader', 'job', 'collaborators', 'work_size',
            'start_date', 'end_date', 'is_finished'
        )))

    def delete(self, jobs_id):
        abort_if_news_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'ok'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({
            'jobs': [
                job.to_dict(only=('id', 'team_leader', 'job', 'collaborators', 'work_size',
                                  'start_date', 'end_date', 'is_finished'))
                for job in jobs
            ]
        })