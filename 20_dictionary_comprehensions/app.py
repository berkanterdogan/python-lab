users = [
    (0, "Bob", "password"),
    (1, "Rolf", "1234"),
    (2, "Jose", "4321"),
    (3, "username", "mypass")
]

user_mapping = {user[1]: user for user in users}
print(user_mapping)
print(user_mapping["Bob"])

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

if username_input in user_mapping:
    _, username, password = user_mapping[username_input]

    if password_input == password:
        print("Your details are correct!")
    else:
        print("Your details are incorrect!")
else:
    print("Username is wrong!")
