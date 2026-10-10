def func(x, n):
    if n==0:
        return
    print(x)
    func(x,n -1)

func(15,4)

def newFunc(x, n):
    for i in range (n):
        print(x)
newFunc(14,5)