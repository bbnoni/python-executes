#
#
# name = input("Enter your name: ")
#
# age = input("Enter your age: ")
#
# print(f"Hello, {name}!, You are {age} years old.")

# x = 10
# y = 5.5
# z = "Python"
#
# print(type(x))
# print(type(y))
# print(type(z))

# print(float(100))
# print(float(3.14))
# print(int(5.67))

# a = "5"
# b = 3
# print(a * b)

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# print(num1 + num2)


# age = int(input("Enter your age: "))
#
# if age < 18:
#     print("You are a minor")
# else:
#     print("You are an adult")

#number = int(input("Enter a number: "))
#
# if number%2 == 0:
#     print("Even")
# else:
#     print("Odd")

# password = input("Enter password: ")
#
# if password == "Python123":
#     print("Access Granted!")
# else:
#     print("Access Denied!")

# score = float(input("Enter your score: "))
#
# if score > 90 and score <= 100:
#     print(f"Your score is {score}. \ A")
# elif score >= 80 and score <= 89:
#     print("B")
# elif score >= 70 and score <= 79:
#     print("C")
# elif score >= 60 and score <= 69:
#     print("D")
# elif score < 60:
#     print("F")
# else:
#     print("Enter score 100 and below")


#loops

# for i in range(1, 11):
#     print(i)

# num = 2
#
# while num <= 20:
#     print(num)
#     num = num + 2

# num = 1
#
# while num <= 20:
#     print(num)
#     num += 2


#sum of numbers from 1 to N
#
# n = int(input("Enter a number: "))
# total = 0
# for i in range(1, n+1)
#     print(i)


# text = input("Enter a string: ")
#
# reversed_text = ""
# for char in text:
#     reversed_text = char + reversed_text
#
# print("Reversed:", reversed_text)


# def sum_numbers(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#     return total
# print(sum_numbers(5))


import random

def guessing_game():

    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number guessing game")
    print("I have chosen a number between 1 and 100. Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Your guess must be between 1 and 100!")

        except ValueError:
            print("Invalid Input")

if __name__ == "__main__":
    guessing_game()




