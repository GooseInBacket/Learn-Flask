from flask import Flask, render_template, request
from dotenv import load_dotenv
from mail_sender import send_email

app = Flask(__name__)
load_dotenv()


@app.route('/', methods=['GET'])
def get_form():
    return render_template('mail_me.html')


@app.route('/', methods=['POST'])
def post_from():
    email = request.values.get('email')
    if send_email(email, 'Тестовое письмо', 'Тестовый текст', ['1.png', 'doc.pdf', 'text.txt']):
        return f'Письмо отправлено учпешно на адрес {email}'
    return f'Во время отправки письма на адрес {email} произошла ошибка'


if __name__ == '__main__':
    app.run()
