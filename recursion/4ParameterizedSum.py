def add(sum, i, n):
    if i>n:
        print(sum)
        return
    add(sum+i,i+1,n)
add(0,1,4)