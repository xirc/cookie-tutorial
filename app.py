from flask import Flask, make_response

app = Flask(__name__)


@app.route('/index/', methods=["GET"])
def index():
    response = make_response("Here, take some cookie!")
    response.headers["Set-Cookie"] = "my-first-cookie=some-cookie-value; HttpOnly"
    return response


if __name__ == '__main__':
    app.run()
