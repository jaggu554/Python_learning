import json

with open("Chunking/employees.json") as f:
    data=json.load(f)

chunks=[]

for dept in data["departments"]:
    text=f"department {dept["name"]}\n"

    for emp in dept["employees"]:
        text+=f"""Name :{emp["name"]}\nRole :{emp["role"]}\nSkills :{" , ".join(emp["skills"])} \n"""

    chunks.append(text)


for i,chunk in enumerate(chunks):
    print(f"---chunk :{i+1}---\n")
    print(chunk)

    
