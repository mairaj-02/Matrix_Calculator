import os
import hashlib

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def load_user_data(file_path):
    """Load user data from a file."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r') as file:
        return dict(line.strip().split(',') for line in file)

def save_user_data(file_path, user_data):
    """Save user data to a file."""
    with open(file_path, 'w') as file:
        for username, password in user_data.items():
            file.write(f"{username},{password}\n")

def login(file_path):
    """Handle user login and registration."""
    user_data = load_user_data(file_path)
    attempts = 3

    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")
        hashed_password = hash_password(password)

        if username in user_data:
            if user_data[username] == hashed_password:
                print("Login successful!")
                return True
            else:
                print("Incorrect password.")
                attempts -= 1
        else:
            print("Username not found. Registering new user...")
            user_data[username] = hashed_password
            save_user_data(file_path, user_data)
            print("Registration successful! You can now log in.")
            return True

    print("Too many failed attempts. Exiting.")
    return False
