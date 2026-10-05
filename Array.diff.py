def array_diff(a, b):
    ans_array = []
    for digit in a:
        if digit in b:
            continue
        else:
            ans_array.append(digit)
    return ans_array
