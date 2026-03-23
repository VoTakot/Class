import flask_login
from flask import Flask, render_template, redirect

from data.db_session import create_session
from forms.jobs_form import JobsForm
from forms.login_form import LoginForm
from data.users import User
from data.jobs import Jobs
from flask_login import LoginManager, login_user, logout_user, login_required
import datetime as dt

from data import db_session

app = Flask(__name__)

app.config["SECRET_KEY"] = 'parol_ot_krasnoy_knopki_donalda_trampa'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def user_loader(user_id):
    session = db_session.create_session()
    return session.get(User, user_id)


@app.route('/')
@app.route('/index')
def index():
    session = create_session()
    result = session.query(Jobs, User).join(
        User,
        Jobs.team_leader == User.id
    )
    return render_template('index.html', title='Главная страница', result=result)


@app.route('/promotion')
def ad():
    return ('<p>Человечество вырастает из детства.</p><p>Человечеству мала одна планета.</p>'
            '<p>Мы сделаем обитаемыми безжизненные пока планеты.</p><p>И начнем с Марса!</p><p>Присоединяйся!</p>')


@app.route('/image_mars')
def image_mars():
    return render_template('image_mars.html')


@app.route('/promotion_image')
def promotion_image():
    return render_template('promotion_image.html')


@app.route('/astronaut_selection')
def astronaut_selection():
    return render_template('astronaut_selection.html', title='Отбор астронавтов')


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return render_template('choice.html', planet_name=planet_name, title='Варианты выбора')


@app.route('/results/<nickname>/<level>/<rating>')
def results(nickname, level, rating):
    return render_template('results.html', title='Результаты', nickname=nickname, level=level, rating=rating)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', title='Тренировки в полёте', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('list_prof.html', title='Список профессий', list=list, jobs=['инженер-исследователь',
                                                                                        'пилот', 'строитель', 'врач',
                                                                                        'пилот дронов', 'штурман',
                                                                                        'метеоролог', 'киберинженер'])


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    context = {'title': 'Анкета',
               'surname': 'Watny',
               'name': 'Mark',
               'education': 'выше среднего',
               'profession': 'штурман марсохода',
               'sex': 'male',
               'motivation': 'Всегда мечтал застрять на Марсе!',
               'ready': True
               }
    return render_template('auto_answer.html', **context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(
            User.email == login_form.email.data
        ).first()
        if user and user.check_password(login_form.password.data):
            login_user(user, remember=login_form.remember_me)
            return redirect('/')
        return render_template('login.html', form=login_form, message='Ошибка входа')
    return render_template('login.html', form=login_form)


@flask_login.login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route('/carousel')
def carousel():
    return render_template('carousel.html', title='Пейзажи Марса')


@login_required
@app.route('/addjob', methods=['GET', 'POST'])
def addjob():
    jobs_form = JobsForm()
    if jobs_form.validate_on_submit():
        session = db_session.create_session()
        job = Jobs(
            team_leader=jobs_form.team_leader.data, job=jobs_form.job.data,
            work_size=jobs_form.work_size.data, collaborators=jobs_form.collaborators.data, start_date=dt.datetime.now(),
            is_finished=jobs_form.is_finished.data
        )
        session.add(job)
        session.commit()
        return redirect('/')
    return render_template('addjob.html', title='Adding a Job', form=jobs_form)


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    app.run('127.0.0.1', 8080)
