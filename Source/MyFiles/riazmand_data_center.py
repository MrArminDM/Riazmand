#region My files & library
import MyFiles.riazmand_text as t
from MyFiles.riazmand_tools import logger

import random
#endregion My files & library

#region Jock loader

def get_jokes(language, num, mode):
    small_joke_reloader(language)
    jokes = joke_pack.copy()
    if language == "En":    jokes[0].replace("\ufeff ", "")
    logger(language, t.log_get_jocks.copy())
    if mode == 1:
        random_jokes = random.sample(jokes, num)
        return random_jokes
    else:
        return jokes
#endregion Jock loader
#region Save/Load

def jock_saver(language, value, work):  #to save jokes to the database
    small_joke_reloader(language)
    global joke_pack
    if work == "append":
        joke_pack.append(value)
    elif work == "remove":
        joke_pack.remove(value)
    elif work == "pop":
        joke_pack.pop(int(value))
    joke_pack.insert(0, "0")
    with open(filename(language), 'w', encoding='utf-8') as file:
        file.writelines("%s|" % data for data in joke_pack)
    small_joke_reloader(language)
    logger(language, t.jock_saver.copy())

def jock_loader(language):  #to save jokes to the database
    with open(filename(language), 'r', encoding='utf-8') as file:
        content = file.read()
        file_data = content.split("|")
        file_data.pop(0)
        file_data.pop()
    return file_data
#endregion Save/Load
#region Tool

def filename(language):  #to generate the filename for the joke database based on the language
    if language == "En":
        return "MyFiles/jock_db/en_jock_db.txt"
    else:
        return "MyFiles/jock_db/fa_jock_db.txt"
    
def small_joke_reloader(language):
    global joke_pack
    joke_pack = jock_loader(language)
#endregion Tool
