from app import create_app
from app.models import db, Category, Product, Client, Order

def seed_data():
    app = create_app()
    with app.app_context():
        db.create_all()
        
        if Category.query.first():
            print("Database already seeded")
            return
        
        cat1 = Category(name="Electronics", description="Electronic devices")
        cat2 = Category(name="Clothing", description="Apparel and fashion")
        cat3 = Category(name="Books", description="Books and publications")
        
        db.session.add_all([cat1, cat2, cat3])
        db.session.commit()
        
        prod1 = Product(name="Laptop", description="High performance laptop", price=2999.99, stock=10, category_id=cat1.id)
        prod2 = Product(name="Smartphone", description="Latest smartphone model", price=1999.99, stock=25, category_id=cat1.id)
        prod3 = Product(name="T-Shirt", description="Cotton t-shirt", price=49.99, stock=100, category_id=cat2.id)
        prod4 = Product(name="Jeans", description="Denim jeans", price=89.99, stock=50, category_id=cat2.id)
        prod5 = Product(name="Python Book", description="Learn Python programming", price=79.99, stock=30, category_id=cat3.id)
        
        db.session.add_all([prod1, prod2, prod3, prod4, prod5])
        db.session.commit()
        
        client1 = Client(name="John Doe", email="john@example.com", phone="11999999999", address="123 Main St")
        client2 = Client(name="Jane Smith", email="jane@example.com", phone="11888888888", address="456 Oak Ave")
        
        db.session.add_all([client1, client2])
        db.session.commit()
        
        order1 = Order(client_id=client1.id, total=2999.99, status="completed")
        order2 = Order(client_id=client2.id, total=169.98, status="pending")
        
        db.session.add_all([order1, order2])
        db.session.commit()
        
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()