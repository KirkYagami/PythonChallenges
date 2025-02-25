# Number of good pairs
# good pair => nums[i]== nums[j] and i<j


def count_good_pairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]==nums[j] and i<j:
                count+=1
    return count

# lst = [1,2,3,1,1,3]
# from collections import Counter
# count = Counter(lst)

# print(count)


print(count_good_pairs([1,2,3,1,1,3]))