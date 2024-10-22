import random

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>  <a href="/random_fact">Посмотреть случайный факт!</a> <a href="/downloadsmg4launchernightly">Скачать Бета Версия SMG4 Лаунчер!</a>'
@app.route("/random_fact")
def facts_list():
    facts_list = "SMG4 Лаунчер движок к Winforms и CSharp, у SMG4 Radio который радио можно слушать бесплатно есть 2 версия Alpha и Бета это чтобы он работал на Alpha и бета."
    return f'<p>{random.choice(facts_list)}</p> <a href="/">Назад!</a>'

@app.route("/downloadsmg4launchernightly")
def installnightlysmg4launcher():
    return '<h1>The Nightly is not come out but you can use Normal version -- SMG4Project <a href="https://smg4project.github.io/smg4launchersite/">Download Pre-Release Versions</a> <a href="/">Назад!</a>'

app.run(debug=True)
