n = 123
num = n
total = 0
nod = 0

while num > 0:
    nod+=1
    num = num//10
print(nod)

while num > 0:
    ld = num % 10
    total = total + (ld**nod)
    num = num//10
print(total)