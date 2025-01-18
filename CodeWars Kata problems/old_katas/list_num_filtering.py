def filter_list(l):
    'return a new list with the strings filtered out'
    numbers = []
    for nums in l:
        if type(nums) == int:
            numbers.append(nums)
    
    return numbers
            