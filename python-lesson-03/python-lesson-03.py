# savings calulator 
money_start = input("Enter how much money you currently have saved: ")
saving_years = input("Enter how many years you will be saving for: ")
interest_rate = input("Enter the current interest rate: ")

# calulate principal amount + simple interest earned
money_result = float(money_start) + (float(money_start) * int(saving_years) * float(interest_rate)/100)

# calulate principal amount + compund interest earned
money_result_compound = float(money_start) * (1 + float(interest_rate)/100) ** int(saving_years)

# print input questions and give result
print(f"Your savings after {saving_years} years: ${int(money_result_compound)}")
print(f"Will you be able to afford your holiday? {bool(money_result_compound>10000)}")
print(f"Will you be able to fly business class? {bool(money_result_compound>=20000)}")
