x=10

y=x
print(id(x))
print(id(y))

x=5

print("x values ",x)
print("y values ",y)

print(id(x))
print(id(y))

# mutable changes in list 
list1=[12,23,24,25,26]

list2=list1

print(id(list1))
print(id(list2))

# Made the chanes for list1. but it reflects to list2 also 
list1.append(50)

print(list1)
print(list2)

print("="*60)
def add_items(item,shopping_list=[]):
    shopping_list.append(item)
    return shopping_list

print(add_items("banana"))
print(add_items("cake"))
print(add_items("Orange"))

print("="*60)
# for mutable objects create none not defaults .
def add_items(item,shopping_list=None):
    if shopping_list is None:
        shopping_list=[]
        shopping_list.append(item)
    return shopping_list

print(add_items("banana"))
print(add_items("cake"))
print(add_items("Orange"))