#region My files & library
import MyFiles.riazmand_text as t
from MyFiles.riazmand_data_center import get_jokes, jock_saver, jock_loader
from MyFiles.riazmand_doc_maker import jock_to_file, logger, log_mode, doc_title, clear_doc
from MyFiles.riazmand_tools import my_print, my_print_fa, my_input, my_exit, clear_terminal, select_language, check_password, loading_animation, language
from MyFiles.riazmand_account import login_user, save_user

import random
#endregion My files & library

#region Global
joke_pack = []
number_of_all_jocks = 0
print_number_of_all_jocks = ""
user_type = "user"
logger_mode = "on"
language = ""
username = ""
#endregion Global
#region Main
#region Start

def start():
    clear_terminal()
    global language
    logger(language, t.log_start.copy())
    language = select_language()
    jock_reloader(language)
    welcome()
    account()

def welcome():  #to display a welcome message and prompt the user to select their user type
    clear_terminal()
    my_print(t.print_welcome.copy(), 2)
#endregion Start
#region Error

def error_confirm():  #to prompt the user for input with optional title and language support
    clear_terminal()
    logger(language, t.log_erorr.copy())
    my_print(t.print_value_erorr.copy(), 1)
    selection = my_input(t.input_mini_menu.copy())
    if selection == "1":
        menu_by_user_type()
    elif selection == "2":
        my_exit()
    else:
        error_confirm()
#endregion Error
#region Setting

def setting():
    global language
    clear_terminal()
    logger(language, t.log_setting.copy())
    selection = my_input(t.input_setting_menu.copy())
    if selection == "1":
        language = select_language()
        menu_by_user_type()
    elif selection == "2":
        logger_ctrl()
    elif selection == "3":
        menu_by_user_type()
    else:
        error_confirm()

def logger_ctrl():  #to enable or disable logging
    global logger_mode
    clear_terminal()
    logger(language, t.log_ctrl.copy())
    if logger_mode == "off":
        selection = my_input(t.input_log_off.copy())
        if selection == "1":
            logger_mode = "on"
            log_mode("on")
            logger(language, t.log_on.copy())
            logger_ctrl()
        elif selection == "2":
            menu_by_user_type()
        else:
            error_confirm()
    else:
        selection = my_input(t.input_log_on.copy())
        if selection == "1":
            logger_mode = "off"
            logger(language, t.log_off.copy())
            log_mode("off")
            logger_ctrl()
        elif selection == "2":
            menu_by_user_type()
        else:
            error_confirm()
#endregion setting
#region User

def account():
    clear_terminal()
    global user_type, username
    selection = my_input(t.input_account.copy())
    if selection in ["1", "login"]:
        back = login_user()
        information = back[0]
        if information == False:
            my_print(t.print_login_error.copy(), 1)
            loading_animation(3, "", "", 3)
            account()
        else:
            user_type = back[0]
            username = back[1]
    elif selection in ["2", "sing up"]:
        select_user_type()
        back = save_user(user_type)
        if back == False:
            account()
        else:
            username = back
    elif selection in ["3", "guest"]:
        username = ""
        user_type == "user"
    else:
        my_print(t.print_value_erorr.copy(), 1)
        loading_animation(3, "", "", 3)
        account()

    menu_by_user_type()

def select_user_type():  #to prompt the user to select their user type
    clear_terminal()
    global user_type
    selection = my_input(t.input_select_user_type.copy())
    if selection in ["1", "user"]:
        user_type = "user"
    elif selection in ["2", "writer"]:
        user_type = "writer"
    elif selection in ["3", "admin"]:
        user_type = "admin"
    elif selection in ["18109337301386070616", "root"]:
        user_type = "root"
    else:
        my_print(t.print_select_user_type_erorr.copy(), 1)
        loading_animation(3, "", "", 3)
        user_type = "user"
    
    logger(language, t.log_select_user_type.copy())
    confirm_user_access()

def confirm_user_access():  #to confirm the user's access level
    clear_terminal()
    global user_type
    password = ""
    if user_type != "user": password = my_input(t.input_password.copy())
    if user_type == "user" or check_password(user_type, password):
        logger(language, t.log_user_access_confirmrd.copy())
    else:
        my_print(t.print_password_erorr.copy(), 1)
        loading_animation(3, "", "", 3)
        logger(language, t.log_user_access_failed.copy())
        confirm_user_access()

