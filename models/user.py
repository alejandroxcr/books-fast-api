from typing import Optional
from pydantic import BaseModel, Field

class User:
  id: int
  name: str
  lastName: str
  position: str

  def __init__(self, id, name,lastName, position):
    self.id = id
    self.name = name
    self.lastName = lastName
    self.position = position

  def fullName(self):
    return f"{self.lastName}, {self.name}"

# Used to validate request objects.
# It must extend from base model. 
class UserRequest(BaseModel):
  id: Optional[int] = Field(description="Id is not required.")
  name: str
  lastName: str
  position: str

  # This class adds documentation in swagger.
  class Config:
    json_schema_extra = {
      "example":{
        "name": "John",
        "lastName":"Smith",
        "position":"HR Agent"
      }
    }