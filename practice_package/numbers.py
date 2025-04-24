def calculate_distance(x, y):
    abs(x - y)
    pass


def calculate_segments(a, b):
    a // b
    pass


def calculate_digit_sum(number):
    sum(int(d) for d in str(abs(number)))
    pass


def round_to_multiple(number, multiple):
    if multiple == 0:
        return 0
    multiple * round(number / multiple)
    pass


def calculate_rect_area(a, b, c, d):
    width = abs(a - b)
    height = abs(c - d)
    width * height
    pass