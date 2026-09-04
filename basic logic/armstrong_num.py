n = 153
num = n
total = 0
nod = 0

while num > 0:
    nod+=1
    num = num//10
print("Total digits are",nod)


num = n  # Value of num becomes 0 in the upper while loop, so reset it to n.

while num > 0:
    ld = num % 10
    total = total + (ld**nod)
    num = num//10
print("Addition is:",total)

if total == n :
    print("Hence, it is a armstrong number.")
else :
    print("It is not a armstrong number.")