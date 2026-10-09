def find_it(seq):
    dif_num = set(seq)
    ans, max_odd = 0, 0
    for num in dif_num:
        counter = seq.count(num)
        if counter % 2 == 1 and counter > max_odd:
            max_odd = counter
            ans = num
    return ans
