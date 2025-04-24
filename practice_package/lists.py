def square_odds(numbers):
    return [x**2 for x in numbers if x % 2 != 0]


def normalize_names(names):
    return [name.capitalize() for name in names]


def remove_invalid_emails(emails):
    valid = []
    for email in emails:
        if (email.count('@') == 1 and 
            len(email) >= 5 and 
            not email.startswith('@') and 
            not email.endswith('@')):
            valid.append(email)
    return valid


def filter_palindromes(words):
    return [word for word in words if word.lower() == word.lower()[::-1]]


def calculate_factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def find_common_prefix(strings):
    if not strings:
        return ""

    min_len = min(len(s) for s in strings)
    
    for i in range(min_len):

        char = strings[0][i]

        for s in strings[1:]:
            if s[i] != char:

                return strings[0][:i]
    
    return strings[0][:min_len]