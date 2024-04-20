from pydantic import (
    BaseModel,
    ConfigDict, 
    EmailStr,
)

# UserCreate is for creating a new user
class UserCreate(BaseModel):
    name: str
    username: str
    email: EmailStr

    model_config: ConfigDict = {
        "json_schema_extra" : {
            "example": {
                "name": "John Doe",
                "username": "johndoe",
                "email": "johndoe@example.com"
            }
        }
    }

# UserOut is for returning a user
class UserOut(BaseModel):
    username: str
    name: str
    email: EmailStr
    
    model_config: ConfigDict = {
        "from_attributes": True,
    }