from flask import Flask, render_template, redirect, request, abort, make_response, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data import db_session, call_resource
from data.users import User
from data.calls import Call
from forms.addcallform import AddCallForm
from forms.editcallform import EditCallForm
from forms.edituserform import EditUserForm
from forms.loginform import LoginForm
from forms.registerform import RegisterForm
from flask_restful import Api
import joblib

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['JSON_AS_ASCII'] = False
login_manager = LoginManager()
login_manager.init_app(app)
predictor = joblib.load('model/my_log_reg')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.errorhandler(404)
def not_found(error):
    if request.path.startswith('/api/'):
        return jsonify({'error': 'url not found'}), 404
    else:
        return render_template('404.html', title='Страница не найдена'), 404


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            position=form.position.data,
            locality=form.locality.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)

@app.route('/users/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_user(id):
    form = EditUserForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.id == id).first()
        if user:
            form.email.data = user.email
            form.name.data = user.name
            form.surname.data = user.surname
            form.locality.data = user.locality
            form.position.data = user.position
        else:
            abort(404)
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('edit_user.html', title='Профиль оператора',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data, User.id != id).first():
            return render_template('edit_user.html', title='Профиль оператора',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = db_sess.query(User).filter(User.id == id).first()
        if user:
            user.email = form.email.data
            user.name = form.name.data
            user.surname = form.surname.data
            user.locality = form.locality.data
            user.position = form.position.data
            user.set_password(form.password.data)
            db_sess.commit()
            return redirect('/login')
        else:
            abort(404)
    return render_template('edit_user.html', title='Профиль оператора', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/map')
@app.route('/')
def index():
    db_sess = db_session.create_session()
    calls = db_sess.query(Call).all()
    db_sess.commit()
    police = []
    fire = []
    amb = []
    for call in calls:
        coord = [float(x) for x in call.point.split()]
        coord[1], coord[0] = coord[0], coord[1]
        if call.service == "police":
            police.append([coord, call.id])
        elif call.service == "fire":
            fire.append([coord, call.id])
        else:
            amb.append([coord, call.id])
    return render_template('map.html', police=police, fire=fire, amb=amb)


@app.route('/add_call', methods=['GET', 'POST'])
@login_required
def add_call():
    form = AddCallForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        call = Call()
        call.message = form.message.data
        call.address = form.address.data
        call.recognize_call()
        db_sess.add(call)
        db_sess.commit()
        return redirect('/calls')
    return render_template('add_call.html', title='Новый вызов',
                           form=form)


@app.route('/calls/<int:call_id>', methods=['GET', 'POST'])
@login_required
def edit_call(call_id):
    form = EditCallForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        call = db_sess.query(Call).filter(Call.id == call_id).first()
        if call:
            form.message.data = call.message
            form.address.data = call.address
            form.service.data = call.service
            form.status.data = call.status
            form.call_id = call_id
            if call.point:
                x, y = call.point.split()
                form.point = f"{x},{y}"
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        call = db_sess.query(Call).filter(Call.id == call_id).first()
        if call:
            call.message = form.message.data
            call.service = form.service.data
            call.change_address(form.address.data)
            call.change_status(form.status.data)
            db_sess.commit()
            return redirect('/calls')
        else:
            abort(404)
    return render_template('edit_call.html',
                           title='Редактирование вызова',
                           form=form
                           )


@app.route('/calls')
@login_required
def calls():
    db_sess = db_session.create_session()
    calls = db_sess.query(Call).all()
    db_sess.commit()
    return render_template('calls.html', calls=calls)


@app.route('/delete_call/<int:call_id>', methods=['GET', 'POST'])
@login_required
def delete_call(call_id):
    db_sess = db_session.create_session()
    call = db_sess.query(Call).filter(Call.id == call_id).first()
    if call:
        db_sess.delete(call)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/calls')


def main():
    db_session.global_init("db/emergency.db")
    api.add_resource(call_resource.CallListResource, '/api/calls')
    api.add_resource(call_resource.CallResource, '/api/calls/<int:id>')
    app.run(debug=True)


if __name__ == '__main__':
    main()
