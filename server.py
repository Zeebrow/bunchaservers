from flask import Flask
from random import randint, choice
import string
import os
import socket
app = Flask(__name__)

@app.route("/")
def return_json():
    return {
        "name": ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(12)),
        "pid": os.getpid(),
        "hostname": socket.gethostname(),
        "integer": randint(0,65534),
        "muhmap": {
                    "mapname": "map-" +
                    ''.join(choice(string.ascii_lowercase +
                    string.digits) for _ in range(6)),
                    "mapint": randint(0,65534)
                }
    }

