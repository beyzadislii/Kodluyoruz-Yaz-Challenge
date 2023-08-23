array=[5,10,78,9,65,47,36,45,20,41,19]
result=0
for x in array:
    if x%2==0:
        result=result+x
print(f"Sum of even numbers:{result} ")