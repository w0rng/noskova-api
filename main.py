from flask import Flask, request, send_file
from dzonsan import dzonsan
from petrov import petrov

app = Flask(__name__)


@app.route("/dzonsan", methods=["POST"])
def dzonsan_url():
    return dzonsan(request.json)


@app.route("/petrov", methods=["POST"])
def petrov_url():
    return petrov(request.json)


@app.route("/image/<name>", methods=["GET"])
def image(name):
    return send_file(f"{name}.png")
