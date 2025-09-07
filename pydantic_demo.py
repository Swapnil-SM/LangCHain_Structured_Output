from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import email_validator

class Student(BaseModel):

    name: str = 'nitish' # default value
    age: Optional[int] = None
    email: EmailStr   #built in email validator in pydantic
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student') # gt = greater than, lt = less than


new_student = {'age':'32', 'email':'abc@gmail.com'}

student = Student(**new_student)

print(student)  # Student(name='nitish', age=32,
print(type(student)) # <class 'pydantic.main.Student'>

student_dict = dict(student)  # converting pydantic model to dictionary

print(student_dict['age']) 

student_json = student.model_dump_json()