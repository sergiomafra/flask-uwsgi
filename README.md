# flask-uwsgi
Basic configurations to a Flask app

Notice: server.conf is configured for a localhost machine. server_name variable should be changed to adapt to a server where there are multiple webapps.

Notice: the app user will be the user you'll  run this command

***

### Installation

	sudo ./install.sh
	
You will be prompted to answer some questions regarding the app's configuration like:
1) Name
2) App folder absolute path
3) Virtualenv absolute path

After this, folder tree, basic configuration to uwsgi, service and nginx, permissions and ownership for files and directories will be automatically prepared.

***

### #TODOs
 This script isn't finished yet.
 Check the code for some TODOs.