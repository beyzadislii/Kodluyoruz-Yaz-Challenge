x=int(input("Enter a number: "))

if x==1:
    print(f"{x} is not a prime number")
if x<1:
    print("Invalid number!")
if x>1:
    for i in range(2,x):
        if (x%i==0):
            print(f"{x} is not prime number")
            break
    else:
        print(f"{x} is prime number")