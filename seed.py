"""Seed file to make sample data for pets_db."""

from models import Pet, db
from app import app

# Create all tables
with app.app_context():
    db.drop_all()
    db.create_all()

# If table isn't empty, empty it
    Pet.query.delete()

# Add pets
cooper = Pet(name="Cooper", species="dog",
             photo_url="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2021%2F07%2F15%2Flab-face-aussie-tricolor-lunyaussiedor-2000.jpg", age=3)

harley = Pet(name="Harley", species="dog",
             photo_url="https://t2.ea.ltmcdn.com/en/posts/4/0/9/10_things_you_should_know_about_golden_retrievers_904_600_square.jpg", age=4, available=True)

rosie = Pet(name="Rosie", species="dog",
            photo_url="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2020%2F12%2F15%2Ftoy-poodle-992302634-2000.jpg", age=1, notes="Rosie is very energetic.", available=True)


# Add new objects to session, so they'll persist
with app.app_context():
    db.session.add(cooper)
    db.session.add(harley)
    db.session.add(rosie)

# Commit--otherwise, this never gets saved!
    db.session.commit()
