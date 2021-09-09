import random
word_list, display = ["strawberry", "shampoo", "shower", "stapler", "apple", "theatre"], []
word = random.choice(word_list)
life = 6

#TODO-1: - fill the list "display" with blanks
for _ in word:
    display.append("_")
print(display)

tock = 0
#TODO-3: Check if you've won
while life > 0:
    if "_" not in display:
        print("You're the man now, Dog!!!")
        break
#TODO-4: If guessed letter is in the word, edit the "display" list
    else:
        letter = input("Guess a letter:\n").lower()
        if letter in word:
            tock = 0
            for s in word:
                if letter == s:  # if letter equals the string in the solve word
                    display.pop(tock)
                    display.insert(tock, s)
                    tock += 1
                else:
                    tock += 1
                    pass
            tock = 0
#TODO-5: Bad guess = Reduce lives by 1
        else:
            life -= 1
            if life == 0:
                print("Lost")
                break
            else:
             print(f"Uh oh! {life} lives remaining!")
        print(f"{display}")
