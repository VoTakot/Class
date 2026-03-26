from flask import Blueprint, request, jsonify
from data import db_session
from data.jobs import Jobs

api = Blueprint(
    "job_api",
    __name__,
    template_folder="templates"
)


@api.route("/api/jobs", methods=['GET'])
def jobs():
    if request.method == 'GET':
        session = db_session.create_session()
        jobs_items = session.query(Jobs).all()
        return jsonify({
            'jobs': [
                job.to_dict(only=('id', 'team_leader', 'job', 'collaborators', 'work_size',
                                  'start_date', 'end_date', 'is_finished'))
                for job in jobs_items
            ]
        })
    return jsonify({'error': 'Method Not Allowed'}), 405


@api.route("/api/jobs/<int:job_id>", methods=['GET', 'POST'])
def one_jobs(job_id):
    if request.method == 'GET':
        session = db_session.create_session()
        job = session.query(Jobs).filter(Jobs.id == job_id).first()
        return jsonify(job.to_dict(only=('id', 'team_leader', 'job', 'collaborators', 'work_size',
                                  'start_date', 'end_date', 'is_finished')))
    if request.method == 'POST':
        jobs_json = request.get_json()
        job = Jobs(
            collaborators=jobs_json['collaborators'],
            end_date=jobs_json['end_date'],
            is_finished=jobs_json['is_finished'],
            start_date=jobs_json['start_date'],
            job=jobs_json['job'],
            team_leader=jobs_json['team_leader'],
            work_size=jobs_json['work_size']
        )
        session = db_session.create_session()
        job = session.merge(job)
        session.commit()
        return jsonify({'id': job.id}), 201
    return jsonify({'error': 'Method Not Allowed'}), 405