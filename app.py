users = {
    "alice": "1234",
    "bob": "password",
    "charlie": "qwerty"
}

def check_login(username, password):
    if username in users:
        if users[username] == password:
            print("Login successful")
            return
    print("Login failed")

def main():
    user = input("Username: ")
    pwd = input("Password: ")
    check_login(user, pwd)

main()
