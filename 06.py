# # remove duplicates

# lst = [1,2,3,3,2,2,5,7]

# def remove_duplicates(nums):
#     return list(set(nums))

# print(remove_duplicates(lst))

# # Write a function that returns tuple(duplicates, uniques)

# lst = [1,2,3,3,2,2,5,7]
# def remove_duplicates_new(nums):
#     seen = set()
#     distinct = []
#     for num in nums:
#         if num not in seen:
#             seen.add(num)
#         else:
#             distinct.append(num)
#     return seen, distinct

# first put the item into distinct,if it is already there, put it to seen



lst = [1,2,3,3,2,2,5,7]
def remove_duplicates_new(nums):
    seen = set()
    distinct = []
    for num in nums:
        if num not in distinct:
            distinct.append(num)
        else:
            seen.add(num)
    return distinct, seen

print(remove_duplicates_new(lst))