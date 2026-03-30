import math
#sum of digits

def sum_digits(n):
    sum=0
    while(n>0):
        digit=n%10;
        sum+=digit
        n=n//10
    return sum

print(sum_digits(1234))


# count vowels

def count_vowels(str):
    vowel_count=0
    for i in str:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            vowel_count+=1
    return vowel_count

print(count_vowels("hello worlds"))


# checking armstrong number

def is_armstrong(n):
    pow=len(n)
    print("pow ",pow)
    m=int(n)
    n=int(n)
    num=0
    while(n>0):
        digit=n%10
        num+=math.pow(digit,pow)
        n=n//10
    return m==num

print(is_armstrong("154"))

# factorial 
def factorial(n):
    a=0
    b=1
    l=[0,1]
    c=0
    for i in range(n-2):
        
        c=a+b
        l.append(c)
        a=b
        b=c
    return l
    

print(factorial(6))

# flatten the list

def flatten(nums):
    result=[]
    for x in nums:
        if type(x)==list:
            for i in x:
                result.append(i)
        else:
            result.append(x)
    return result

print(flatten([1, [2, 3], [4, 5], 6]))


# custom map function

def apply_function(nums,func):
    result=[]
    for x in nums:
        result.append(func(x))
    
    return result

def square(x):
    return x*x

print(apply_function([1,2,3,4,5,6],square))