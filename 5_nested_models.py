from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address
    
address_dict = {"city": "New York", "state": "NY", "street": "123 Main St", "zip_code": "10001"}

address1 = Address(**address_dict)
patient_dict = {"name": "Sam", "gender": "male", "age": 30, "address": address1} 

patient1 = Patient(**patient_dict)
print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.address.zip_code)