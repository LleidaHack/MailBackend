from multiprocessing import cpu_count

from src.configuration.Settings import settings

#socket path
bind = f"0.0.0.0:{settings.port}"

#worker options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'
# Gunicorn's 2s default closes idle keep-alive sockets before the backend's
# httpx pool (5s expiry) stops reusing them, which drops requests with
# "Server disconnected without sending a response".
keepalive = 75

#Logging options
loglevel = 'debug'
accesslog = '-'
errorlog = '-'
capture_output = True
