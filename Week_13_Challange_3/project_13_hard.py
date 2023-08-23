student=30
selected_student=4
first=1
second=1
for i in range(30):
    first=first*(i+1)
for i in range(30-4):
    second=second*(i+1)
chance=first/second
print(f"4 people out of 30, selected in different {chance} ways")
