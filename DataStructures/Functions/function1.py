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