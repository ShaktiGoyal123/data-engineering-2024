#pip install fastapi
#pip install uvicorn

from typing import Union

from fastapi import FastAPI

from enum import Enum

class ProductType(str, Enum):
    computer = "COMPUTER"
    printer = "PRINTER"
    monitor = "MONITOR"

app = FastAPI()

@app.get("/")
def read_root():

    return {"Hello Dell Data Engg Team": "Welcome to FASTAPI"}


@app.get("/products/{product_id}")

async def read_product(product_id: int, name: Union[str, None] = None):

    return {"product_id": product_id, "product_name": name}

@app.get("/products/{product_id}/{product_type}")
async def get_product_type(product_type: ProductType):
    if product_type is ProductType.computer:
        return {"product_type": product_type, "message": "Computers and Laptops"}

    if product_type is ProductType.monitor:
        return {"product_type": product_type, "message": "Monitors LCD and LED"}

    
    return {"product_type": product_type, "message": "Printers"}

@app.post("/products/", status_code=201)
async def create_product(name: str,product_id: int):
    return {"product_name": name,"product_id":product_id}