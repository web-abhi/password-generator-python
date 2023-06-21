import random
letter = int(input("Enter the number of letters."))
no = int(input("Enter the number of numbers."))
misc = int(input("Enter the number of symbols."))
num = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
symbol = ["!","@","#","$","%","^","&","*","()"]
number = ["1","2","3","4","5","6","7","8","9"]

character = []
for char in range(1, letter+1):
    character+=random.choice(num)


for char in range(1, no+1):
    character+=random.choice(number)

    
for char in range(1, misc+1):
    character+=random.choice(symbol)

random.shuffle(character)

new_password = ""

for char in character:
    new_password+=char
print(new_password)