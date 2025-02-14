import random
word = random.randint(0,50)
user = 0
print(type(word))
while user != word:
    user = int(input("Guess a Number: "))
    print(type(user))
    if user > word:
        print("Too High")
    elif user < word:
        print("Too Low")
print("correct")
