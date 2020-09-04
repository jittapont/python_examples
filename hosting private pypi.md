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

# How to upload package to devpi server

[Taken from this url](https://opensource.com/article/18/7/setting-devpi)

1.  Install devpi-client and twine
```bash
  pip install devpi-client twine
```
2.  Configure devpi to use devpi server
```bash
  devpi use http://SERVER_IP_ADDRESS:3141
```
3.  Create user and password
```bash
  devpi user -c username password=password
```
4.  Login using created user credentials
```bash
  devpi login username --password=password
```
5.  Create index for current user
```bash
  devpi index -c index_name bases=root/pypi
```
6.  Configure devpi to use current user index
```bash
  devpi use username/index_name
```
7.  Use twine to upload your package
```bash
  twine upload --repository-url http://SERVER_IP_ADDRESS:3141/username/index_name -u username -p password YOUR_PACKAGE_NAME.tar.gz
```
8.  Verify upload by install package from devpi
```bash
  pip install --trusted-host SERVER_IP_ADDRESS -i http://SERVER_IP_ADDRESS:3141/username/index_name YOUR_PACKAGE_NAME
```
