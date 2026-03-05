from flask import Flask, render_template, jsonify, redirect

from forms.login_form import LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = 'parol_ot_krasnoy_knopki_donalda_trampa'


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Заготовка')


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
                           'пилот', 'строитель', 'врач', 'пилот дронов', 'штурман', 'метеоролог', 'киберинженер'])


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
        return redirect('/')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
