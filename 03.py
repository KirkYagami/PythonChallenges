# second largest

def second_largest(numbers):
    return sorted(set(numbers))[-2]


lst = [-800, -6, 2, 8, 7, 1, 1, 60]
print(second_largest(lst))

def second_highest(numbers):
    first, second  = float("-inf"), float("-inf")

    for num in numbers:
        if num > first:
            first, second = num, first
        elif first > num > second:
            second = num
    return second
    
lst = [-800, -6, 2, 8, 7, 1, 1, 60]
print(second_highest(lst))
