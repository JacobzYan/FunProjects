# Up to base 36


start_number = input("Enter number: ")
final_base = input("Enter Final Base: ")

highest_power = 0
while final_base ^ (highest_power < start_number):
    highest_power += 1
store_digits = [] * (highest_power + 1)
current_power = highest_power
while current_power >= 0:
    current_digit = start_number % (final_base ^ highest_power)
    start_number = start_number - current_digit * (final_base ^ highest_power)
