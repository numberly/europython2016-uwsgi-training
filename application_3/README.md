# Run an external daemon using uWSGI
## Context
A simple Hello world using memcached.

## Goal
- [ ] Attach a simple daemon to your application.
- [ ] More and more resilience with the daemon.

## Usage in `dumb` mode
1. Launch the application with uWSGI.
```bash
uwsgi --ini emperor.ini
```

2. Simulate one request.
```bash
curl http://localhost:8888
```

3. Another request using the memcached.
```bash
curl http://localhost:8888
```

4. Restart uWSGI instance (you will loose the cache).
```bash
curl http://localhost:8888
```

## Usage in `smart` mode
1. Use the smart daemon in the `server.ini`.

2. Launch the application with uWSGI.
```bash
uwsgi --ini emperor.ini
```

3. Simulate one request.
```bash
curl http://localhost:8888
```

4. Another request using the memcached.
```bash
curl http://localhost:8888
```

5. Restart uWSGI instance (the cache is still present).
```bash
curl http://localhost:8888
```
