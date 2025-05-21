import getpass
import hashlib

# Pre-hashed passwords using SHA-256
# Example: hashlib.sha256("1234".encode()).hexdigest()
users = {
    "alice": hashlib.sha256("1234".encode()).hexdigest(),
    "bob": hashlib.sha256("password".encode()).hexdigest(),
    "charlie": hashlib.sha256("qwerty".encode()).hexdigest()
}

def hash_password(password):
    """Returns the SHA-256 hash of the given password."""
    return hashlib.sha256(password.encode()).hexdigest()

def check_login(username, password):
    """Checks if the username and hashed password match."""
    username = username.lower()
    if username in users:
        if users[username] == hash_password(password):
            return True
    return False

def main():
    max_attempts = 3
    for attempt in range(max_attempts):
        user = input("Username: ").strip()
        pwd = getpass.getpass("Password: ").strip()
        if check_login(user, pwd):
            print("✅ Login successful")
            return
        else:
            print(f"❌ Login failed. Attempts remain
