def find_it(seq):
    for num in seq:
        new_no = seq.count(num)
        if new_no % 2 == 0:
            pass
        else:
            return num
    