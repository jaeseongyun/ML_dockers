import os

home_dir = os.environ['HOME']

if os.path.isdir("$HOME/.ipython/profile_nbserver")is False:
    os.system("ipython profile create nbserver")
else: 
    os.system("echo profile_nbserver is already exist.")

from IPython.lib import passwd
pwsha = passwd()
   
config_str = """
# Server config
c = get_config()
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.password = u'{}'
# It is a good idea to put it on a known, fixed port
c.NotebookApp.port = 8888
c.NotebookApp.notebook_dir = u'/'
""".format(pwsha)

with open(home_dir+"/.ipython/profile_nbserver/ipython_notebook_config.py", "w") as cf:
    cf.write(config_str)
