import os
from flask import Flask, url_for, request

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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
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
    <title>Отбор астронавтов</title>
</head>
<body>
    <h1>Анкета претендента</h1>
    <form method="post">
        <div class="mb-3">
            <label for="surname" class="form-label">Фамилия</label>
            <input type="text" class="form-control" id="surname" name="surname">
        </div>
        <div class="mb-3">
            <label for="name" class="form-label">Имя</label>
            <input type="text" class="form-control" id="name" name="name">
        </div>
        <div class="mb-3">
            <label for="email" class="form-label">Email</label>
            <input type="email" class="form-control" id="email" name="email">
        </div>
        <div class="mb-3">
            <label for="education" class="form-label">Образование</label>
            <select class="form-select" id="education" name="education">
                <option>Среднее</option>
                <option>Среднее специальное</option>
                <option>Неоконченное высшее</option>
                <option>Высшее</option>
            </select>
        </div>
        <div class="mb-3">
            <label for="profession" class="form-label">Основная профессия</label>
            <select class="form-select" id="profession" name="profession">
                <option>Инженер-исследователь</option>
                <option>Пилот</option>
                <option>Строитель</option>
                <option>Экзобиолог</option>
                <option>Врач</option>
                <option>Инженер по терраформированию</option>
                <option>Климатолог</option>
                <option>Специалист по радиационной защите</option>
                <option>Астрогеолог</option>
                <option>Гляциолог</option>
                <option>Инженер жизнеобеспечения</option>
                <option>Метеоролог</option>
                <option>Оператор марсохода</option>
                <option>Киберинженер</option>
                <option>Штурман</option>
                <option>Пилот дронов</option>
            </select>
        </div>
        <div class="mb-3">
            <label class="form-label">Пол</label>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                <label class="form-check-label" for="male">Мужской</label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                <label class="form-check-label" for="female">Женский</label>
            </div>
        </div>
        <div class="mb-3">
            <label for="motivation" class="form-label">Мотивация</label>
            <textarea class="form-control" id="motivation" rows="3" name="motivation"></textarea>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="ready" name="ready">
            <label class="form-check-label" for="ready">Готовы остаться на Марсе?</label>
        </div>
        <button type="submit" class="btn btn-primary">Отправить</button>
    </form>
</body>
</html>"""
    elif request.method == 'POST':
        surname = request.form.get('surname')
        name = request.form.get('name')
        email = request.form.get('email')
        education = request.form.get('education')
        profession = request.form.get('profession')
        sex = request.form.get('sex')
        motivation = request.form.get('motivation')
        ready = request.form.get('ready')
        return f"""<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>Ответ</title>
</head>
<body>
    <h1>Спасибо, {name} {surname}!</h1>
</body>
</html>"""


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
    <title>Освоение {planet_name}</title>
</head>
<body>
    <h1>Миссия: {planet_name}</h1>
    <h2>Начнём освоение новой планеты!</h2>
    <div class="alert alert-primary" role="alert">
        <h3>Планета: {planet_name}</h3>
    </div>
    <div class="alert alert-success" role="alert">
        Мы готовы к колонизации!
    </div>
</body>
</html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
    <title>Результаты отбора</title>
</head>
<body>
    <h1>Результаты отбора</h1>
    <h2>Астронавт: {nickname}</h2>
    <div class="alert alert-info" role="alert">
        <h3>Этап: {level}</h3>
    </div>
    <div class="alert alert-success" role="alert">
        <h4>Рейтинг: {rating}</h4>
    </div>
</body>
</html>"""


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
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
    <title>Загрузка фото</title>
</head>
<body>
    <h1>Загрузите вашу фотографию</h1>
    <form method="post" enctype="multipart/form-data">
        <div class="mb-3">
            <label for="photo" class="form-label">Выберите файл</label>
            <input type="file" class="form-control" id="photo" name="file">
        </div>
        <button type="submit" class="btn btn-primary">Отправить</button>
    </form>
</body>
</html>"""
    elif request.method == 'POST':
        f = request.files['file']
        if f:
            f.save(os.path.join('static', 'img', 'uploaded.jpg'))
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
    <title>Загрузка фото</title>
</head>
<body>
    <h1>Загрузите вашу фотографию</h1>
    <form method="post" enctype="multipart/form-data">
        <div class="mb-3">
            <label for="photo" class="form-label">Выберите файл</label>
            <input type="file" class="form-control" id="photo" name="file">
        </div>
        <button type="submit" class="btn btn-primary">Отправить</button>
    </form>
    <img src="{url_for('static', filename='img/uploaded.jpg')}" alt="Ваше фото" width="300">
</body>
</html>"""


@app.route('/gallery')
def gallery():
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
    <title>Галерея Марса</title>
</head>
<body>
    <h1>Марсианские ландшафты</h1>
    <div id="carouselExample" class="carousel slide" data-bs-ride="carousel" style="max-width: 800px; margin: auto">
        <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExample" data-bs-slide-to="0" class="active"></button>
            <button type="button" data-bs-target="#carouselExample" data-bs-slide-to="1"></button>
            <button type="button" data-bs-target="#carouselExample" data-bs-slide-to="2"></button>
        </div>
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="{url_for('static', filename='img/mars1.jpg')}" class="d-block w-100" alt="Марс 1">
                <div class="carousel-caption d-none d-md-block">
                    <h5>Поверхность Марса</h5>
                </div>
            </div>
            <div class="carousel-item">
                <img src="{url_for('static', filename='img/mars2.jpg')}" class="d-block w-100" alt="Марс 2">
                <div class="carousel-caption d-none d-md-block">
                    <h5>Глобус Марса</h5>
                </div>
            </div>
            <div class="carousel-item">
                <img src="{url_for('static', filename='img/mars.jpg')}" class="d-block w-100" alt="Марс 3">
                <div class="carousel-caption d-none d-md-block">
                    <h5>Ландшафт Марса</h5>
                </div>
            </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
            <span class="carousel-control-prev-icon"></span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
            <span class="carousel-control-next-icon"></span>
        </button>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js"
    crossorigin="anonymous"></script>
</body>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
