
def collatz(number):
    # if num is even, it should print number // 2 and return while return 3 * num + 1 if odd
     if number % 2 == 0:
          return number // 2
     else:
          return 3 * number + 1

try:
     num = input("Enter your number: ")
     print(collatz(num))
except:
     print("wrong input! praEnter an interger")
    