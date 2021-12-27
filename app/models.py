from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(40), nullable = False, unique = True, index = True)
    email = db.Column(db.String(100), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False)
    gender = db.Column(db.String(6), nullable = False)
    # add ip addresses model 
    dob = db.Column(db.DateTime, nullable = False)
    status = db.Column(db.Integer, nullable = False)
    

#roles 

#category

#post

#reply

#ip