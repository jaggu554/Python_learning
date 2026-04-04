nums={1,2,3,4} # to create a set

print(nums)
print(type(nums))
nums1=set([1,2,3,4,5,5])
print(type(nums1))
print(nums1)


nums.add(5) # adding to element to the set

nums.remove(2) #removing element to the set .throw error

nums.discard(10) #safe removal. No Error even value is present

if 5 in nums:
    print("Yes")

l=[1,1,2,2,3,3,4,4,5,5]
unique=list(set(l))
print(unique)

a={1,2,3}
b={2,3,4}

print("a or b",a|b) #removes duplicates from the duplicates and show combined set
print("a and b ",a&b) # only intersection elements it will show

print(a-b) # removes intersection elements show remaining in a

# Exercise 2 — Common Elements
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

print(set(a) & set(b))


#  Exercise 3 — Unique Words

text = "I love AI and AI loves me"

a=set(text.split())
print(a)


#  Exercise 4 — Check Subset

a = {1, 2}
b = {1, 2, 3, 4}

print("A is subset of b ",a.issubset(b))


# Exercise 7 — AI Style: Vocabulary Builder

sentences = [
    "I love AI",
    "AI is powerful",
    "I love coding"
]

result=set()
for sent in sentences:
    for i in sent.split():
        result.add(i)

print(result)

#  Exercise 8 — Remove Duplicates but Keep Order (Important)

nums = [1, 2, 2, 3, 1, 4]
result=set()
for i in nums:
    if i not in result:
        result.add(i)

print(result)

