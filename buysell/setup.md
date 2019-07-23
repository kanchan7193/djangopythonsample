###Setting up BuySell


https://tecadmin.net/install-django-on-ubuntu/
```
sudo apt install python3.7
pip3 install Django
pip3 install mysqlclient
python3 manage.py migrate
python3 manage.py runserver
```

```
mysql -u root
CREATE USER 'root'@'localhost' IDENTIFIED BY 'root';
create database buysell
```


default way of running unit tests
python3 manage.py test polls

using coverage
pip3 install coverage
coverage run --source='.' manage.py test polls
coverage html 



to install all dependendecies 
pip3 install -r requirement.txt

Regular templated ui with Django -
http://127.0.0.1:8000/polls

Django API 
http://127.0.0.1:8000/polls/api/

####Contributor
* Kanchan