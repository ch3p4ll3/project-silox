import multiprocessing

# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "project_silos.wsgi:application"
# The number of worker processes for handling requests
workers = multiprocessing.cpu_count() * 2 + 1
# The socket to bind
bind = "0.0.0.0:8080"
# Write access and error info to /var/log
# accesslog = "/log/gunicorn/access.log"
# errorlog = "/log/gunicorn/error.log"
# Redirect stdout/stderr to log file
capture_output = True
# # PID file so you can easily fetch process ID
# pidfile = "/log/gunicorn/prod.pid"
# Daemonize the Gunicorn process (detach & enter background)
#daemon = True
