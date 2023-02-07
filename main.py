import os

from flask import Flask, render_template, url_for, request
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html', title='Домашняя страница')

@app.route('/index')
def more_index():
    params = dict()
    params['username'] = 'Яндексоид комнатный'
    params['title'] = 'Домашняя страница!'
    return render_template('index.html', **params)

@app.route('/conditions')
def conditions():
    params = dict()
    params['title'] = 'Условия'
    params['number'] = 2
    return render_template('conditions.html', **params)

@app.route('/cycles')
def cycles():
    params = dict()
    params['title'] = 'Циклы'
    params['users'] = ['Егор', 'Егор', 'Шьям', 'Андрей', 'Даня']
    params['pic'] = url_for('.static', filename='/img/pic.png')
    return render_template('cycles.html', **params)

@app.route('/base')
def base():
    params = dict()
    params['title'] = 'Наследование шаблонов'
    params['css'] = url_for('.static', filename='/css/base_style.css')
    return render_template('base.html', **params)

@app.route('/inner')
def inner():
    params = dict()
    params['title'] = 'Наследование шаблонов'
    params['css'] = url_for('.static', filename='/css/base_style.css')
    return render_template('inner.html', **params)

@app.route('/forms', methods=['GET', 'POST'])
def forms():
    if request.method == 'GET':
        params = dict()
        params['title'] = 'Работа с формами'
        params['css'] = url_for('.static', filename='/css/base_style.css')
        params['form'] = LoginForm()

        return render_template('forms.html', **params)
    elif request.method == 'POST':
        params = dict()
        params['title'] = 'Работа с формами'
        params['css'] = url_for('.static', filename='/css/base_style.css')

        params['username'] = request.form.get('username')
        params['password'] = hash(request.form.get('password'))
        params['remember'] = request.form.get('remember_me')

        return render_template('post_form.html', **params)

if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1', debug=True, load_dotenv=True)