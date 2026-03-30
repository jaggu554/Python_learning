def greet():
    return "Hello world!"

print(greet())


def greet(name):
    return "Hello "+name


print(greet("Jagadeesh"))

def add(a,b):
    return a+b

print(add(10,9))

def multiply(a,b,c):
    return a*b*c

print(multiply(5,6,7))

def greet(name="surendra"):
    return name+" King"

print(greet("Rajesh "))

print(greet())

def helloworld():
    return "Welcome to the jungle"

print(helloworld())

def find_prime(n):
    for i in range(2,n):
        if n%i==0 :
            return "not prime"
    else:
        return "prime"
    
print(find_prime(11))


def sum_list(nums):
    sum=0
    for i in nums:
        sum+=i
    return sum

print(sum_list([1,2,3,4]))

# count even numbers

def even_count(nums):
    count=0
    for i in nums:
        if i%2==0:
            count+=1

    return count

print(even_count([1,2,3,4,5,6,6,88]))

# maximum in the list

def find_largest(nums):
    largest=0
    for i in nums:
        if i>largest:
            largest=i
    return largest

print(find_largest([1,2,3,4,5,6,6,88]))


def reverse_list(nums):
    result=[]
    for i in range(len(nums)-1,-1,-1):
        result.append(nums[i])
    return result

print(reverse_list([1,2,3,4,5,6,6,88]))


def remove_duplicates(nums):
    result=[]
    for x in nums:
        if x>=3 and x not in result:
            result.append(x)
    return result

print(remove_duplicates([1,1,22,2,22,3,4,5,6]))
