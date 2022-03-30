from flask import Flask, request, send_file
from dzonsan import dzonsan

app = Flask(__name__)


@app.route("/dzonsan", methods=["GET"])
def dzonsan_url():
    return dzonsan(request.json)


@app.route("/image/<name>", methods=["GET"])
def image(name):
    return send_file(f"{name}.png")
