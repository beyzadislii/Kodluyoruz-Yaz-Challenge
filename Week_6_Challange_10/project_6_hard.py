x=int(input("Enter a number: "))
result=0
for i in range(x):
    if x%(i+1)==0:
        result=result+(i+1)
print(f"Sum of integer divisors of a number is {result}")