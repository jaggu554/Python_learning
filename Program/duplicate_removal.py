nums=[1, 2, 2, 3, 4, 1, 5, 3]

def duplicate_remove(nums):

    original=set()
    l=[]
    for i  in nums:
        if i not in original:
            original.add(i)
            l.append(i)
        
    return l

print(duplicate_remove(nums))




