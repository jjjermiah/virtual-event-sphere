from pydantic import (
    BaseModel,
    ConfigDict,
)

class CreateEvent(BaseModel):
    name: str
    description: str
    date: str
    time: str

    model_config: ConfigDict = {
        "json_schema_extra" : {
            "example": {
                "name": "Event Name",
                "description": "Event Description",
                "date": "2021-01-01",
                "time": "12:00:00"
            }
        }
    }
    
class EventOut(BaseModel):
    name: str
    description: str
    date: str
    time: str
