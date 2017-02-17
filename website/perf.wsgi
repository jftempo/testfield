import sys
import os

os.environ['MPLCONFIGDIR'] = "/tmp"

path = os.path.expanduser("~/.myenv/bin/activate_this.py")
if os.path.exists(path):
    execfile(activate_env, dict(__file__=path))

import bottle

sys.path = [os.path.dirname(__file__)] + sys.path
os.chdir(os.path.dirname(__file__))

import performance # This loads your application

application = bottle.default_app()
