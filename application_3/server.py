#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from random import randint
from sys import exit

from flask import Flask
from memcache import Client


app = Flask(__name__)
# NOTE: ugly way to manage the connection.
mclient = Client(['127.0.0.1:11311'], debug=0)


@app.route("/")
def hello():
    mkey = mclient.get("sleep")
    if mkey:
        return "Hello World from cache :: {} !".format(mkey)

    # NOTE: simulate a failure.
    if randint(1, 5) == 1:
        exit(1)

    # NOTE: simulate a long operation.
    print("sleep my friend !")
    time.sleep(10)

    mclient.set("sleep", "Hearth of the Swarm")
    return "Hello World !"


if __name__ == "__main__":
    app.run(debug=True)
