def add_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(num1, num2):
    return num1 - num2


def multiply_numbers(num1, num2):
    return num1 * num2


def divide_numbers(num1, num2):
    if not num2:
        raise ZeroDivisionError
    ans = num1 / num2
    return ans


def modulo_numbers(num1, num2):
    if not num2:
        raise ZeroDivisionError
    ans = num1 % num2
    return ans
