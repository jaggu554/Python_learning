print("="*60)
print("Example 1 : with simple Loop")
print("="*60)

fruits=["apple","Mango","Orange","sapota"]
for i in fruits:
    print(i)


print("="*60)
print("Example 2: with index loop")
print("="*60)

for index,fruit in enumerate(fruits):
    print(f"Index :{index} , Fruit: {fruit}")


print("="*60)
print("Example 3 : Nested Loop")
print("="*60)

matrix=[[1,2,3],[4,5,6],[7,8,9]]

for row in matrix:
    for num in row:
        print(num,end=" ")
    print()
