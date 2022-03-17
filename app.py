from flask import Flask, request, redirect
from pathlib import Path

import ws

app = Flask(__name__)


@app.route('/<query>', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index(query=''):
    if request.method == 'POST':
        return redirect('/' + request.form['query'])

    with open(Path('templates', 'index.html'), 'r', encoding='utf-8') as html_stream:
        html = html_stream.read()

    weather = ws.get_weather(query)
    for replace in weather:
        html = html.replace(f'{{{{ {replace} }}}}', str(weather[replace]))
    return html


if __name__ == '__main__':
    app.run(debug=True)
