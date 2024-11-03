from multiprocessing import cpu_count

from configuration import Configuration

#socket path
bind = f"localhost:{Configuration.port}"

#worker options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

#Logging options
loglevel = 'debug'
accesslog = './logs/gunicorn_access.log'
errorlog = './logs/gunicorn_error.log'
