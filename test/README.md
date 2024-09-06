Django project creation guide
1. python -m pip install (installs python packages using pip)
2. python -m venv env_site (creating vm)
3.  if windows run: .\env_site\Scripts\activate.ps1 if mac/os run: source env_site/bin/activate (activating the vm)
4. pip install django (install django)
5. django-admin startproject myfirstproject (creating a django project called myfirstproject)
6. cd myfirstproject
7. python manage.py runserver (starting djangos development server)
8. once hitting these commands the link the project will be run on is: http://127.0.0.1:8000/

Acessing an existing project such as myfirstproject
1. cd test
2. .\env_site\Scripts\activate.ps1
3. cd myfirstproject
4. python manage.py runserver

Exiting a django project
1. ctrl + C
2. exit


