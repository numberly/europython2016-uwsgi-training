# Run a gevent based Flask web application
## Context
A simple Hello world with a long task (simulate by a sleep).

## Goal
- [ ] Call the application without the asynchronous part.
- [ ] Add the gevent loop.

## Usage
1. Launch the application with uWSGI.
```bash
uwsgi --ini emperor.ini
```

2. Simulate two requests.
```bash
curl http://localhost:8888

Hello World !
```

## Usage with the gevent loop engine
1. Add the gevent loop engine in the `server.ini` (add `gevent27` in the plugins directive).
```bash
# check if the loop engine is loaded in the uWSGI logs.
[...]
*** running gevent loop engine [addr:0x7fc7ccb89be0] ***
```

2. Simulate two requests.
```bash
curl http://localhost:8080

Hello World !
```
