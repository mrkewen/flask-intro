from flask import Flask, url_for, render_template, request, redirect, flash
app = Flask(__name__)


def valid_login(user, password):
    if user == password:
        return True
    else:
        return False


@app.route("/index", methods=['POST', 'GET'])
def index():

    error = None

    if request.method == "POST":
        if valid_login(request.form['username'], request.form['password']):
            return redirect(url_for('welcome',
                                    username=request.form['username']))
        else:
            error = "Incorrect username or password"

    return render_template("new_login.jinja2", error=error)


@app.route("/welcome/<username>")
def welcome(username):
    return render_template("welcome.jinja2", username=username)


if __name__ == "__main__":
    app.debug = True
    app.run()
