def likes(names):
    
    count = len(names) - 2
    
    if len(names) == 0:
            new = "no one likes this"
            return new
    # your code here
    for name in names:
        
        if  len(names) >= 4:
            return f"{names[0]}, {names[1]} and {count} others like this"
                
        elif len(names) == 1:
            return f"{names[0]} likes this"
        
        elif len(names) == 2:
            return f"{names[0]} and {names[1]} like this"
        
        elif len(names) == 3:
            return f"{names[0]}, {names[1]} and {names[2]} like this"
        
