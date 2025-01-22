def enough(cap, on, wait):
    """cap is the amount of people the bus can hold excluding the driver.
        on is the number of people on the bus excluding the driver.
        wait is the number of people waiting to get on to the bus excluding the driver."""
    # If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.
    total_on_bus = on + wait
    
    if total_on_bus <= cap:
        return 0
    else:
        return total_on_bus - cap