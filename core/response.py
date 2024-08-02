from pydantic import BaseModel, Field

    

class ItemResponse(BaseModel):
    name: str
    description: str = None
    price: float = Field(..., gt=100)
    tax: float = None
