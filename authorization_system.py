user = input("Do you want to (l)ogin or (s)ignup?:-- ").lower()

if user == "l":
    username = input("Enter your username:--")
    password = input("Enter your password:--")
    if username == "admin" and password == "1234":
        print("Welcome Admin")
    else:
        print("Invalid username or password")

elif user == "s":
    username = input("Enter your username:--")
    password = input("Enter your password:--")
    confirm_password = input("Confirm your password:--")
    if password == confirm_password:
        print("The account has been created")
    else:
        print("Signup failed: The passwords do not match")

else:
    print("Invalid option. Please choose (l)ogin or (s)ignup.")
