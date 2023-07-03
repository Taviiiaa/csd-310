https://github.com/Taviiiaa/csd-310.git
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


-- INSERT STATEMENTS --
Insert student record Greg Walsh into the students collections with the document id 1008
Insert student record Victoria Love into the students collections with the document id 1008
Insert student record Micheal Reed into the students collections with the document id 1008
