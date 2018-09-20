# ayomi_test
environment project
Python 2.7, Django 1.8 et Bootstrap 3


### To run project please follow this steps
### best Practice create virtual environment
$ pip install virtualenv
### in the project folder run this command
$ virtualenv venv
$ source venv/bin/activate 

 1-install req
> ~$ pip install -r requirements.txt

 2-migrate the data base
> ~$ ./manage.py migrate

 3-Run
> ~$ ./manage.py runserver


PS: To run Test you have to copy geckodriver in your /usr/local/bin if you are using Linux 
run test with firefox
> ~$ ./manage.py test


