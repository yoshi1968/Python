# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)


# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)


counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

# 3.2.1.6 LAB: Essentials of the for loop - counting mississippily
import time

# Write a for loop that counts to five.
for i in range(1, 6)
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    print(i, "Mississippi")
    # Body of the loop - use: time.sleep(1)
    time.sleep(1)

# Write a print function with the final message.
print("Ready or not, here I come!")

# Lab
secret_word = input("enter a word: ")

while True:
    if secret_word == "chupacabra":
        break
    secret_word = input("enter a word: ")

print("You've successfully left the loop.")

# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")


# Prompt the user to enter a word
# and assign it to the user_word variable.

user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    # Complete the body of the for loop.
    if letter == "A":
        letter == ""
        continue
    elif letter == "E":
        letter == ""
        continue
    elif letter == "I":
        letter == ""
        continue
    elif letter == "O":
        letter == ""
        continue
    elif letter == "U":
        letter == ""
    else:
        letter += "\n"

print(user_word)    


# 3.2.1.14 LAB: Essentials of the while loop
blocks = int(input("Enter the number of blocks: "))
height = 0

while blocks > 0:
    if blocks < height:
        break
    height += 1
    blocks -= height    

print("The height of the pyramid:", height)
