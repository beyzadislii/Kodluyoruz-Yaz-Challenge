array=[4,8,56,74,36,43,78,45,23]
y=len(array)
x=sorted(array)
if y%2==0:
    i=y/2
    print(f"Median is {(array[i]+array[i-1])/2}")
else:
   print(f"Median is {x[y//2]}")
