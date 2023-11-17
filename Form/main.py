from flask import Flask, render_template, request
from flask_wtf import CSRFProtect
from model import db, User
from forms import RegisterForm
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
db.init_app(app)


@app.route('/')
def index():
    return 'Hello!'


@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('OK')


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return 'Данные введены правильно!'
    return render_template('registration.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
