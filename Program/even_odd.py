nums=[1, 2, 3, 4, 5, 6, 7, 8]

def even(nums):
    even_list=[]
    for i in nums:
        if i%2==0:
            even_list.append(i)
    return even_list

print(even(nums))

even_numbers=[i for i in nums if i%2==0]

print(even_numbers)

