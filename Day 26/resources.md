# Resources

## Today's source code
* requirements.txt - Python libraries used today
  * pip install -r requirements.txt
* "01 SQL Alchemy": Sample SQLite database using SQLAlchemy. Used in later examples
* "02 Flask Hello World": Extremely simple Flask application. Creates a single end point at "/"
* "03 Flask SQLAlchemy": Integrates the database from step 1, plus SQLAlchemy, into the Flask app. Just enough to show one single value
* "04 With Template": Shows a complete HTML page, based on a Flask/Jinja2 template. Shows all data from the SQLite database
* "05 With Alembic": Adds in Alembic to facilitate database changes using migrations
* "05a - Final version - With Alembic": As the previous version, but with a single field added to the books table, done using a migration

## Documentation
* [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
    * In particular, chapters 1, 2 and 4
* [SQLAlchemy on RealPython](https://realpython.com/python-sqlite-sqlalchemy/)
* [SQLAlchemy, official documentation](https://www.sqlalchemy.org/)
    * Note the difference between SQLAlchemy Core and ORM. We're using ORM
* [Alembic](https://alembic.sqlalchemy.org/en/latest/)
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
* [Jinja2 - Flask's default templating language](https://jinja.palletsprojects.com/en/2.11.x/)
