def location_to_int(location_string):
    a, b = location_string.split('..')
    a_num = int(a)
    b_num = int(b)
    
    if a_num > 0 and b_num > 0:
        return a_num, b_num
    else:
        raise Exception