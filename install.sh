while true; do
    read -p "Choose your APP name: " APP_NAME
    read -p "Path to your app folder: " APP_ABS_PATH
    echo -e "APP name: ${APP_NAME}\nAPP path: ${APP_PWD}"
    read -p "Is that correct? [Y/n] " YN
    case $YN in
        Y|y|"" ) break;;
        N|n    ) continue;;
        * ) echo -e "Not a valid option\n"; continue;;
    esac
done

APP_PATH=$("${APP_PWD}${APP_NAME}")
APP_USER=$(whoami)

echo -n "Creating app folders' tree"
sudo mkdir -p ${APP_PATH}/{etc,log,www}
sudo mkdir ${APP_PATH}/{etc,log}/{nginx,uwsgi}
echo " ... Done!"

echo -p "Moving files to correct places"
## TODO
## 1) Change file names i.e. app.ini -> ${APP_NAME}.ini
## 2) SED content with user parameters
## 3) Move files to correct folders
echo " ... Done!"

echo -n "Changing permissions and users"
## TODO
echo " ... Done!"

## TODO
## Configure virtual env installing dependencies

## TODO
## 1) Reload NGINX conf
## 2) Start uWSGI app service
## 3) Make sure service will start on server start
