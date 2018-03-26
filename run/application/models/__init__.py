#!/usr/bin/env python3

# This is our model.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from application.models import acl as USER

# module = Flask(__name__)
# module.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///master.db"
# module.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# db = SQLAlchemy(module)

# class Customer(db.Model):
class Customer():
    # def setup(self, omnibus):
    #
    #     # Write the query method in the Customer class that's called in the controller.
    #
    #     # # db = SQLAlchemy(omnibus)
    #     # db = SQLAlchemy(omnibus)
    #     # # model = db.Model
    #     # __tablename__ = "users"
    #     # id = db.Column(db.Integer, primary_key=True)
    #     # username = db.Column(db.String(40), unique=True)
    #     # password = db.Column(db.String(255))
    #     # email = db.Column(db.String(120), unique=True)
    #     # role = db.Column(db.SmallInteger, default=USER.USER)
    #     # status = db.Column(db.SmallInteger, default=USER.NEW)
    #     import sqlite3
    #     connection = sqlite3.connect('run/datastore/sql.db', check_same_thread=False)
    #     cursor = connection.cursor()
    #     # id       = cursor.execute(';')
    #     # username = cursor.execute(';')
    #     # password = cursor.execute(';')
    #     # email    = cursor.execute(';')
    #     # role     = cursor.execute(';')
    #     # status   = cursor.execute(';')
    #     cursor.close()
    #     connection.close()

    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = password
        self.email = email

    def get_customer(self, customer_id):
        # Check if the username exists (in the database)
        # TODO Re-factor the following into an ORM for PostgreSQL
        import sqlite3
        # --> Open up a connection and cursor objects
        connection = sqlite3.connect('run/datastore/sql.db', check_same_thread=False)
        cursor     = connection.cursor()
        # --> Execute a query
        cursor.execute('SELECT * FROM users WHERE id="{0}";'.format(customer_id))
        user_details = cursor.fetchone()
        cursor.close()
        connection.close()
        print(user_details)
        return user_details

    def status(self):
        return USER.STATUS[self.status]

    def role(self):
        return USER.ROLE[self.role]

    def register(self, username, password):
        # Check if the username exists (in the database)
        # TODO Re-factor the following into an ORM for PostgreSQL
        import sqlite3
        # --> Open up a connection and cursor objects
        connection = sqlite3.connect('run/datastore/sql.db', check_same_thread=False)
        cursor     = connection.cursor()
        # --> Execute a query
        cursor.execute('SELECT COUNT(*) FROM users WHERE username="{0}";'.format(username))
        tally = int(cursor.fetchall()[0][0])
        if tally == 0:
            # State: Username doesn't exist
            # Store submitted username and password in the database
            # TODO Mitigate a hypothetical SQL injection attack by
            #      replacing the format invocation with something else.
            cursor.execute('INSERT INTO users(username, password) VALUES("{0}","{1}");'.format(username, password))
            connection.commit()
            cursor.execute('SELECT MAX(id) FROM users;')
            customer_id = cursor.fetchone()[0]
            cursor.close()
            connection.close()
            # FIXME Assign objects to `g` and `session`
            return customer_id
        else:
            # State: Username exists
            # FIXME
            pass
        # Close the aforementioned connection and cursor objects
        cursor.close()
        connection.close()

    def login():
        pass

    def __repr__(self):
        return "<Customer %r>" % (self.username)
