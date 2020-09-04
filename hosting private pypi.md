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
4.  Verify an installation by
```bash
  devpi-server --version
```
5.  Start devpi server by issue this command
```bash
  devpi-server --start --port 3141 --host 0.0.0.0
```
6.  Verify by curl to localhost
```bash
  curl http://localhost:3141
  curl http://SERVER_IP_ADDRESS:3141
```
7.  Stop devpi server by
```bash
  devpi-server --stop
```
8.  Install some test package to verify that devpi server is working
```bash
  pip install -i http://SERVER_IP_ADDRESS:3141/root/pypi/+simple/ simplejson
```
