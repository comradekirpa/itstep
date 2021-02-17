def print_num(x, y):
    if operation == '+':
        return x + y
    else:
        return 'Entre right symbol'


# пока истина цикл выполняется
while True:
    # истина если ввод а и b числа. цикл работает
    try:
        a = float(input('a = '))
        operation = input('symbol = ')
        b = float(input('b = '))
        print(print_num(a, b))
        print("Sasha")
    except ValueError:
        print('EXIT')
        break