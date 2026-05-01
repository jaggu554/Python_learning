text="hello"

# text[0]="H" # error , becuase strings are immutable

print(text)

print(text[0])
print(text[::-1])

print(text[::])

for ch in text:
    print(ch)


print(text[1:]) #ello
print(text[2:]) #llo
print(text[::-3]) #oe

str="  Hello  ";
s=str.strip()
print(s)

print(str.lower().strip())
print(str.upper().strip())

print(text.replace('l','x'))
print(text)

text="I Love AI"
words=text.split()

sentence=" ".join(words)
print(sentence)


# reverse string
print(text[::-1])

def reverse_string(text):
    temp=""
    
    for i in range(len(text)-1,-1,-1):
        temp+=text[i]
    return "reverese String :",temp

print(reverse_string("hello"))


def count_vowels(n):
    count=0
    for i in n:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            count+=1
    return count

print(count_vowels("education"))

def is_palindrome(s):
    rev=""
    for i in range(len(s)-1,-1,-1):
        rev=rev+s[i]
    
    print("Reverse :",rev)
    if rev==s:
        return True
    else:
        return False

print(is_palindrome("madam"))

print("="*60)
def remove_spaces(s):
    words=s.split()
    return "".join(words)


print(remove_spaces("I love AI"))

print("="*60)
result={}
def first_unique(s):
    for i in s:
        if i in result:
            result[i]=result[i]+1
        else:
            result[i]=1
   
    for i in s:
        if result[i]==1:
            return i

print(first_unique("leetcode"))

print("="*60)

def char_frequency(s):
    res={}
    for i in s:
        if i in res:
            res[i]=res[i]+1
        else:
            res[i]=1
    
    return res

print(char_frequency("aabbc"))


def most_frequent_char(s):
    res={}
    maxValue=0
    for i in s:
        if i in res:
            res[i]=res[i]+1
            maxValue=max(maxValue,res[i]);
        else:
            res[i]=1

    for i in res:
        if res[i]==maxValue:
            return i

print(most_frequent_char("aabbccc"))


    
def clean_text(s):
    word=s.strip().split()
    result=" ".join(word)
    return result.lower()

print(clean_text("  Hello   AI   World  "));

