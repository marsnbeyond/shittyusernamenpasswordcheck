print("Welcome to idiot login center!!!")
username = input("Enter a username: ")
password = input("Enter a password: ")

acc = [username, password]

print("\nNow we log in...")

attempts = 0
while attempts < 3:
    guest_user = input("Enter your username: ")
    guest_pass = input("Enter your password: ")
    if guest_user != username:
        attempts += 1
        print("Wrong!!!! Try again")
    if guest_pass != password:
        attempts += 1
        print("fucking idiot")
    else:
        print("congradulations!! bye")
        break
