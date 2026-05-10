nums = [1, 2, 3, 2, 4, 5, 1, 6,1]
original=set()

def remove_duplicates(nums):
    duplicates_list=set()
    for i in nums:
        if i  in original:
            duplicates_list.add(i)
        else:
            original.add(i)

    return duplicates_list

print(remove_duplicates(nums))



