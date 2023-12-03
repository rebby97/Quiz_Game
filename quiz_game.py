print("Welcome to my Computer quiz")

playing = input("Do you want to play? ") #add space to make sure the users start typing one space after the question mark

#text = "Quiz IS Great"
#print(text.lower()) 
#.lower() it will convert all to lower cases
#.upper() it will convert all to lower cases

if playing.lower() != "yes": 
    quit()

print("Okay! Let's play:)")
score = 0

answer = input("What does CPU stand for? ")#.lower() can also put it to the answer instead
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1 
else:
    print("Incorrect!")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphic processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!") #plus sign is a concatenation operator
#string because score is a number
print("You got " + str((score / 4) * 100) + "%.")
#((score/4) * 100) score /divided for number of questions  *multiplyied by 100 for %percentage 
#double parentesis to make sure the operation happens first, before we multiply by 100

#else statment comes after if statment only
#remember to use the appropriate spaces with the syntax ex:
# answer = input()
# if answer == ""
#     print() 4 spaces 











