day_of_week = input("What day of the week is it today? ").lower()

print(day_of_week == "monday")

if day_of_week == "monday":
    print("Have a great start to your week!")
elif day_of_week == "tuesday":
    print("It's Tuesday.")
elif day_of_week == "saturday" or day_of_week == "sunday":
    print("Have a good weekend!")
else:
    print("Full speed ahead!")
