from flask import Flask, request, url_for, render_template, redirect, flash
app = Flask(__name__)


def valid_login(username, password):
    if username == password:
        return True
    else:
        return False


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            flash("Successfully logged in")
            return redirect(url_for('welcome',
                                    username=request.form['username']))
        else:
            error = "Incorrect username and/or passowrd"

    return render_template('login.jinja2', error=error)


@app.route("/welcome/<username>")
def welcome(username):
    return render_template('welcome.jinja2', username=username)


if __name__ == "__main__":
    app.debug = True
    app.secret_key = "secret_key"
    app.run()
