def find_common_elements(set1, set2):
    return set1.intersection(set2)


def is_superset(set_a, set_b):
    return set_b.issubset(set_a)


def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def count_unique_words(text):
    words = text.lower().split()
    return len(set(words))


def find_shared_items(*sets):
    if not sets:
        return set()
    shared = sets[0].copy()
    for s in sets[1:]:
        shared.intersection_update(s)
    return shared


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