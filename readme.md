Project made using Django framework with sqlite database. Only one html page is used to display questions. Response model is used to store answer of the user.

# Steps to install dependency

Python 3.x should be installed
```
pip install -r requirements.txt
```


# Steps to run the project

``` 
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Steps to view responses

<ol>
<li> Create a credential for superuser by running the command </li>

```
python manage.py createsuperuser

```
<li> Run the project and visit 127.0.0.1:8000/admin
<li> Use the credential created above to login. Then go to responses model.
<li> All the responses will be visible there.