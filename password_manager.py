# Import module (pip install) for encrypting text
from cryptography.fernet import Fernet

# Function creates file 'key.key' in wb (write in byte) mode.
    # Function was called once and is commented out to avoid issues
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Call above function; run once and then comment out to avoid issues
# write_key()

# Function to load the above created "key.key" file. Opens, closes, returns key
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# Calls load_key function and adds the master password to the key
key = load_key()

# Stores key  a variable
fer = Fernet(key)

# Function that allows viewing instead of adding new text
    # 'r' is syntax for opening the file just for reading
    # rstrip() gets rid of the \n during reading
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

# Function that allows for adding new text
def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# Opens file with open() method. Appends with 'a' and creates file if it does 
    # not exist
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones?"
        "\nType 'view' or 'add' or enter 'q' to quit. ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. " )
        continue