#region My files & library
import MyFiles.riazmand_text as t
from MyFiles.riazmand_tools import my_print, my_input, clear_terminal, loading_animation

import os, hashlib
#endregion My files & library

#region Main

def save_user(user_type):
    username, password = getting_user_information()
    # Check if username already exists
    with open("MyFiles/user_db/user_db.txt", "a+") as file:
        file.seek(0)
        for line in file:
            existing_username = line.strip().split(":")[0]
            if check_hash(existing_username, username):
                my_print(t.print_username_exists.copy(), 1)
                loading_animation(3, "", "", 3)
                return False
    # Check if password is at least 8 characters long
    if len(password) < 8:
        my_print(t.print_pass_len_error.copy(), 1)
        loading_animation(3, "", "", 3)
        return False
    # Save user in one line
    with open("MyFiles/user_db/user_db.txt", "a+") as file:
        hashed_username = hash_maker(username)
        hashed_password = hash_maker(password)
        encrypted_user_type = encrypter(user_type)
        file.write(f"{hashed_username}:{hashed_password}:{encrypted_user_type}\n")
        my_print(t.print_save_user.copy(), 5)
    return username

def login_user():
    username, password = getting_user_information()
    if not os.path.isfile('MyFiles/user_db/user_db.txt'):
        return False, username
    else:    
        with open("MyFiles/user_db/user_db.txt", "r") as file:
            for line in file:
                existing_username, existing_password, existing_user_type = line.strip().split(":")
                if check_hash(existing_username, username) and check_hash(existing_password, password):
                    user_type = unencrypter(existing_user_type)
                    return user_type, username
        return False, username

def folder_checker():
    if not os.path.isdir('MyFiles/user_db/'):
        os.makedirs('MyFiles/user_db/')

def getting_user_information():
    clear_terminal()

    username = my_input(t.input_username.copy())
    password = my_input(t.input_password.copy())

    return username, password

#region hash

def check_hash(hash, input):
    return hashlib.sha256(input.encode()).hexdigest() == hash

def hash_maker(input):
    hash_object = hashlib.sha256(input.encode())
    hash_value = hash_object.hexdigest()
    return hash_value

def encrypter(input):
    encrypted = ""
    for i in input:
        encrypted += chr(ord(i) + 5)
    return encrypted

def unencrypter(input):
    unencrypted = ""
    for i in input:
        unencrypted += chr(ord(i) - 5)
    return unencrypted
#endregion hash
#endregion Main

folder_checker()