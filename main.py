from flask import Flask, request, send_file, send_from_directory
from dzonsan import dzonsan
from petrov import petrov
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_url_path="", static_folder="site")
CORS(app)


@app.route("/", methods=["GET"])
def main():
    return send_file("site/index.html")


@app.route("/dzonsan", methods=["POST"])
@cross_origin()
def dzonsan_url():
    return dzonsan(request.json)


@app.route("/petrov", methods=["POST"])
@cross_origin()
def petrov_url():
    return petrov(request.json)


@app.route("/image/<name>", methods=["GET"])
@cross_origin()
def image(name):
    return send_file(f"{name}.png")


if __name__ == "__main__":
    app.run(debug=True)
