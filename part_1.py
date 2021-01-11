def calculator(x, y, operation):
    if operation == '+':
        return x+y
    elif operation == '/':
        return x/y
    else:
        print('Not allowed')

print(calculator(1, 2, '+'))
print(calculator(1, 2, '/'))