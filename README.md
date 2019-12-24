# Introduction

The goal of this project is to provide minimalistic django project template that everyone can use, which _just works_ out of the box and has the basic setup you can expand on. 

Silvertec-server was made with Django 2.2.7 and Django Rest Framework 3.10.3

### Main features

* API to create and list orders

* Front end Project to show, create and filter orders.

* Docker

* Postgres by Default in Docker Image

* Unit tests

* PEP 8 Style Guide

# Usage

To start this project:

### Using Docker-Compose

If environment already have docker just run the following command:

    $ docker-compose up --build

This will setup a image with a empty Postgres DB. 

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https://github.com/douglastmp/silvertec-server-v2/zipball/master \
      --extension=py,md \
      silvertec-server
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django startproject \
      --template=https://github.com/douglastmp/silvertec-server-v2/zipball/master \
      --extension=py,md \
      <project_name>
      
      
After that just install the local dependencies, run migrations, and start the server.


# Silvertec Server 

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/douglastmp/silvertec-server-v2.git
    $ cd silvertec-server
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

### Content
The start page of the project it's a swagger page containing all routes and schemes to do requests 
using the base Base URL: "127.0.0.1:8000/api".

To do a POST Order request it's required the other models created in the Database, this is possible 
making POST request for the others models or just adding them in the Admin page. 

To use the Admin page it's required to have a Super User, to create that just type:

    $ python manage.py createsuperuser


To Create Orders it's only possible by POST request because of the validations.


### Known issues and limitations

In development time was found one issue that wasn't possible to close in time to deliver the project
related to cors headers. Even using a Django-cors-headers the problem persisted and to continue 
developing the project was user a chrome extension named Moesif CORS even knowing that this is not 
the solution or the best practise


### Prints of the Project
To see some print's of localhost pages use the following link:
https://drive.google.com/drive/folders/1vfF4nruDv_HpuC4QO56qR23VlikFEex7?usp=sharing