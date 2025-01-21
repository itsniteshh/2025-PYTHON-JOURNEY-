def fake_bin(x):
    final = ""
    
    for nums in x:
        if int(nums) < 5:
            final += "0"
        else:
            final += "1"
    
    return final