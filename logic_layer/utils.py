def location_to_int(location_string):
    a, b = location_string.split('..')
    a_num = int(a)
    b_num = int(b)

    if a_num > 0 and b_num > 0:
        return a_num, b_num
    else:
        raise Exception


def calculate_frequencies(list_of_dicts):
    total_count = {}
    freq = {}
    total = len(list_of_dicts)

    # Count the items in the list
    for item in list_of_dicts:
        for k in item.keys():
            if k in total_count:
                total_count[k] += 1
            else:
                total_count[k] = 1

    # Calculate the frequencies
    for k, v in total_count.items():
        freq[k] = (v)/total

    return freq
