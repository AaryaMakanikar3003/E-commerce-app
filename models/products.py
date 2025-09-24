from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    productId: str
    name: str
    description: Optional[str]=None
    price: float
    compare_at_price: Optional[float]=None
    cost_per_item: float
    images:list
    weight: float
    dimensions:dict[str, float]
    inventory_quantity: int
    status: str
    