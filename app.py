import secrets
from flask import Flask, request, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route('/')
def index():
    if 'email' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))


@app.route('/cloth/')
def cloth():
    context = {'title': 'Одежда'}
    return render_template('cloth.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    return render_template('shoes.html', **context)


@app.route('/jackets/')
def jackets():
    context = {'title': 'Куртки'}
    return render_template('jackets.html', **context)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['email'] = request.form.get('email')
        session['username'] = request.form.get('username')
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
