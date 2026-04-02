person={
    "name":"Jagadeeswar reddy",
    "age":40
}
print("Name",person["name"])

print(person)

person["city"]="Benguluru"

print(person)

# print key values
for key in person:
    print(key)

# printing key values
for key,value in person.items():
    print(key ,value)

#  print names

if "name" in person:
    print("Exists")

#  datasets 
datasets=[
    {"text1":"one","label":1},
    {"text2":"two","label":2}
]


for key in datasets:
    for k,v in key.items():
        print(k,v)


d={"a":1,"b":2,"c":3}
for key,values in d.items():
    print(key,values)


a="hello"
d={}
for i in a:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1

print(d)

str="I love AI and AI loves me"
res={}
for i in str.split():
   
    if i in res:
        res[i]=res[i]+1
    else:
        res[i]=1

print(res)

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}


for key,value in d2.items():
    d1[key]=value

print(d1)


# Most Frequent Element

def most_frequent(nums):
    freq={}
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    max_count=0
    result=None

    for i in freq:
        if freq[i]>max_count:
            max_count=freq[i]
            result=i
    return result

print(most_frequent([1, 2, 2, 3, 3, 3, 4]))


def invert_dict(d):
    freq={}
    for key,value in d.items():
        if value not in freq:
            freq[value]=[]
        
        freq[value].append(key)
    return freq

print(invert_dict({"a": 1, "b": 2, "c": 1}))
