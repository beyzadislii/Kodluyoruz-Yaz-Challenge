x=input("Enter a text: ")
y=x.split()
a=True
for i in y:
    if y.count(i)>1:
     a=True
     print("You used duplication.") 
     break
    else:
       a=False
if a==False:
   print("You did not use duplication")


        
        