def count_char_occurrences(text):
    counts = {}
    for char in text.lower():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    return counts


def merge_dicts(dict1, dict2, conflict_resolver):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] = conflict_resolver(key, result[key], value)
        else:
            result[key] = value
    return result


def invert_dictionary(original_dict):
    inverted = {}
    for key, value in original_dict.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key]
    return inverted


def dict_to_table(data_dict, columns):
    if not data_dict or not columns:
        return ""
    
    headers = [col.upper() for col in columns]
    rows = []
    for item in data_dict.values():
        row = [str(item.get(col, "N/A")) for col in columns]
        rows.append(row)
    
    col_widths = []
    for i in range(len(columns)):
        max_width = len(headers[i])
        for row in rows:
            if len(row[i]) > max_width:
                max_width = len(row[i])
        col_widths.append(max_width)
    
    header_line = "|" + "|".join(
        f" {headers[i].ljust(col_widths[i])} " 
        for i in range(len(columns))
    ) + "|"
    
    separator = "|" + "|".join(
        "-" * (col_widths[i] + 2) 
        for i in range(len(columns))
    ) + "|"
    
    row_lines = []
    for row in rows:
        row_line = "|" + "|".join(
            f" {row[i].ljust(col_widths[i])} " 
            for i in range(len(columns))
        ) + "|"
        row_lines.append(row_line)
    
    return "\n".join([header_line, separator] + row_lines)


def deep_update(base_dict, update_dict):
    result = base_dict.copy()
    for key, value in update_dict.items():
        if (key in result and 
            isinstance(result[key], dict) and 
            isinstance(value, dict)):
            result[key] = deep_update(result[key], value)
        else:
            result[key] = value
    return result