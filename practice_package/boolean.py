def check_between_numbers(A, B, C):
    return (A < B < C) or (C < B < A)


def check_odd_three(number):
    return (abs(number) >= 100 and abs(number) <= 999) and number % 2 != 0


def check_unique_digits(number):
    if 100 <= abs(number) <= 999:
        return len(set(str(abs(number)))) == 3
    return False


def check_palindrome_number(number):
    s = str(abs(number))
    return s == s[::-1]


def check_ascending_digits(number):
    if 100 <= abs(number) <= 999:
        num_str = str(abs(number))
        return num_str in '123456789'
    return False