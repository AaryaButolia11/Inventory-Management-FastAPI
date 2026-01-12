from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware as CORS
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORS,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
)

database_models.Base.metadata.create_all(bind=engine)

# DB init
products = [
    Product(id=1,name="phone",desc="smart phone",price=699.99,qty=50),
    Product(id=2,name="laptop",desc="gaming laptop",price=1299.99,qty=30),
    Product(id=3,name="tablet",desc="android tablet",price=399.99,qty=20),
    Product(id=4,name="headphones",desc="wireless headphones",price=199.99,qty=100),
    Product(id=5,name="smartwatch",desc="fitness smartwatch",price=249.99,qty=75)
]

def init_db():
    db = session()
    if db.query(database_models.Product).count() == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

init_db()

# Routes
@app.get("/products/")
def get_all_products(db: Session = Depends(get_db)):
    return db.query(database_models.Product).all()

@app.get("/products/{id}")
def get_product(id: int, db: Session = Depends(get_db)):
    prod = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if prod:
        return prod
    return {"message": "Product not found"}

@app.post("/products/")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_prod = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_prod:
        db_prod.name = product.name
        db_prod.desc = product.desc
        db_prod.price = product.price
        db_prod.qty = product.qty
        db.commit()
        return {"message": "Product updated successfully"}
    return {"message": "No product found to update"}

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_prod = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_prod:
        db.delete(db_prod)
        db.commit()
        return {"message": "Product deleted successfully"}
    return {"message": "No product found to delete"}
