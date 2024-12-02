from application.database import db

class User(db.Model):
    __tablename__="user"
    phoneNo=db.Column(db.Integer,primary_key=True)
    fName=db.Column(db.String,nullable=False)
    lName=db.Column(db.String,nullable=False)
    mail=db.Column(db.String,nullable=False,unique=True)
    city=db.Column(db.String)
    district=db.Column(db.String)
    password=db.Column(db.String,unique=True)
class Tour(db.Model):
    __tablename__="tour"
    
    country=db.Column(db.String,primary_key=True)
    destination=db.Column(db.String)
    description=db.Column(db.String)
    cost=db.Column(db.Integer)
class TripPlaced(db.Model):
    __tablename__="tripPlaced"
    phoneNo=db.Column(db.Integer,primary_key=True)
    destination=db.Column(db.String,nullable=False)
class Hotel(db.Model):
    __tablename__ = 'hotels'  # Define the table name in the database

    # Define the columns of the hotels table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Unique identifier for each hotel
    destination = db.Column(db.String(255), nullable=False)  # Destination name (e.g., France, Japan)
    hotel_name = db.Column(db.String(255), nullable=False)  # Name of the hotel (e.g., 'Le Grand Paris')
    price = db.Column(db.Float, nullable=False)  # Price of the room per night
    