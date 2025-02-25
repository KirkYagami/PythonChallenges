# Closest number to Zero

def closest_to_zero(numbers):
    return min(numbers, key=lambda x: (abs(x), -x))


lst = [-800, -6, 2, 8, 7, 1, 1, 60]

print(closest_to_zero(lst))

# Try to solve this by applying map function