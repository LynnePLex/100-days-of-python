print("Bill Split Calculator")

bill = float(input("What is your bill?\n"))

tip = int(input("How much are you tipping? 10, 12, or 15?\n"))

people = int(input("How many peple were served?\n"))

tip_percentage = tip / 100

total_tip_amount = bill * tip_percentage

total_bill = bill + total_tip_amount

bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
