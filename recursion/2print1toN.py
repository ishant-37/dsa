x = int(input("Enter a number:"))
n = int(input("Enter frequency:"))
def num(x, n):
    if x > n:
        return
    print(x)
    num(x+1, n)

num(x,n)
