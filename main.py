name = input('Введите своё имя:')


if len(name):
# if name == "":
    print(f"Привет, {name}!")
    print("Привет,", name, "!")
    print("Привет," + name + "!")
else:
    print("Вы ничего не ввели!")