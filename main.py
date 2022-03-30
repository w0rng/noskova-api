from flask import Flask, request
from dzonsan import dzonsan

app = Flask(__name__)


@app.route("/dzonsan", methods=["GET"])
def hello_world():
    return dzonsan(request.json)
