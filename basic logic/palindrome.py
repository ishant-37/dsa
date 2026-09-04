''' num = int(input("Enter a number:")) '''
n = 1234
num = n
result = 0

while num > 0:
    last_digit = num % 10
    result = (result*10) + last_digit
    num = num // 10

print ("Number:",n)

if  n == result  :
        print("is a palindrome.")
else :
        print("is not a palindrome")