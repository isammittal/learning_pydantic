from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=50, title="Patient Name", description="Full name of the patient in less than 50 characters", example=["Alex", "John", "Romie"])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True, description="Weight in kg", example=70.5)]
    married: Annotated[bool, Field(default=False, description="Is the patient married?")]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print("Updated")
    
patient_info = {"name": "sam","email": "sammittal2010@gmail.com", "linkedin_url": "http://isammittal.netlify.app", "age": "14", "weight": 56.4, "contact_details": {"phone": "6239463312"}}

patient1 = Patient(**patient_info)
update_patient_data(patient1)
