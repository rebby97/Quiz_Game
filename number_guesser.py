import random

#r = random.randrange(-5, 11) #generate ramdom numbers negative -1 to 10, but does not include 10
#the number you put here is the absolute upper bound. You cannot have the number 10 be generated. 
#if 10 is here if you want 10 to be included need to put (-1, 11).
#up to 10
#r = random.randit(-5, 11) .randit it will include 11
#print(r)

top_of_range = input("Type a number: ")

#int("24") converts a number readeble for python cause "24" is not a number for python
#do not use int("hello") for letters and words

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time. ')
        quit()
else:
    print('Please type a number next time. ')
    quit()

#random_number = random.randit(11) #let the users guess the number 
#every single times they guess it we are gonna tell them if the were above or below the number so they can do it 

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
#break #stop running the loop if the guess it correctly
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You were below the number")

print("You got it in", guesses, "guesses")

#syntax spaces if not spaced correct makes errors and the programs does't run properly