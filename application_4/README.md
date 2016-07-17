# Run a gevent based Flask web application
## Context
A simple Hello world with a piece of resilience

## Goal
- [ ] Spool instead of a dirty crash.

## Usage with spool
1. Create a spooler directory
```bash
mkdir /tmp/spooler
```

2. Launch the application with uWSGI
```bash
uwsgi --ini emperor.ini
```

2. First request (no cache)
```bash
curl http://localhost:8080

Hello World !
```

3. Second request use the cache
```bash
curl http://localhost:8080

Hello World from cache :: Hearth of the Swarm !
```

4. Requests until a crash, the server will spool the request. Then the function will update the cache with a new key.
```bash
curl http://localhost:8080

Hello World from cache :: Wings of Liberty !
```
