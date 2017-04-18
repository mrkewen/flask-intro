from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        if valid_login(request.form['username'], request.form['password']):
            return "User %s logged in" % request.form['username']
        else:
            error = 'Incorrect username and/or password'

    return render_template('login.jinja2', error=error)


def valid_login(username, password):
    if username == password:
        return True
    else:
        return False


if __name__ == "__main__":
    app.debug = True
    app.run()
