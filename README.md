# flask_collect
(venv) $ python manage.py db init
(venv) $ python manage.py db migrate -m "initial migration"
(venv) $ python manage.py db upgrade
(venv) $ python manage.py collect_index
(venv) $ python manage.py collect_list_add
(venv) $ python manage.py collect_list_edit
(venv) $ python manage.py runserver
