# How to host private pypi using devpi

1.  Create a python virtual environment

```bash
  mkdir devpi_example
  cd devpi_example
  virtualenv venv
```
2.  Activate virtualenv

```bash
  source venv/bin/activate
```

3.  Install devpi server

```bash
  pip install -q -U devpi-server
```

4.  Start devpi server by issue this command
```bash
  devpi-server --start --port 3141 --host 0.0.0.0
```

5.  Verify by curl to localhost

```bash
  curl http://localhost:3141
  curl http://SERVER_IP_ADDRESS:3141
```