from datetime import date
# This snippet of code determines if Susan can buy a alcoholic drink.
# Bartender asks relevant question that would prevent her from drinking.

# example string variable
name = input("What is name given to you?")
name_lcn = input("What is name on license?:").lower()
if name == name_lcn:
  print("Hi, " + name)
else:
  print("This is not your licence")

# define function/determine age based on today's date
def old_enough(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

birth_year =int(input("Birth year on her license(YYYY):"))
birth_month = int(input("Birth month on license 2 digit number:"))
birth_day = int(input("Birth day on license 2 digit number:"))
birth_date_license = date(birth_year, birth_month, birth_day)

age_today = old_enough(birth_date_license)

if age_today >=21:
    print(f"{age_today} is old enough!")
else:
    print(f"You are {age_today}, so too young!")
    
#example number variables
drink_cost = 10.00
tax = drink_cost * .08
total_drink_cost = drink_cost + tax
money_in_purse = float(input("How much money in your purse?:"))

if total_drink_cost < money_in_purse:
  print("You can afford your drink at $" + str(total_drink_cost))
else:
  print("Sorry not enough money.")
#example boolean variable
person_response = input("Ask yourself- Am I pregnant?(yes/no):")
is_pregnant = person_response in ["yes", "y", "true"]
if is_pregnant:
  print("Think about how drinking will hurt your baby!!")
else: 
  print("Think no problem-I will buy my drink now.")
