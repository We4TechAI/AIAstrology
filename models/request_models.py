from pydantic import BaseModel

class AstrologyRequest(BaseModel):
    location: str
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int

class AstrologyResponse(BaseModel):
    observation: list[str]