# Europython - training uWSGI

What is uWSGI and why it can help you ?
What is the dynamic emperor mode and how it works ?
* Run a simple Flask web application
* Run a gevent based Flask web application
* Run an external daemon
* Create and run a task deferral application

# Slides
[...]

# Requirements
## Using the VM (only for people present during the EP16 training)
* All the stuff is already installed. Each VM is powered by Linux Gentoo.

## Using your computer
* python
* uwsgi 2.x and specific plugins (some distribution compile uWSGI without the plugins above)
    * python
    * gevent
    * spooler
    * emperor

## Common part
* Clone this repository.
* All configuration use /tmp/ep16-training-uwsgi as root directory.

1. Create a virtualenv
```bash
virtualenv /tmp/venv
```

2. install the requirements
```bash
source /tmp/venv/bin/activate
pip install -r requirements.txt
```
