from flask import Flask, render_template
app = Flask(__name__)


# goes to /templates and renders "hello.html"
@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.jinja2", name=name)


if __name__ == "__main__":
    app.debug = True
    app.run()
