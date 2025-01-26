
def is_prime(num):
    """to check if the number is prime or not"""
    prime = []
    if num <= 1:
        return False
    
    for nums in range(1, num+1):
        if num % nums == 0:
            prime.append(nums)
    
    return len(prime) == 2

number = int(input("Enter a number: "))
print(is_prime(number))

