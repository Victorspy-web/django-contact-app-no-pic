# Contact Storage App


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

## Must Do

**Create this two files in the project base where settings.py can be found**
```
1) SECRET_KEY.py 
2) EMAIL_CONFIG_INFO.py
```
* Inside the `SECRET_KEY.py`, create a variable name called SECRET_KEY and store your secret key in it. https://djecrety.ir can help you generate one.


* Inside the `EMAIL_CONFIG_INFO.py` file, create 2 variable names called;
  * `EMAIL_HOST_USER` = `'gmail address name'`
  * `EMAIL_HOST_PASSWORD` = `'gmail address password'`
  
    * If google is not allowing you to login into you account 
      using django then visit this url and set it ON
      https://myaccount.google.com/lesssecureapps

  
**Prerequisites**

```
Check requirements.txt for packages to install
```

**Installations for mac and linux users**

```
First clone the repository from Github and switch to the project directory
```

* git clone https://github.com/Victorspy-web/django-contact-app-no-pic.git


```
Open terminal and install pipenv for your project
```

`
You can use any other way of creating a virtual env if you are familiar with venvs
`

* sudo apt install pipenv

```
Install Django, activate and migrate project
```

* pipenv install django==3.2 . `Dont forget the space and dot at the end!`
* pipenv shell
* python manage.py makemigrations
* python manage.py migrate


```
Create django superuser
```

* python manage.py createsuperuser
    * Fill in the fields to create a superuser `Passwords are invisble`


```
You can now run the development server
```

* python manage.py runserver
    * `Paste this link in your browser to run local server` http://127.0.0.1:8000