def user_access_level():  #to confirm the user's access level
    clear_terminal()
    print(username)

    if user_type == "user":
        my_print(t.print_user_access_user.copy(), 5)
    elif user_type == "writer":
        my_print(t.print_user_access_auther.copy(), 5)
    elif user_type == "admin":
        my_print(t.print_user_access_admin.copy(), 5)
    elif user_type == "root":
        my_print(t.print_user_access_root.copy(), 5)

    logger(language, t.log_user_access_show.copy())
    print()
#endregion User
#region Menu
def menu_by_user_type():  #to display the menu options by ser type
    clear_terminal()
    logger(language, t.log_menu.copy())
    jock_reloader(language)
    user_access_level()

    my_print(t.menu_title.copy(), 3)
    my_print(t.menu_guide.copy(), 3)    #all user types
    my_print(t.menu_setting.copy(), 3)  #all user types
    my_print(t.menu_read.copy(), 3)     #all user types
    if user_type == "user":
        my_print(t.menu_about(4).copy(), 3)
        my_print(t.menu_exit(5).copy(), 3)
    elif user_type == "writer":
        my_print(t.menu_add.copy(), 3)
        my_print(t.menu_about(5).copy(), 3)
        my_print(t.menu_exit(6).copy(), 3)
    elif user_type == "admin":
        my_print(t.menu_add.copy(), 3)
        my_print(t.menu_del.copy(), 3)
        my_print(t.menu_about(6).copy(), 3)
        my_print(t.menu_exit(7).copy(), 3)
    elif user_type == "root":
        my_print(t.menu_add.copy(), 3)
        my_print(t.menu_del.copy(), 3)
        my_print(t.menu_export.copy(), 3)
        my_print(t.menu_about(7).copy(), 3)
        my_print(t.menu_exit(8).copy(), 3)

    selection = my_input("")
    if selection == "1":
        guide()
    elif selection == "2":
        setting()
    elif selection == "3":
        jock_reader(number_of_all_jocks)
    elif selection in ["4", "5"] and user_type == "user":
        if selection == "4": about()
        elif selection == "5": my_exit()
    elif selection in ["4", "5", "6"] and user_type == "writer":
        if selection == "4":   jock_adder()
        elif selection == "5": about()
        elif selection == "6": my_exit()
    elif selection in ["4", "5", "6", "7"] and user_type == "admin":
        if selection == "4":   jock_adder()
        elif selection == "5": jock_deleter(number_of_all_jocks)
        elif selection == "6": about()
        elif selection == "7": my_exit()
    elif selection in ["4", "5", "6", "7", "8"] and user_type == "root":    
        if selection == "4":   jock_adder()
        elif selection == "5": jock_deleter(number_of_all_jocks)
        elif selection == "6": jock_exporter(number_of_all_jocks)
        elif selection == "7": about()
        elif selection == "8": my_exit()
    else:
        error_confirm()
#endregion Menu
#region Jock
#region Loader

def jock_reloader(language):
    global joke_pack, number_of_all_jocks, print_number_of_all_jocks
    logger(language, t.log_jock_reload.copy())
    joke_pack = jock_loader(language)
    number_of_all_jocks = len(joke_pack)
    print_number_of_all_jocks = [f"تعداد کل جوک های موجود = {number_of_all_jocks}", f"Total number of available jokes = {number_of_all_jocks}"]
#endregion Loader
#region Main

def jock_reader(noaj):  #to allow the user to read jokes
    clear_terminal()
    logger(language, t.log_jock_reader.copy())
    selection = my_input(t.input_jock_reader_menu.copy())
    clear_terminal()
    if selection == "1":
        jock_list_to_print(noaj, 1, 1)
        logger(language, t.log_1_jock_showed.copy())
        end_of_work()
    elif selection == "2":
        my_print(print_number_of_all_jocks.copy(), 5)
        num = my_input(t.input_jock_num.copy())
        try:
            jock_list_to_print(noaj, num, 1)
            logger(language, t.log_some_jocks_showed.copy())
            end_of_work()
        except ValueError:
            error_confirm()
    elif selection == "3":
        jock_list_to_print(noaj, noaj, 1)
        logger(language, t.log_all_jocks_showed.copy())
        end_of_work()
    elif selection == "4":
        menu_by_user_type()
    else:
        error_confirm()

def jock_adder():  #to allow the user to add a joke
    clear_terminal()
    logger(language, t.log_jock_adder.copy())
    my_print(print_number_of_all_jocks.copy(), 5)
    value = my_input(t.input_your_joke.copy())
    clear_terminal()
    jock_saver(language, value, "append")
    my_print(t.print_jock_added.copy(), 2)
    logger(language, t.log_jock_added.copy())

    end_of_work()

