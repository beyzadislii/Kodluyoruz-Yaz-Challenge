array=["a","e","i","o","u"]
x=input("Enter a text: ")
result=0
for i in array:
 result= x.count(i)+result
print(f"The number of vowels in the text is {result}")
