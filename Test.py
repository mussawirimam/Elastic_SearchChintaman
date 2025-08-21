import json

mydocs= { 
    "Students":    {    
    "Bob":{"sername":"{sername:rathore,age:31,\"under19:False,speedofiq:1.3}","age":30,"under19":"True","speedofiq":1.2},
    "mic": {"sername":"rathore","age":31,"under19":"False","speedofiq":1.3},
    "quick": {"sername":["romey","tommy"],"age":30,"under19":"True","speedofiq":1.2}
    }
}

student = mydocs.get("Students")      

print(student.get("Bob"))






