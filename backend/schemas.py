from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):
    roll_no: int
    name: str
    email: EmailStr
    branch : str


class StudentResponse(BaseModel):
    id: int
    roll_no: int
    name: str
    email: str
    branch :str

    class Config:
        from_attributes = True