from pydantic import BaseModel

class ProductSchema(BaseModel):
        id: str
        name: str
        price: float
        currency: str