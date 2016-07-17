#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from random import randint
from sys import exit

import uwsgi

from flask import Flask
from memcache import Client


app = Flask(__name__)
# NOTE: ugly way to manage the connection.
mclient = Client(['127.0.0.1:11311'], debug=0)
mclient.set("sleep", None)


@app.route("/")
def hello():
    try:
        # NOTE: simulate a failure.
        if randint(1, 5) == 1:
            raise Exception("this is the end")

        mkey = mclient.get("sleep")
        if mkey:
            return "Hello World from cache :: {} !".format(mkey)

       # NOTE: simulate a long operation.
        print("sleep my friend !")
        time.sleep(5)
        mclient.set("sleep", "Hearth of the Swarm")
        return "Hello World !"
    except Exception as e:
        uwsgi.spool({'name': 'Wings of liberty'})
        return "Hello World with failure !"


def my_spooler(env):
    try:
        print("spooler function :: update cache with {}".format(env))
        mclient.set("sleep", env["name"])
    except Exception as e:
        print("oops :: {}".format(e))
        return uwsgi.SPOOL_RETRY
    else:
        return uwsgi.SPOOL_OK


uwsgi.spooler = my_spooler


if __name__ == "__main__":
    app.run(debug=True)
