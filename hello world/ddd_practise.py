from pydantic import BaseModel, ValidationError
from enum import Enum


class PropertyType(str, Enum):
    residential = "residential"
    commercial = "commercial"


class Property(BaseModel):
    name: str
    owner: str
    lat: float
    lon: float
    type: PropertyType

    class Config:
        use_enum_values = True


property = Property(name='Manamaiju', owner="Rishav",
                    lat=1.2, lon=3.4, type="residential")
print(property.dict())
