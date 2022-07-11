# Pikachu-Housing
Project Pikachu-housing Development Guide

## Project introduction


Pikachu Housing is a single page website for house/apartment rentals in Northeastern University, San Jose, California.The goal of this website is to provide renters better overviews on house rental prices in San Jose area, especially for new students.


Basic functions of the project contain CRUD and multiple-param query search. Advanced function is house suggestion.  


Tech stack:
- Database: PostgreSQL
- Backend: Django (python)


## Prepare for development
* Install prerequisite packages: python(2.7), pip, virtualenv, git, postgreSQL, Nodejs(frontend)；
 

## Delevopment - Backend
* Finish "Prepare for development" and read the tutorial of Django https://www.djangoproject.com/;
git fork and clone!
`git clone https://github.com/irisxiu666/Pikachu-Housing.git` 
* Activate virtual environment:
`virtualenv venv, source venv/bin/activate`
* Install requirements, execute `pip install -r requirements.txt`;
* Execute `python manage.py migrate`, then `python manage.py runserver 8000`，the Django server starts and connect to the local database；
* Before programming, `git pull`;
* Do something exciting；
* Pull request if you want to make contribution;

## Delevopment - Frontend
* Finish "Prepare for development" and read the tutorial of Vue: https://vuejs.org/index.html ;
* Finish "Development - Backend", `cd frontend`, execute `npm install`;
* Create some exciting buttons；
* Check layout by `npm run dev`, browsing 127.0.0.1:3000（Use chrome to debug）；
* Before submission，`cd frontend` , execute `npm run build` to pack your code；
* Pull request if you want to make contribution;


