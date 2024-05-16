
from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI
from fastapi import HTTPException
from Entities import Gender, Role , Employee

app=FastAPI()



db: List[Employee] = [
 Employee(
 id=uuid4(),
 first_name="John",
 last_name="David",
 gender=Gender.male,
 roles=[Role.manager],
 ),
 Employee(
 id=uuid4(),
 first_name="Kamila",
 last_name="Parker",
 gender=Gender.female,
 roles=[Role.architect],
 ),
 Employee(
 id=uuid4(),
 first_name="James",
 last_name="Cameron",
 gender=Gender.male,
 roles=[Role.developer],
 ),
 ]

#get employee
@app.get("/api/v1/employees")
async def get_employee():
    return db

# create employee
@app.post("/api/v1/employee")
async def create_employee(employee: Employee):
    db.append(employee)
    return employee.id


@app.delete("/api/v1/delete/{id}")
async def delete_employee(id: UUID):
    flag=False

    for employee in (db):
        if employee.id == id:
            db.remove(employee)
            flag=True

    if flag==False:
        raise HTTPException(
            detail=f"delete employee failed, id {id} not found",
            status_code=400
        )
    return

