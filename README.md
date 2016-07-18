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
* Pick one and be gently ! (it's a micro instance).
```bash
ec2-52-28-198-245.eu-central-1.compute.amazonaws.com
ec2-52-28-153-162.eu-central-1.compute.amazonaws.com
ec2-52-28-28-181.eu-central-1.compute.amazonaws.com
ec2-52-28-49-207.eu-central-1.compute.amazonaws.com
ec2-52-28-58-201.eu-central-1.compute.amazonaws.com
ec2-52-28-80-246.eu-central-1.compute.amazonaws.com
ec2-52-29-106-255.eu-central-1.compute.amazonaws.com
ec2-52-29-13-9.eu-central-1.compute.amazonaws.com
ec2-52-29-199-216.eu-central-1.compute.amazonaws.com
ec2-52-29-58-202.eu-central-1.compute.amazonaws.com
ec2-52-58-101-234.eu-central-1.compute.amazonaws.com
ec2-52-58-131-154.eu-central-1.compute.amazonaws.com
ec2-52-58-221-254.eu-central-1.compute.amazonaws.com
ec2-52-58-244-130.eu-central-1.compute.amazonaws.com
ec2-52-58-248-171.eu-central-1.compute.amazonaws.com
ec2-52-58-88-133.eu-central-1.compute.amazonaws.com
ec2-52-59-21-206.eu-central-1.compute.amazonaws.com
ec2-52-59-23-40.eu-central-1.compute.amazonaws.com
ec2-52-59-28-114.eu-central-1.compute.amazonaws.com
ec2-52-59-29-58.eu-central-1.compute.amazonaws.com
ec2-52-59-30-251.eu-central-1.compute.amazonaws.com
ec2-52-59-31-212.eu-central-1.compute.amazonaws.com
ec2-52-59-34-190.eu-central-1.compute.amazonaws.com
ec2-52-59-36-197.eu-central-1.compute.amazonaws.com
ec2-52-59-36-49.eu-central-1.compute.amazonaws.com
ec2-52-59-37-206.eu-central-1.compute.amazonaws.com
ec2-52-59-38-149.eu-central-1.compute.amazonaws.com
ec2-52-59-61-105.eu-central-1.compute.amazonaws.com
ec2-52-59-63-40.eu-central-1.compute.amazonaws.com
ec2-52-59-65-34.eu-central-1.compute.amazonaws.com
ec2-52-59-66-185.eu-central-1.compute.amazonaws.com
ec2-52-59-66-235.eu-central-1.compute.amazonaws.com
ec2-52-59-67-36.eu-central-1.compute.amazonaws.com
ec2-52-59-68-228.eu-central-1.compute.amazonaws.com
ec2-52-59-69-125.eu-central-1.compute.amazonaws.com
ec2-52-59-69-214.eu-central-1.compute.amazonaws.com
ec2-52-59-70-95.eu-central-1.compute.amazonaws.com
ec2-52-59-71-30.eu-central-1.compute.amazonaws.com
ec2-52-59-71-59.eu-central-1.compute.amazonaws.com
ec2-52-59-71-72.eu-central-1.compute.amazonaws.com
```

```bash
ssh -i ep16.pem ec2-user@<instance>
```

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
