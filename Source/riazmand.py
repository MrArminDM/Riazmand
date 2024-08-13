# # # # # # # # # # # # # # # #  # # # # # # # # # # # # # # # #
#                                                              #
#       █▀▀▀█ ▀ █▀▀▀█ ▀▀▀▀▀█ █▀▄ ▄▀█ █▀▀▀█ █▀▄   █ █▀▀▀▄       #
#       █▄▄▄█ █ █▄▄▄█    ▄▀  █  ▀  █ █▄▄▄█ █  █  █ █    █      #
#       █▀▄   █ █   █  ▄▀    █     █ █   █ █  █  █ █    █      #
#       █  ▀▄ █ █   █ █▄▄▄▄▄ █     █ █   █ █   ▀▄█ █▄▄▄▀       #
#                                                              #
# # # # # # # # # # # # # # # #  # # # # # # # # # # # # # # # #
#                                                              #
#   --- --- ---  ArminDM (Armin Dost Mohammadi)  --- --- ---   #
#                                                              #
#    Copyright ArminDM. Made Only for competitions & github    #
#                                                              #
# # # # # # # # # # # # # # # #  # # # # # # # # # # # # # # # #
#                                                              #
#                        Github: MrArminDM                     #
#                  My email: MrArminDM@gmail.com               #
#         Riazmand report email: report.riazmand@gmail.com     #
#                                                              #
#   --- --- ---  ArminDM (Armin Dost Mohammadi)  --- --- ---   #
#                                                              #
# # # # # # # # # # # # # # # #  # # # # # # # # # # # # # # # #

#region My files
from MyFiles.riazmand_main import start
from MyFiles.riazmand_tools import crasher, loading_animation
from MyFiles.riazmand_doc_maker import log_saver
#endregion My files

#region Main

def run():
    try:
        start()
    except SystemExit:
        pass
    except SyntaxError:
        crasher(SyntaxError)
    except IndexError:
        crasher(IndexError)
    except ValueError:
        crasher(ValueError)
    except:
        crasher("Other errors!")

    log_saver()
    loading_animation(3, "", "", 3)

def dev_run():
    start()
    log_saver()
    loading_animation(3, "", "", 3)
#endregion Main

run()
