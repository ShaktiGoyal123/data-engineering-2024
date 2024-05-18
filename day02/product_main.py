
from typing import List
from uuid import UUID,uuid4
from fastapi import FastAPI
from fastapi import HTTPException
from product_entity import Product, ProductType


app=FastAPI()

# creating database with dummy product details

db: List[Product]=[
    Product(
        id=uuid4(),
        product_code="P101",
        product_description="Laptop",
        product_type=ProductType.fgi,
        price=897.12,
        stock_qty=15,
    ),
    Product(
        id=uuid4(),
        product_code="P102",
        product_description="Server",
        product_type=ProductType.fgi,
        price=40897.72,
        stock_qty=25,
    ),
    Product(
        id=uuid4(),
        product_code="P103",
        product_description="2 Year Extended Warrenty",
        product_type=ProductType.service,
        price=200.00,
        stock_qty=11,
    ),        

]


# get all products
@app.get("/api/v1/products")
async def get_products():
    return db

# get a specific product by id
@app.get("/api/v1/products/{product_id}")
async def get_product(product_id: UUID):
    dummy_flag=False
    for prod in (db):
        if prod.id==product_id:
            dummy_flag=True
            return {"id":prod.id,"product_code":prod.product_code,
                    "product_description":prod.product_description,
                    "product_type":prod.product_type,
                    "price":prod.price,
                    "stock_qty":prod.stock_qty
                    }
        
    if dummy_flag==False:
        raise HTTPException(
            status_code=404, detail="product not found, {product_id} not found"
        )




# create a product
@app.post("/api/v1/products")
async def create_products(product: Product):
    db.append(product)
    return{"id":product.id}


# delete a product
@app.delete("/api/v1/products/{product_id}")
async def get_product(product_id: UUID):
    dummy_flag=False
    for prod in (db):
        if prod.id==product_id:
            dummy_flag=True
            db.remove(prod)
        
    if dummy_flag==False:
        raise HTTPException(
            status_code=404, detail=f"product not found, {product_id} not found"
        )
    

# update a product    
@app.patch("/api/v1/products/{prod_id}")
async def update_product(prod_id:UUID,product_desc: str,stock_qty: int):
    dummy_flag=False
    for prod in (db):
        if prod.id==prod_id:
            dummy_flag=True
            prod.product_description=product_desc
            prod.stock_qty=stock_qty

        
    if dummy_flag==False:
        raise HTTPException(
            status_code=404, detail=f"product not found, {prod_id} not found"
        )