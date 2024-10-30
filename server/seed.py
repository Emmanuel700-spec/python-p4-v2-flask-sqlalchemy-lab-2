#!/usr/bin/env python3

from app import app
from models import db, Customer, Review, Item

def seed_data():
    with app.app_context():
        # Clear existing records
        db.drop_all()  # Drop all tables to clear existing data
        db.create_all()  # Recreate the tables

        # Seed Customers
        customer1 = Customer(name='Tal Yuri')
        customer2 = Customer(name='Raha Rosario')
        customer3 = Customer(name='Luca Mahan')

        # Add customers to session
        db.session.add_all([customer1, customer2, customer3])
        db.session.commit()  # Commit after adding customers

        # Seed Items
        item1 = Item(name='Laptop Backpack', price=49.99)
        item2 = Item(name='Insulated Coffee Mug', price=9.99)
        item3 = Item(name='6 Foot HDMI Cable', price=12.99)

        # Add items to session
        db.session.add_all([item1, item2, item3])
        db.session.commit()  # Commit after adding items

        # Print Customer and Item IDs for debugging
        print(f"Customer IDs: {customer1.id}, {customer2.id}, {customer3.id}")
        print(f"Item IDs: {item1.id}, {item2.id}, {item3.id}")

        # Seed Reviews
        reviews = [
            Review(comment="Zipper broke the first week", customer_id=customer1.id, item_id=item1.id),
            Review(comment="Love this backpack!", customer_id=customer2.id, item_id=item1.id),
            Review(comment="Coffee stays hot for hours!", customer_id=customer1.id, item_id=item2.id),
            Review(comment="Best coffee mug ever!", customer_id=customer3.id, item_id=item2.id),
            Review(comment="Cable too short", customer_id=customer3.id, item_id=item3.id)
        ]

        # Add reviews to session
        db.session.add_all(reviews)
        
        # Commit all reviews to the database
        db.session.commit()

if __name__ == "__main__":
    seed_data()
