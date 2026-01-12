from pydantic import BaseModel


# this is for pydantic but will not have any db related code
class Product(BaseModel):
    id:int
    name:str
    desc:str
    price:float
    qty:int
    
    # constructor
    # def __init__(self, id:int, name:str, desc:str, price:float, qty:int):
    #     self.id = id
    #     self.name = name
    #     self.desc = desc
    #     self.price = price
    #     self.qty = qty
    
    # done by pyadantic iteself
    