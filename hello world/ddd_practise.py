from pydantic import BaseModel, ValidationError
from enum import Enum
from typing import List


class PropertyType(str, Enum):
    residential = "residential"
    commercial = "commercial"


class Property(BaseModel):
    name: str
    owner: str
    lat: float
    lon: float
    type: PropertyType
    energy_production: float

    class Config:
        use_enum_values = True

    def update_availablity(self, subscribed_quantity):
        self.energy_production -= subscribed_quantity

    def add_to_marketplae(self):
        marketplace=Marketplace(properties=[self])
        return marketplace.dict()


class Marketplace(BaseModel):
    properties: List[Property]


property = Property(name='Manamaiju', owner="Rishav",
                    lat="1.2", lon=3.4, type="residential", energy_production=120.10)
# print(property.dict())
print(property.add_to_marketplae())

