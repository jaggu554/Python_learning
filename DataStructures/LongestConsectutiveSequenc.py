#Exercise 5 — Longest Consecutive Sequence (SET POWER)
import math


def longest_consecutive_sequence(nums):
    ss=set(nums)
    maxx=0
    for i in nums:
        if(i-1 not in ss):
            next=i
            length=0
            while(next in ss):
                next+=1
                length+=1
            maxx=max(maxx,length)
    return maxx

print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))

#Exercise 6 — Find Missing Numbers

numbers=[1,2,4,6]
n=6

def find_missing_numbers(numbers,n):
    result=[]
    set_numbers=set(numbers)
    for i in range(1,n+1):
        if i not in set_numbers:
            result.append(i)
    
    return result

print(find_missing_numbers([1,2,4,6],6))