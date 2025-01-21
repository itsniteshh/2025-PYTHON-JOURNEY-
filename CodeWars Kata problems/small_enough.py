def small_enough(array, limit):
    highest = 0
    
    for nums in array:
        if nums > highest:
            highest = nums
            
    return highest <= limit