#CHALLENGE D

'''
temps = [-5, -2, 0, 0, 1, 4, 5, 3, 6, 5, 6, 7, 10, 13, 12, 11, 11, 8, 10, 7, 4, 0, -6, -3]

highForToday = temps[0]
lowForToday = temps[0]

for i in range(len(temps)):

    if temps[i] > highForToday:
        highForToday = temps[i]
    
    elif temps[i] < lowForToday:
        lowForToday = temps[i]


print(f"Today's high is {highForToday}! ")

print()

print(f"Today's low is {lowForToday}! ")
'''

#CHALLENGE E

'''
q1 = "What is Samyak's favourite video game? " 
q2 = "What is Samyak's favourite food? "
q3 = "What is the first name of the first african american president of the USA? "
q4 = "What is the first name of Bart Simpson's father? "
q5 = "What is Intel's most famous rival? "

a1 = "Valorant"
a2 = "Poutine"
a3 = "Barack"
a4 = "Homer"
a5 = "AMD"

questions = [q1, q2, q3, q4, q5]
answers = [a1, a2, a3, a4, a5]

userGuesses = []

for i in range(len(questions)):
    currentUserGuess = input(questions[i])
    print()
    userGuesses.append(currentUserGuess)

scoreSoFar = 0

for i in range(len(questions)):
    if userGuesses[i] == answers[i]:
        print(f"The question was {questions[i]} ")
        print()
        print(f"Your answer was {userGuesses[i]}. ")
        print()
        print("Your answer was correct! ")
        print()

        scoreSoFar += 1

    elif userGuesses[i] != answers[1]:
        print(f"The question was {questions[i]} ")
        print()
        print(f"Your answer was {userGuesses[i]}. ")
        print()
        print("Your answer was incorrect. ")
        print()

print("")

print(f"You got {scoreSoFar} questions correct.")
'''

#CHALLENGE F


raceTimes = [453, 450, 420, 492, 509, 444, 460, 530, 499]

places = ["", " second", " third", " fourth", " fifth", " sixth", " seventh", " eighth", " ninth"]

#fastestTime = raceTimes[0]

for i in range(len(raceTimes)):

    fastestTime = raceTimes[0]
    
    for j in range(len(raceTimes)):

        if fastestTime > raceTimes[j]:
            fastestTime = raceTimes[j]

    print(f"The{places[i]} fastest time is {fastestTime}. ")

    print()

    raceTimes.remove(fastestTime)
