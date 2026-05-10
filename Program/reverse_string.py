s="I love python"
def reverse_string(s):
    l=s.split()
    l=l[::-1]
    
    return " ".join(l)

print(reverse_string(s))