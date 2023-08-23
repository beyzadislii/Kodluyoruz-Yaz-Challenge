x=int(input("Enter a number: "))
digit=str(x)
result=0
for i in digit:
    number=int(i)
    result=result+number
print(f"Sum of digits of the number is {result}")