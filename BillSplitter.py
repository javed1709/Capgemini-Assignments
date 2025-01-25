def split_bill(total_amount, num_people, tip_percentage):
    tip_amount = total_amount * (tip_percentage / 100)

    total_with_tip = total_amount + tip_amount
    amount_per_person = total_with_tip / num_people
    
    return amount_per_person

total_amount = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people: "))
tip_percentage = float(input("Enter the tip percentage: "))

amount_per_person = split_bill(total_amount, num_people, tip_percentage)

print(f"Each person has to pay: {amount_per_person}")