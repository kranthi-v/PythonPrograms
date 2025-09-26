a=input('enter the value of first variable: ')
b=input('enter the value of second variable: ')

print(f'original values: a={a}, b={b}')

temp = a
a = b
b = temp
print(f'Swap values: a={a}, b={b}')
