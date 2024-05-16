from typing import List
from uuid import UUID,uuid4
from fastapi import FastAPI
from fastapi import HTTPException
from demo_entities import Gender, Role, Employee

app = FastAPI()

db: List[Employee] = [
 Employee(
 id=uuid4(),
 first_name="John",
 last_name="David",
 gender=Gender.male,
 roles=[Role.user],
 ),
 Employee(
 id=uuid4(),
 first_name="Kamila",
 last_name="Parker",
 gender=Gender.female,
 roles=[Role.user],
 ),
 Employee(
 id=uuid4(),
 first_name="James",
 last_name="Cameron",
 gender=Gender.male,
 roles=[Role.user],
 ),
 ]

#get employees
@app.get("/api/v1/employees")
async def get_employees():
    return db

# add new employee
@app.post("/api/v1/employees")
async def create_employee(employee: Employee):
 db.append(employee)
 return {"id": employee.id}

#delete an employee
@app.delete("/api/v1/employees/{id}")
async def delete_employee(id: UUID):
    flag=False
    for employee in db:
        if employee.id == id:
            db.remove(employee)
            flag=True

    if flag==False: 
        raise HTTPException(
    status_code=404, detail=f"Delete employee failed, id {id} not found."
    )

    return