# using parameter

def fact(mul, i, n):

    if i > n:
        print(mul)
        return

    fact(mul * i, i + 1, n)


n = int(input("Enter number: "))

fact(1, 1, n)

# using function
def facto(n):
    if n == 0 or n == 1:
        return 1
    return n * facto(n-1)
print(facto(4))