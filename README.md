# fashionist-blog

Schritte, um den Blog zum Laufen zu bringen:

$ git clone https://github.com/vincentgottschling/fashionist-blog.git

$ python -m venv 'Name des Virtual Environments'

$ 'Name des Virtual Environments'\Scripts\activate

$ python -m pip install --upgrade pip

$ pip install -r anforderungen.txt

$ pip install pillow

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py createsuperuser

$ python manage.py runserver

