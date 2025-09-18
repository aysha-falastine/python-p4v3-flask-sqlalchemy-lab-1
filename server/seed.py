#!/usr/bin/env python3
# server/seed.py

from app import app
from models import db, Earthquake

with app.app_context():

    # Delete all rows in the "earthquakes" table
    Earthquake.query.delete()

    # Add several Earthquake instances with explicit IDs
    db.session.add(Earthquake(id=1, magnitude=9.5, location="Chile", year=1960))
    db.session.add(Earthquake(id=2, magnitude=9.2, location="Alaska", year=1964))
    db.session.add(Earthquake(id=3, magnitude=8.6, location="Alaska", year=1946))
    db.session.add(Earthquake(id=4, magnitude=8.5, location="Banda Sea", year=1934))
    db.session.add(Earthquake(id=5, magnitude=8.4, location="Chile", year=1922))

    # Commit the transaction
    db.session.commit()
