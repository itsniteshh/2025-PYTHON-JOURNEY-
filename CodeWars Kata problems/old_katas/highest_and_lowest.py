def high_and_low(numbers):
    
    n = numbers.split()
    max_num = int(n[0])
    min_num = int(n[0])
    for numb in n:
        new_num = int(numb)
        if new_num > max_num:
            max_num = new_num
        
        if new_num < min_num:
            min_num = new_num
    
    return f"{max_num} {min_num}"

