from datetime import date
#This snippet of code determines if Susan can buy a alcoholic drink from bartender.

#example string variable
name = input("What is name on license?:")
print(name)

#example number variables
drink_cost = 10.00
tax = drink_cost * .08
total_drink_cost = drink_cost + tax
money_in_Purse = 20.00
print(total_drink_cost)

#example boolean variable
is_pregnant = input("Ask Susan if she is pregnant True or False:")
print(is_pregnant)

#determine age based on today's date

#define function
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
#Other conditions that could stop her from drinking

