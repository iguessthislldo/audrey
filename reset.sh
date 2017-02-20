rm -fr db.sqlite3 todo/migrations tag/migrations
python manage.py makemigrations tag
python manage.py makemigrations todo
python manage.py migrate
