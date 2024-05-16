from typing import List, Optional 
from uuid import UUID, uuid4 
from pydantic import BaseModel 
from enum import Enum



class Gender(str, Enum):
    male="Male"
    female="Female"

class Role(str, Enum):
    architect ="Architect"
    manager ="Manager"
    lead = "Technical Lead"
    developer = "Developer"

class Employee(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Role]

