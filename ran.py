import random
word = random.randint(0,50)
user = None
while user != word:
    try:
        user = int(input("Guess a Number: "))
        if user > word:
            print("Too High")
        elif user < word:
            print("Too Low")
    except ValueError:
        print("ErRER")
print("correct")