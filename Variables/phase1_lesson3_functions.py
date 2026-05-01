def add(a,b):
    return a+b
result=add(5,6)

print(result)
print(result*10)

# example of default paramters

def greet(name,message="Hello"):
    return f"{message} {name}"

print(greet("jaggu"))
print(greet("jaggu","Hi"))