def calculator(function):
    symbol = '+-/*'
    if not any(sign in function for sign in symbol):
        raise ValueError(f'Некорректно выражение, нет допустимых знаков ({symbol})')
    for sign in symbol:
        if sign in function:
            try:
                left, right = function.split(sign)
                left, right = int(left), int(right)
                return {
                    '+': lambda a, b: a + b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b,
                    '-': lambda a, b: a - b,
                }[sign](left, right)
            except (ValueError, TypeError):
                raise ValueError('Выражение должно содержать целые числа и один знак')
            except(ZeroDivisionError):
                raise ZeroDivisionError('На ноль не делят')


if __name__ == '__main__':
    print(calculator('10/10'))
