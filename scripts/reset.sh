# Ensure we are in the root of the project
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
cd ..

rm -fr db.sqlite3 task/migrations tag/migrations
python manage.py makemigrations tag
python manage.py makemigrations task
python manage.py migrate
