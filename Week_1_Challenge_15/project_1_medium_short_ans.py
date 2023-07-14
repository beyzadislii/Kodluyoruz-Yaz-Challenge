text=input("Enter your text: ")
letters="qwertyuopasdfghjklizxcvbnm"
all_letters={letter:0 for letter in letters}

for char in text.lower():
    if char in letters:
        all_letters[char]+=1

sorted_values=sorted([(value,key)for (key,value) in all_letters.items()],reverse=True)

print(f"The most repeated letter and how many times it is repeated:  {max(sorted_values)}")
print("Here is the frequency of repetition of letters:")

for value,letter in sorted_values:
    print(f"{letter}:{value}")