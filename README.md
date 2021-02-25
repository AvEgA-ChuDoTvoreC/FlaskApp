# FlaskApp
## Temp project to learn Flask

Ok folks here is my flask project which should be integrated with some other projects in future.

It's created for learning flask basics

You can try it right now:

```bash
$ git clone https://github.com/AvEgA-ChuDoTvoreC/FlaskApp.git
$ cd FlaskApp
$ pyenv virtualenv 3.9.2 flask
$ source flask/bin/activate
```
```bash
$ export FLASK_APP=run.py
$ flask run --host=0.0.0.0 --port=5000
```
or
```bash
python run.py
```
and check your browser at https://0.0.0.0:5000
also don't forget register

Don't forget about database creation ```brew install postgresql```

## Project overview

```
FlaskApp data structure

.
├── README.md
├── app_folder        - main folder project
│   ├── __init__.py   - some kinda configurator file
│   ├── models.py     - most of all db functions
│   ├── routes.py     - all flask routes to html pages
│   ├── static        - folder with .css .js files wich provides html-page style 
│   ├── templates     - folder with .html templates
│   └── views         - folder with nothing (soon will be views.py file)
├── requirements.txt  - pip freeze >  (all side packages here)
├── run.py            - FlaskApp starter      
└── tmp               
    ├── mysql         - just db follder
    └── postgresql    - just db follder


FlaskApp
.
├── README.md
├── app_folder
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── static
│   │   ├── css
│   │   │   └── bootstrap.min.css
│   │   ├── img
│   │   │   └── ormrO7X6yI.jpg
│   │   ├── js
│   │   │   └── bootstrap.min.js
│   │   └── upload_folder
│   │       └── avatar
│   │           ├── -ormrO7X6yI.jpg
│   │           ├── 16305.jpg
│   │           ├── 19483.jpg
│   │           ├── 2.jpg
│   │           └── 920.jpg
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── main.html
│   │   ├── register.html
│   │   ├── upload.html
│   │   ├── upload2.html
│   │   └── welcome.htm
│   └── views
├── requirements.txt
├── run.py
└── tmp
    ├── mysql
    └── postgresql
        └── PG_13_202007201


```


## Some usefull stuff
```bash
pip install flask
pip install flask-sqlalchemy
pip install psycopg2

pip freeze > requirements.txt
mkdir app
mkdir app/static
mkdir app/templates
mkdir app/views
mkdir tmp

brew install postgresql
brew install mysql
pip install psycopg2 flask-migrate   #(psycopg2-binary?)
```

PostgreSQL:
```bash
$ pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start
$ psql -l && psql --help
$ psql -U USERNAME -d DBNAME
=# SHOW DATA_DIRECTORY;
$ pg_config
```
Sql problems
```html
https://dataschool.com/learn-sql/how-to-start-a-postgresql-server-on-mac-os-x/
https://www.codementor.io/@engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb
```
```bash
=# CREATE ROLE username WITH LOGIN PASSWORD 'quoted password'
=# ALTER ROLE username CREATEDB REPLICATION;
=# CREATE TABLESPACE tablespace_name [ OWNER user_name ] LOCATION 'directory'
=# CREATE TABLE sport (sports_name TEXT, country TEXT, score INT);
=# DROP TABLE [IF EXISTS] table_name;
=# DROP TABLE [IF EXISTS] table_name [CASCADE | RESTRICT];
=# INSERT INTO users(id, login, password) VALUES (1, 'Xxx', '123');
=# SELECT * FROM table_name WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';
=# CREATE TABLE films2 AS TABLE films;
=# CREATE TABLE [IF NOT EXIST] films (
      code        char(5),
      title       varchar(40),
      did         integer,
      date_prod   date,
      kind        varchar(10),
      len         interval hour to minute,
      CONSTRAINT production UNIQUE(date_prod)
  );

pip install flak-login
```
Usefull links about Flask
```html
<h1>Flask</h1>
https://flask.palletsprojects.com/en/0.12.x/quickstart/
https://flask.palletsprojects.com/en/1.1.x/api/#message-flashing
https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.after_request
https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/?highlight=message%20flashing

<h1>Jinja templates</h1>
https://jinja.palletsprojects.com/en/2.11.x/templates/

<h1>Flask-SQLAlchemy</h1>
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/?highlight=column
https://flask-sqlalchemy.palletsprojects.com/en/2.x/customizing/?highlight=import%20datetime

<h1>Flask-Login</h1>
https://flask-login.readthedocs.io/en/latest/

<h1>SQLAlchemy UniqueConstraint</h1>
https://docs.sqlalchemy.org/en/13/core/constraints.html#unique-constraint

<h1>werkzeug.security.check_password_hash</h1>
https://werkzeug.palletsprojects.com/en/0.16.x/utils/#werkzeug.security.check_password_hash

<h1>File Uploads with Flask</h1>
https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask

<h1>Icons</h1>
https://blog.nucleoapp.com/the-guide-to-integrating-and-styling-icon-systems-svg-sprites-svg-symbols-and-icon-fonts-da7c424dac1b
```


