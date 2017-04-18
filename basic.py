from flask import Flask, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return "TODO: index.html"


@app.route('/user/<username>')
def show_user_profile(username):
    return "User: %s." % username


@app.route('/number/<int:n>')
def show_number(n):
    return "Number: %d" % n


@app.route('/url_for_index')
def url_for_index():
    #   import pdb
    #   pdb.set_trace()
    return url_for("index")


if __name__ == '__main__':
    app.debug = True
    app.run()
