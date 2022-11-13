def input_int(message):
    result = int(input(message))

    return result


a = input_int('Введите первое число:')
b = input_int('Введите второе число:')

print(f'{a} + {b} = {a+b}')