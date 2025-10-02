n = int(input("Enter number: "))
summ = 0
product = 1
while n>0:
    rem = n % 10
    summ = summ + rem
    product = product * rem
    n = n // 10
if summ == product:
    print(f'{n} is a spy number')
else:
    print(f'{n} is not a spy number')