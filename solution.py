from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def motto():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return """Человечество вырастает из детства.
Человечеству мала одна планета.
Мы сделаем обитаемыми безжизненные пока планеты.
И начнем с Марса!
Присоединяйся!"""


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>Привет, Марс!</title>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/mars.jpg')}" alt="Марс" width="300">
    <div>Вот она какая, планета Марс!</div>
</body>
</html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
    <title>Колонизация</title>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <div class="alert alert-dark">
        Человечество вырастает из детства.
    </div>
    <div class="alert alert-success">
        Человечеству мала одна планета.
    </div>
    <div class="alert alert-warning">
        Мы сделаем обитаемыми безжизненные пока планеты.
    </div>
    <div class="alert alert-info">
        И начнем с Марса!
    </div>
    <div class="alert alert-danger">
        Присоединяйся!
    </div>
    <img src="{url_for('static', filename='img/mars.jpg')}" alt="Марс" width="300">
</body>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
