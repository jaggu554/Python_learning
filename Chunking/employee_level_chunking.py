import json

with open("Chunking/employees.json","r") as f:
    data=json.load(f)

chunks=[]

for dept in data["departments"]:
    for emp in dept["employees"]:
        chunk=f"""
        Deparment :{dept["name"]}
        Name :{emp["name"]}
        Role :{emp["role"]}
        Skills :{" , ".join(emp["skills"])}
        Projects :{", ".join(emp["projects"])}
"""
        chunks.append(chunk)


for i,chunk in enumerate(chunks):
    print(f"\n---{i+1}---")
    print(chunk)