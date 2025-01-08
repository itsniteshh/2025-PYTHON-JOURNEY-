def fake_bin(x):
    num = x.split()
    for nums in num:
        if nums < "5":
            num = 0
        else:
            num = 1
    
    return num

fake_bin("01011110001100111")

#not completed yet