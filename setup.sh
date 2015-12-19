# source setup.sh

# Colors
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

echo "${green}>>> Creating virtualenv${reset}"
virtualenv -p python3 .venv
source .venv/bin/activate

cd djangoproject

echo "${green}>>> Installing the Django${reset}"
pip install - requirements.txt
# ./manage.py dumpdata core --format=json --indent=2 > fixtures.json
python manage.py loaddata fixtures.json
python manage.py runserver
echo "${green}>>> Done${reset}"
