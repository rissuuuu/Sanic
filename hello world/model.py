from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str

user=User(id="1",name='Rishav')
print(user)