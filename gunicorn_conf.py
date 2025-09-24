from multiprocessing import cpu_count

from src.configuration.Settings import settings

#socket path
bind = f"localhost:{settings.port}"

#worker options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

#Logging options
loglevel = 'debug'
accesslog = './logs/gunicorn_access.log'
errorlog = './logs/gunicorn_error.log'
