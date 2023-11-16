print("Welcome to the tip calculator.")
total_sum = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_count = int(input("How many people to split the bill? "))
tip = (total_sum * ((percentage / 100) + 1)) / people_count
print(f'Each person should pay: ${round(tip, 2)}')
