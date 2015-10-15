# To install Python/Django libs
pip install -r REQUIREMENTS.txt

# To setup tables in database (initial)
python manage.py syncdb
python manage.py migrate

# to add new field
python manage.py schemamigration --auto appsname
python manage.py migrate


# to create new user, specialist or midwife
in admin:
add user > enter username and password > save
enter user details(name, email, select group midwife or specialist > save and continue editing > save
