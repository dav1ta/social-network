# Installation

- create postgresql database named social_network
- Install dependencies requirements.txt
- run  `python manage.py makemigrations profiles feed`
- run `python manage.py migrate`
- create superuser in case for admin page `python manage.py createsuperuser`
- run `python manage.py test`
- run `python manager.py runserver`
- go to /feed 
- check /admin


## Additional info

### Why there are no indexes
queries in this project only uses foreign keys to search wich is automatically indexed in database.
if we needed some search we probably like to install some postgresql extenstions like fuzzy matching with 
levenstein distance or full text search. because indexing this columns in search still gives us sequential scan.

### why there is no caching 
data is too dynamic i could probably used some caching backend like redis or memcached.
but data is dynamic and different for every user. 
also there are no big perfomance difference as this article says  
(redis vs postgresql vs memcached)[](https://www.cybertec-postgresql.com/en/postgresql-vs-redis-vs-memcached-performance/)
i have used @cached_property for some caching for templates and .only() for nessecery data.

### why i have used custom user model for extending user authentication instead of OneToOne realating to another model

i throught it would avoid more select, or insert queries. because of syncing with signals

### why there are no annotations
despite i am big fan of annotations and type checkers, i could not find good resource or project to make annotations with django.
but i have written much on FastApi

