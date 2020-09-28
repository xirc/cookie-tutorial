from flask import Flask, make_response, request, render_template, jsonify

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/get-cookie/", methods=["GET"])
def get_cookie():
    response = make_response("Here, take some cookie!")
    response.set_cookie(key="id", value="3db4adj3d")
    return response


@app.route("/api/cities/", methods=["GET"])
def cities():
    if request.cookies["id"] == "3db4adj3d":
        cities = [{"name": "Rome", "id": 1}, {"name": "Siena", "id": 2}]
        return jsonify(cities)
    return jsonify(msg="Ops!")


if __name__ == '__main__':
    app.run()
