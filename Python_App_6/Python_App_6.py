# This is Pyton Application 6
# The purpose of this Python application is to demonstrated what I have learned about for loops


print("Hello.  Welcome to Phyton Application 6.")

print()

print("Today we are going to demonstrate what we have leared about for loops.")

print()

# we are going to create a variable, 'values'
# we are going to use 'range' and provide a value of 5

print("Here is a list of numbers ranging from 0 - 4")

for values in range(5):
    
    # here we will print a range of #s from 0 - 4 (totalling 5 numbers)
    print(values)

print()
# we are going to reuse the variable, 'values' to now print values +1

print("Below is the list of numbers ranging from 1 - 5")


for values in range(5):
    print(values + 1)



print()


# when providing a range of numbers, Python will be inclusive of the first number, but exclusive of the next
# with the below statement of range(1,11) we should expect to see a list of numbers starting at 1 and ending at 10 (the last number before 11)
print("Now lets output a range of numbers between 0 and 10.")
for num in range(1,11):
    print(num)


print()
print("Now you provide two numbers and I will provide a list of numbers in between")

# we create a variable of 'x' for the first user input
x = int(input("Please enter your first number: "))

# we create a variable of 'y' for the next user input
y = int(input("Please provide your last number: "))

print()

# we use the two provide inputs and print a range of numbers, starting with the first number providing and listing the last number before the user inputed value
for num in range(x,y):
    print(num)

print("Remember that Pyton is inclusive ofthe first number in the range, but exclusive of your last number.")


print("Now lets experiment with the 'while' command in Python.")

print()

# we create variable called 'z' that we will add to

z = 0

# while z is less than 10 we will continue to print the number, adding 1 to it each time
while z < 10:
    print(z)
    z = z + 1

print()

print("Now let's try the 'import' command.")

import random

# the value for the variable secret will now be created and be an integer between 1 and 9
secret = random.randint(1,10)

# we now create the variable 'guess' and set it to have no value
guess = None

# we now create the variable 'attempts' so that we can count how many attempts it will take the user to determine the random number
attempts = 0


while guess != secret:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1


    # lets now include an if elif else inside the while loop

    if guess < secret:
        print("Too low!")

    elif guess > secret:
        print("Too high!")

    else:
        print(f"Correct! The number was {secret}.")
        print(f"It took you {attempts} to guess the secret number, {secret}.")


 # lets change the difficulty of the guessing game

    import random

# an easy version of the guessing game would be between 1 - 10
easy = 10

# a medium difficulty version of the guessing game would be between 1 - 50
medium = 50

# a hard versioon of the guessing game would be between 1 - 100
hard = 100

print("Please select your difficulty level: Easy , Medium , Hard ")
print("Please enter 1 for Easy")
print("Please enter 2 for Medium")
print("Please enter 3 for Hard")


# now we ask the user to pick a difficulty and assign it to a variable
difficulty = int(input("Please provide enter now: "))

# lets us an if elif else

if difficulty == 3:
    difficulty = hard

elif difficulty == 2:
    difficulty = medium

else:
    difficulty = easy

# the value for the variable secret will now be created and be an integer between 1 and 9
secret = random.randint(1,difficulty)

# we now create the variable 'guess' and set it to have no value
guess = None

# we now create the variable 'attempts' so that we can count how many attempts it will take the user to determine the random number
attempts = 0


while guess != secret:
    guess = int(input(f"Guess a number between 1 and {difficulty}: "))
    attempts += 1


    # lets now include an if elif else inside the while loop

    if guess < secret:
        print("Too low!")

    elif guess > secret:
        print("Too high!")

    else:
        print(f"Correct! The number was {secret}.")
        print(f"It took you {attempts} to guess the secret number, {secret}.")