#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from random import randint
from sys import exit

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    # NOTE: simulate a failure.
    if randint(1, 5) == 1:
        exit(1)

    # NOTE: simulate a long operation.
    print("sleep my friend !")
    time.sleep(10)

    return "Hello World !"


if __name__ == "__main__":
    app.run(debug=True)
