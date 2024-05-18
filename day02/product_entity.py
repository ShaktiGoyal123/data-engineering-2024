from typing import List, Optional 
from uuid import UUID, uuid4 
from pydantic import BaseModel 
from enum import Enum


class ProductType(str, Enum):
    service="Service"
    fgi="Furnished Goods Product"




class Product(BaseModel):
    id: Optional[UUID] = uuid4()
    product_code: str
    product_description: str
    product_type: ProductType
    price: float
    stock_qty: int
