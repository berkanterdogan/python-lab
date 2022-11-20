number = 7

while True:
    user_input = input("Would you like to play? (Y/n) ")
    if user_input == "n":
        break
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")


print("\n###############################\n")

friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
    print(f"{friend} is my friend.")

for friend in range(3):
    print(f"{friend} is my friend.")

print("\n###############################\n")

grades = (63, 85, 70, 91, 100, 100)
total = 0
grade_count = len(grades)

# We can use total = sum(grades) instead of this for loop
for grade in grades:
    total += grade

average = total / grade_count
print(f"The average of the grades is {average}")
