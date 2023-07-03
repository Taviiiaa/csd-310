
from pymongo import MongoClient 


client=MongoClient 

db=client 

pytech =db 

records =[ 

    { 

        "student_id": "1007", 

        "first_name": "Greg", 

        "last_name": "Walsh" 

    }, 

    { 

        "student_id": "1008", 

        "first_name": "Victoria", 

        "last_name": "Love" 

    }, 

    { 

        "student_id": "1009", 

        "first_name": "Michael", 

        "last_name": "Reed" 

    } 

] 



-- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY --
Student ID: 1007
First Name:Greg 
Last Name: Walsh

Student ID: 1008
First Name: Victoria
Last Name: Love

Student ID:1009
First Name: Micheal 
Last Name: Reed

-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY -- 
Student ID: 1007 
First Name: Greg 
Last Name: Walsh

End of program any key to countine...
