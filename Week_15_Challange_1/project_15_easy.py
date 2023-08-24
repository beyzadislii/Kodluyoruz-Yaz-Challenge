red=5
green=4
blue=3
first=1
second=1
third=1
fourth=1
fifth=1
sixth=1
seventh=1
eighth=1
for i in range(red+green+blue):#12!
    first=first*(i+1)
for i in range(red+green+blue-2):#10!
    second=second*(i+1)
for i in range(blue):#3!
    third=third*(i+1)
for i in range(blue-2):#1!
    fourth=fourth*(i+1)
for i in range(green):#4!
    fifth=fifth*(i+1)
for i in range(green-2):#2!
    sixth=sixth*(i+1)
for i in range(red):#5!
    seventh=seventh*(i+1)
for i in range(red-2):#3!
    eighth=eighth*(i+1)
red_chance=(seventh/eighth)*100
blue_chance=(third/fourth)*100
green_chance=(fifth/sixth)*100
general_chance=first/second
print(f"Red chance is: {red_chance/general_chance}")
print(f"Blue chance is: {blue_chance/general_chance}")
print(f"Green chance is: {green_chance/general_chance}")