def is_weekend(day):
    return day in {6, 7}


def get_discount(amount):
    if amount >= 5000:
        return 0.1 * amount
    elif amount >= 1000:
        return 0.05 * amount
    return 0


def describe_number(n):
    parity = "четное" if n % 2 == 0 else "нечетное"
    digits = len(str(abs(n)))
    digit_words = ["однозначное", "двузначное", "трехзначное"]
    return f"{parity} {digit_words[digits - 1]} число"


def convert_to_meters(unitNumber, lengthInUnits):
    conversions = {
        1: 0.1,
        2: 1000,
        3: 1,
        4: 0.001,
        5: 0.01
    }
    return lengthInUnits * conversions.get(unitNumber, 1)


def describe_age(age):
    units = age % 10
    tens = age // 10
    
    word_map = {
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто",
        10: "сто"
    }
    
    unit_map = {
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять"
    }
    
    if age == 20:
        return "двадцать лет"
    
    if units == 0:
        age_word = word_map[tens]
    else:
        age_word = f"{word_map[tens]} {unit_map[units]}"
    
    if units == 1 and tens != 1:
        suffix = "год"
    elif 2 <= units <= 4 and tens != 1:
        suffix = "года"
    else:
        suffix = "лет"
    
    return f"{age_word} {suffix}"