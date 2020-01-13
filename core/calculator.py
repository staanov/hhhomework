from decorators import cache_decorator

@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    operations = ['+', '-', '/', '*', '**']
    if operation not in operations:
        print("Такой операции нет. Введите данные ещё раз. "
              "Удостоверьтесь, что выбран один из этих операторов: +, -, /, *, **")
        return None
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    elif operation == "**":
        return a**b


if __name__ == '__main__':
    while True:
        try:
            a = int(input('Введите первое число: '))
            break
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз")
            continue
    while True:
        try:
            b = int(input('Введите второе число: '))
            break
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз")
            continue
    operation = input('Введите операцию: ')

    print('Результат: ', calculator(a, b, operation))

