def better_than_average(class_points, your_points):
    # Your code here
    class_total = 0
    count = 0
    for points in class_points:
        class_total += points
        count += 1
    
    class_avg = class_total / count
        
    if your_points > class_avg:
        return True
    else:
        return False
    
    
