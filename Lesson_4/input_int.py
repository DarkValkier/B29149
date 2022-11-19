def input_int(message):
    while True:
        try:
            result = int(input(message))
        except ValueError:
            print('Некорректное значение! \nПопробуйте ещё раз.')
        except Exception as error:
            print(f'Что-то пошло не так: {type(error)} {error}')
        else:
            return result


a = input_int('Введите первое число:')
b = input_int('Введите второе число:')

print(f'{a} + {b} = {a+b}')