from datetime import date
def age_calculator(birthdate):
    today=date.today()
    age=today.year-birthdate.year
    return age

x=int(input("Enter your birthday:year"))
y=int(input("Enter your birthday:month"))
z=int(input("Enter your birthday:day"))
answer=age_calculator(date(x,y,z))
print(f"You are {answer} years old")