def jock_deleter(noaj):  #to allow the user to delete a joke
    clear_terminal()
    logger(language, t.log_jock_deleter.copy())
    selection = my_input(t.input_jock_deleter_menu.copy())
    clear_terminal()
    if selection == "1":
        jock_list_to_print(noaj, noaj, 1)
        value = my_input(t.input_jock_deleter_m1.copy())
        try:
            logger(language, t.log_1_jock_deleted.copy())
            jock_saver(language, value, "remove")
            my_print(t.print_jock_deleted.copy(), 2)
            end_of_work()
        except ValueError:
            error_confirm()
    elif selection == "2":
        jock_list_to_print(noaj, noaj, 1)
        value = my_input(t.input_jock_deleter_m2.copy())
        try:
            logger(language, t.log_1_jock_deleted.copy())
            jock_saver(language, int(value) - 1, "pop")
            my_print(t.print_random_jock_deleted.copy(), 2)
            end_of_work()
        except IndexError:
            error_confirm()
    elif selection == "3":
        logger(language, t.log_1_random_jock_deleted)
        jock_saver(language, random.randint(0, noaj - 1), "pop")
        my_print(t.print_random_jock_deleted.copy(), 2)
        end_of_work()
    elif selection == "4":
        menu_by_user_type()
    else:
        error_confirm()

def jock_exporter(noaj):  #to allow the user to export jokes
    clear_terminal()
    logger(language, t.log_jock_exporter.copy())
    selection = my_input(t.input_jock_exporter.copy())
    if selection == "1":
        my_print(print_number_of_all_jocks.copy(), 5)
        num = my_input(t.input_jock_num.copy())
        try:
            logger(language, t.log_some_jocks_exported.copy())
            jock_list_to_print(noaj, num, 2)
            end_of_work()
        except IndexError:
            error_confirm()
    elif selection == "2":
        logger(language, t.log_all_jocks_exported.copy())
        jock_list_to_print(noaj, noaj, 2)
        end_of_work()
    elif selection == "3":
        menu_by_user_type()
    else:
        error_confirm()
#endregion Main
#region Tool

def jock_list_to_print(noaj, num, mode):  #to print a list of jokes
    if num == noaj:
        value = str(get_jokes(language, int(num), 2))
    else:
        value = str(get_jokes(language, int(num), 1))
    value = value.replace("[", "")
    value = value.replace("]", "")
    value = value.replace('"', '')
    value = value.split(', ')
    c = 0

    if mode == 2:
        if num == noaj:
            doc_title("All jocks", "jock")
        elif num == "1":
            doc_title("1 jock", "jock")
        else:
            doc_title(f"{num} jocks", "jock")
    
    for i in value:
        c += 1
        text = i.replace("'", "")
        if mode == 1:
            my_print_fa(f"{c}. {text}", 0)
        elif mode == 2:
            if num == noaj:
                jock_to_file(language, f"{c}. {text}", "all_jocks.docx")
            elif num == 1: 
                jock_to_file(language, f"{c}. {text}", "1_jock.docx")
            else:
                jock_to_file(language, f"{c}. {text}", f"{num}_jocks.docx")

    if mode == 2:
        if num == noaj:
            my_print(t.print_file_saved("all_jocks.docx"), 2)
        elif num == "1":
            my_print(t.print_file_saved("1_jock.docx"), 2)
        else:
            my_print(t.print_file_saved(f"{num}_jocks.docx"), 2)
            
    clear_doc()
    print()

#endregion Tool
#endregion Jock
#region Tool
def end_of_work():  #to prompt the user to return to the menu or exit
    logger(language, t.log_after_jokes.copy())
    selection = my_input(t.input_mini_menu.copy())
    if selection == "1":
        menu_by_user_type()
    elif selection == "2":
        my_exit()
    else:
        error_confirm()

def guide():
    clear_terminal()
    my_print(t.print_guide.copy(), 3)
    selection = my_input(t.input_guide.copy())
    if selection == "1":
        clear_terminal()
        my_print(t.print_email_support.copy(), 3)
        end_of_work()
    elif selection == "2":
        menu_by_user_type()
    elif selection == "3":
        my_exit()
    else:
        error_confirm()

def about():  #to display the about page
    clear_terminal()
    my_print(t.print_about.copy(), 3)
    end_of_work()
#endregion Tool
#endregion Main
