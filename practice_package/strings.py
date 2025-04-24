def extract_file_name(full_file_name):
    return full_file_name.split('/')[-1].split('.')[0]


def encrypt_sentence(sentence):
    even_chars = sentence[1::2]
    odd_chars = sentence[0::2][::-1]
    return even_chars + odd_chars


def check_brackets(expression):
    balance = 0
    for i, char in enumerate(expression):
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return i + 1
    return 0 if balance == 0 else -1


def reverse_domain(domain):
    parts = domain.split('.')
    return '.'.join(reversed(parts))


def count_vowel_groups(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    word = word.lower()
    count = 0
    in_group = False
    
    for char in word:
        if char in vowels:
            if not in_group:
                count += 1
                in_group = True
        else:
            in_group = False
    return count