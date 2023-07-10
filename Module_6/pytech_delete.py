
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ox7kqsr.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient("mongodb+srv://admin:admin@cluster0.ox7kqsr.mongodb.net/?retryWrites=true&w=majority")
db = client.pytech
pytech = db.students

#Call_find()

db.student.find()

#Insert one

doc =[ 

    { 

        "student_id": "1010", 

        "first_name": "Linda", 

        "last_name": "Walters" 
    }
]
 
for doc in docs:
    new_student_id = pytech.insert_one(record).inserted_id
    print(new_student_id)


#Find_one()
print(pytech.find_one({"student_id": "1009"}))

#Delete_one 

db.student.remove({"student_id":"1010"})

#Call_find()

db.student.find()



  -- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY --
Student ID: 1007
First Name:Greg 
Last Name: RAY

Student ID: 1008
First Name: Victoria
Last Name: Love

Student ID:1009
First Name: Micheal 
Last Name: Reed

-- INSERT STATEMENTS --
  Inserted student record into the students collection with document_id 5f0cd4c09d0e680b7b424

-- DISPLAYING STUDENT TEST DOC --
Student ID:1010
First Name: Linda 
Last Name: Walters

  -- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY --
Student ID: 1007
First Name:Greg 
Last Name: RAY

Student ID: 1008
First Name: Victoria
Last Name: Love

Student ID:1009
First Name: Micheal 
Last Name: Reed




