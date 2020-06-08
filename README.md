## Installation & Run
These services must be installed, configured and running:

 * Python (>= 3.6)
 * FFmpeg
 * MongoDB 
 * RabbitMQ (celery backend)

After required services were installed and started, 
you can proceed with a goex server installation.


### Installation for development
NOTE: Use [virtualenv](https://docs.python.org/3/library/venv.html) and [pip](https://pypi.org/project/pip/) to install python modules.

```
# clone project
git clone https://github.com/thanhnguyen-editshare/goex-core.git

# install goex-core server for development
# NOTE: your virtualenv must be activated
pip install -e goex-core/[dev]
```


### Run goex server for development
goex-core server consists from two main parts: http api and celery workers.  

For starting an http api dev server:
1. Set `FLASK_ENV` env variable to `development`:
```
export FLASK_ENV=development
```
2. Run `python -m goex.app`  

For starting a celery workers:
1. Run `celery -A goex.worker worker`

### Running tests
NOTE: You can run tests only if project was installed for development!   
There are several options how you can run tests:

1. Run tests directly from your virtualenv.  
Execute `pytest` from goex-core server root.

```
pytest
```

if you want to get a coverage report into your terminal screen 

```
pytest --cov-report term-missing --cov
```

2. Run tests using [tox](https://tox.readthedocs.io/en/latest/).  
It runs tests for each python version specified in `.python-version` file.  
[tox-pyenv](https://pypi.org/project/tox-pyenv/) plugin is used, so python versions from `.python-version` must be installed in yours 
[pyenv](https://github.com/pyenv/pyenv).
Just execute `tox` from  goex-core server root.


### Installation for production
goex-core server is a module, but not ready to use instance.  
For ready to use installation, please refer to the README file at: https://github.com/thanhnguyen-editshare/goex-app.git


## Getting Started
Once server is started you can access a swagger via http://0.0.0.0:5050/swagger/ 


## Authors
* **Thanh Nguyen**
