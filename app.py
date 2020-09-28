from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    response = make_response("Here, take some cookie!")
    response.set_cookie(key="id", value="3db4adj3d", path="/about/")
    return response


@app.route("/about/", methods=["GET"])
def about():
    print(request.cookies)
    return "Hello world!"


@app.route("/contact/", methods=["GET"])
def contact():
    print(request.cookies)
    return "Hello world!"


if __name__ == '__main__':
    app.run()
