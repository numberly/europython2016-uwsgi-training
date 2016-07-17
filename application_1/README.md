# Run a simple Flask web application
## Context
A simple Hello world with a failure condition.

## Goal
- [ ] Launch a simple application using uWSGI.
- [ ] Add a resilient part like a supervisor with uWSGI/emperor.

## Usage
1. Launch the application with uWSGI
```bash
uwsgi --ini server.ini
```

2. Test and crashed :)
```bash
curl http://localhost:8888
```

## Usage with the emperor
1. Create a configuration directory
```bash
mkdir uwsgi.d
```

2. Run uwsgi with the emperor mode
```bash
uwsgi --ini emperor.ini
```

3. Put the `server.ini` into the uwsgi configuration directory. The emperor discover the configuration file and spawn a new instance
```bash
cp server.ini uwsgi.d/
```

4. Test and crashed again :) but now the emperor automatically reload the application

## Extra
2. Launch multiple applications using emperor mode. Put a second `server.ini` with a different port.
