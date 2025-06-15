from multiprocessing import cpu_count

#socket path
bind = "0.0.0.0:8001"

#worker options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

#Logging options
loglevel = 'debug'
accesslog = './logs/gunicorn_access.log'
errorlog = './logs/gunicorn_error.log'
