from flask import Flask, render_template, redirect, url_for, request, flash
app = Flask(__name__)


def valid_login(user, password):
    if user == password:
        True
    else:
        False


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['passowrd']):
            flash("Successfully logged in")
            return redirect(url_for("welcome", request.form['username']))
        else:
            error = "Wrong username and/or password"

    return render_template('cookie_login.jinja2', error=error)


@app.route('/welcome/<username>')
def welcome(username):
    return "TODO: welcome"


if __name__ == "__main__":
    app.debug = True
    app.run()
