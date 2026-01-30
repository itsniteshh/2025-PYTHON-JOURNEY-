def find_multiples(integer, limit):
    final = []
    for nums in range(integer, limit+ 1):
        if nums % integer == 0:
            final.append(nums)
    
    return final