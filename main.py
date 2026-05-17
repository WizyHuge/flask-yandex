import os
import json
from flask import Flask, url_for, request, render_template, redirect
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    title = request.args.get('title', '')
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        spec = 'Инженерные тренажеры'
        img = url_for('static', filename='img/engineer.jpg')
    else:
        spec = 'Научные симуляторы'
        img = url_for('static', filename='img/scientist.jpg')
    return render_template('training.html', title=spec, spec=spec, img=img)


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    profs = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог',
             'врач', 'инженер по терраформированию', 'климатолог',
             'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
             'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода',
             'киберинженер', 'штурман', 'пилот дронов']
    return render_template('list_prof.html', title='Список профессий',
                           list_type=list_type, profs=profs)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    if sex == 'male':
        wall = '#1e90ff' if age < 21 else '#0000cd'
    else:
        wall = '#ff69b4' if age < 21 else '#c71585'
    img = url_for('static', filename='img/mars_child.jpg') if age < 21 else url_for('static', filename='img/mars_adult.jpg')
    return render_template('table.html', title='Оформление каюты', wall=wall, img=img)


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


@app.route('/gallery', methods=['POST', 'GET'])
def gallery():
    img_dir = os.path.join('static', 'img', 'gallery')
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    images = sorted([f for f in os.listdir(img_dir) if f.endswith(('.jpg', '.png', '.jpeg'))])
    if request.method == 'POST':
        f = request.files.get('file')
        if f:
            f.save(os.path.join(img_dir, f'img_{len(images) + 1}.jpg'))
            images = sorted([f for f in os.listdir(img_dir) if f.endswith(('.jpg', '.png', '.jpeg'))])
    images = [url_for('static', filename=f'img/gallery/{i}') for i in images]
    return render_template('gallery.html', title='Галерея Марса', images=images)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
