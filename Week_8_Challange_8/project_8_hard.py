x=int(input("Enter a number: "))
digit=str(x)
result=0
for i in digit:
    number=int(i)**len(digit)
    result=result+number
if(x==result):
    print("This is an Armstrong number.")
else:
    print("This is not an Armstrong number.")
  