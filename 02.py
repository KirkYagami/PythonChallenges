# swap numbers

def swap_tuple(x, y):


    x, y = y, x
    return x, y

a = 10
b = 5



def swap_with_arith(x, y):
    x = x+y
    y = x-y
    x = x-y

    return x,y

print(swap_tuple(a,b))
print(swap_with_arith(a,b))
