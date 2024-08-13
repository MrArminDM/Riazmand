#region My files & library
import MyFiles.riazmand_text as t
from MyFiles.riazmand_doc_maker import logger
from MyFiles.riazmand_mail_center import crash_mail, close_mail

import hashlib, string, time
from sys import exit, stdout            #for system-related functions
from os import system                   #for system-related functions
from arabic_reshaper import reshape     #for handling Persian text
from bidi.algorithm import get_display  #for handling Persian text
#endregion My files & library

#region global
language = ""            #to store language mode
#endregion global
#region Main
#region Password
#region Hashed password
Hash_WRITER_PASSWORD = "3be5f347c696d1951babdbefe1937ff8242c67098dce12bef6c043fabe1bf41d"
Hash_ADMIN_PASSWORD = "d3e9c1f1b3efad083d0236bc8b3daaf4a0e1912e4220625d2a100b0bb4863928"
Hash_ROOT_PASSWORD = "079fcd778dc520103b239900a13547167153d1452297f1287437f9263e1b14a7"
#endregion Hashed password
#region Password checker

def check_password(user_type, input_password):
    if user_type == "writer":
        stored_password = Hash_WRITER_PASSWORD
    elif user_type == "admin":
        stored_password = Hash_ADMIN_PASSWORD
    elif user_type == "root":
        stored_password = Hash_ROOT_PASSWORD

    return hashlib.sha256(input_password.encode()).hexdigest() == stored_password
#endregion Password checker
#endregion Password
#region Tool
def clear_terminal():
    system('cls')

    print("\033[01;36m"'''
   █▀▀▀█ ▀ █▀▀▀█ ▀▀▀▀▀█ █▀▄ ▄▀█ █▀▀▀█ █▀▄   █ █▀▀▀▄
   █▄▄▄█ █ █▄▄▄█    ▄▀  █  ▀  █ █▄▄▄█ █  █  █ █    █
   █▀▄   █ █   █  ▄▀    █     █ █   █ █  █  █ █    █
   █  ▀▄ █ █   █ █▄▄▄▄▄ █     █ █   █ █   ▀▄█ █▄▄▄▀
''')

def my_print(text, color):  #to print text with optional color and language support
    final_text = ""
    if language == "En":
        final_text = text[1]
    else:
        reshaped_text = reshape(text[0])  # In fact with these libraries we can print Persian (fa) in terminal, but I don't know why they aren't working.
        converted = get_display(reshaped_text)  #Every website or videos do like this. I think I have library bug!!!
        final_text = converted

    print(f"\033[01;3{color}m" + final_text)

def my_print_fa(text, color):
    reshaped_text = reshape(text)  # In fact with these libraries we can print Persian (fa) in terminal, but I don't know why they aren't working.
    converted = get_display(reshaped_text)  #Every website or videos do like this. I think I have library bug!!!
    final_text = converted
    
    print(f"\033[01;3{color}m" + final_text)
    
def my_input(title):  #to prompt the user for input with optional title and language support
    if title != "":  my_print(title, 6)
    return input(">>> ")

def my_exit():
    clear_terminal()
    logger(language, t.log_exit.copy())
    my_print(t.print_email, 3)
    before_exit(close_mail())
    exit()

def crasher(erorr):
    clear_terminal()
    logger(language, t.log_crash.copy())
    my_print(t.print_crash.copy(), 1)
    before_exit(crash_mail(erorr))
    exit()

def before_exit(answer):
    if answer:
        logger(language, t.print_exit_true.copy())
        my_print(t.print_exit_true.copy(), 2)
    else:
        logger(language, t.print_exit_false.copy())
        my_print(t.print_exit_false.copy(), 1)

def loading_animation(duration, loading, done, max_dots):
    end_time = time.time() + duration
    animation = "."
    print("\033[01;31m", end='')
    while time.time() < end_time:
        for i in range(max_dots + 1):
            stdout.write("\r" + loading + animation * i)
            stdout.flush()
            time.sleep(duration/max_dots)
            if time.time() >= end_time: break

    print(f"\r{done}                    ")
#endregion Tool
#region Setting

def select_language():  ##to prompt the user to select their preferred language
    global language
    clear_terminal()
    my_print(t.print_select_language.copy(), 3)
    selection = my_input(t.input_select_language.copy())
    if selection in ["1", "Fa", "فارسی"]:
        language = "Fa"
    elif selection in ["2", "En", "English"]:
        language = "En"
    else:
        my_print(t.print_select_language_erorr.copy(), "1")
        loading_animation(3, "", "", 3)
        language = "Fa"
    logger(language, t.log_language.copy())
    return language
#endregion setting
#endregion Main
