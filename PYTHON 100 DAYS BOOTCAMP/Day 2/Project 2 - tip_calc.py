total_bill = float(input("Enter your total bill: "))
tip = int(input("Enter your total tip %: "))
person = int(input("Enter total number of person: "))

total_with_tip = total_bill + (total_bill * tip)/100
final_total = total_with_tip / person


print(f"The per person contro share is: {final_total}")