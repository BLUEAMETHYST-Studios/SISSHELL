"""
               [ SISSHELL ]
=======================================

- Easy-use command line tool
- Smaller Syntaxes than CMD!  
- Better UI than CMD (COLORS!)
    
=======================================

"""

try:
    import time
    import os
    import sys
    import socket
    import psutil
    import platform
    import colorama
    import zipfile
    import pwinput
    from colorama import Fore
    from getmac import getmac
except ImportError:
    print("Uninstalled libraries detected!")
    input("CLOSE > ")
    sys.exit()

colorama.init(autoreset=True)

os.system("cls")
os.system("title SISSHELL")

BATTERYLIFE = psutil.sensors_battery()
DATE = time.strftime("%d/%m/%y")
UNIX = time.time()
PROCESSOR = platform.processor()
CPUCOUNT = psutil.cpu_count()
MEM = psutil.virtual_memory().total / int(1024. **3)
HOST = socket.gethostname()
LOCALIP = socket.gethostbyname(HOST)
MAC = getmac.get_mac_address()
NETINCARD = psutil.net_if_addrs().keys()
NICLIST = list(NETINCARD) # converts the NETINCARD variable into a list
USERNAME = os.getlogin()
CWD = os.getcwd()
LOCALDIR = os.chdir("C:/Users/" + USERNAME + "/AppData/Local")
OS = platform.system()
DEVMODE = False

def checkAdmin():
    if not os.path.exists("C:/Users/" + USERNAME + "/AppData/Local/SISSHELL/master-data.txt"):
        pass
    else:
        os.chdir("C:/Users/" + USERNAME + "/AppData/Local/SISSHELL/")
        with open("master-data.txt", "r") as check:
            ADMIN_READ = check.read()
            check.close()
        print(Fore.LIGHTBLUE_EX + "Please enter the password to execute this program!")
        ADMIN_CHECK = pwinput.pwinput(str(Fore.LIGHTBLUE_EX + "SISSHELL" + Fore.WHITE + "/" + Fore.LIGHTGREEN_EX + USERNAME + Fore.WHITE + "/" + Fore.CYAN + "CONFIRM" + Fore.WHITE + " > " + Fore.YELLOW), mask="*")
        if ADMIN_CHECK == ADMIN_READ:
            pass
        else:
            os.system("cls")
            print(Fore.RED + "WRONG PASSWORD!")
            input(Fore.RED + "ENTER to close > ")
            sys.exit()

checkAdmin()

os.chdir("C:/Users/" + USERNAME)

print(Fore.LIGHTGREEN_EX + "SISSHELL " + Fore.LIGHTBLUE_EX + "Beta v.1.1")
print(Fore.LIGHTGREEN_EX + 'Type "help" for assistance!')
print("\n")


while True:
    SISSHELL = input(str(Fore.LIGHTBLUE_EX + "SISSHELL" + Fore.WHITE + "/" + Fore.LIGHTGREEN_EX + USERNAME + Fore.WHITE + " > " + Fore.YELLOW))
    
    if SISSHELL == "help":
        print(Fore.WHITE + "======================================================================================================================\n")
        print(Fore.LIGHTBLUE_EX + "cd <args>" + Fore.LIGHTGREEN_EX + "      - " + Fore.LIGHTBLUE_EX + "  Changes the current working directory")
        print(Fore.LIGHTBLUE_EX + "ls" + Fore.LIGHTGREEN_EX + "             - " + Fore.LIGHTBLUE_EX + "  Lists all files in the current working directory")
        print(Fore.LIGHTBLUE_EX + "pwd" + Fore.LIGHTGREEN_EX + "            - " + Fore.LIGHTBLUE_EX + "  Shows you the current working directory")
        print(Fore.LIGHTBLUE_EX + "cwd" + Fore.LIGHTGREEN_EX + "            - " + Fore.LIGHTBLUE_EX + "  Shows you the current working directory")
        print(Fore.LIGHTBLUE_EX + "whereami" + Fore.LIGHTGREEN_EX + "       - " + Fore.LIGHTBLUE_EX + "  Shows you the current working directory")
        print(Fore.LIGHTBLUE_EX + "md <args>" + Fore.LIGHTGREEN_EX + "      - " + Fore.LIGHTBLUE_EX + "  Creates a new directory/folder")
        print(Fore.LIGHTBLUE_EX + "dd <args>" + Fore.LIGHTGREEN_EX + "      - " + Fore.LIGHTBLUE_EX + "  Deletes a directory")
        print(Fore.LIGHTBLUE_EX + "cf <args>" + Fore.LIGHTGREEN_EX + "      - " + Fore.LIGHTBLUE_EX + "  Creates a new file")
        print(Fore.LIGHTBLUE_EX + "sf <args>" + Fore.LIGHTGREEN_EX + "      - " + Fore.LIGHTBLUE_EX + "  Selects a file to be managed")
        print(Fore.LIGHTBLUE_EX + "uz <args>" + Fore.LIGHTGREEN_EX + "      - " + Fore.LIGHTBLUE_EX + "  Extracts a ZIP-File")
        print(Fore.LIGHTBLUE_EX + "reg-admin" + Fore.LIGHTGREEN_EX + "      - " + Fore.LIGHTBLUE_EX + "  Register and manage an Administartor Account")
        print(Fore.LIGHTBLUE_EX + "shutdown" + Fore.LIGHTGREEN_EX + "       - " + Fore.LIGHTBLUE_EX + "  Shuts your system down (Extra Steps: Time, Reason)")
        print(Fore.LIGHTBLUE_EX + "sd" + Fore.LIGHTGREEN_EX + "             - " + Fore.LIGHTBLUE_EX + "  Shuts your system down (Extra Steps: Time, Reason)")
        print(Fore.LIGHTBLUE_EX + "whoami" + Fore.LIGHTGREEN_EX + "         - " + Fore.LIGHTBLUE_EX + "  Shows your current name")
        print(Fore.LIGHTBLUE_EX + "sys" + Fore.LIGHTGREEN_EX + "            - " + Fore.LIGHTBLUE_EX + "  Shows some info about Sistem and your hardware")
        print(Fore.LIGHTBLUE_EX + "echo <args>" + Fore.LIGHTGREEN_EX + "    - " + Fore.LIGHTBLUE_EX + "  Sends a specific message")
        print(Fore.LIGHTBLUE_EX + "title <args>" + Fore.LIGHTGREEN_EX + "   - " + Fore.LIGHTBLUE_EX + "  Sets the title of the terminal")
        print(Fore.LIGHTBLUE_EX + "title-reset" + Fore.LIGHTGREEN_EX + "    - " + Fore.LIGHTBLUE_EX + "  Resets the current title to SISSHELL")
        print(Fore.LIGHTBLUE_EX + "time" + Fore.LIGHTGREEN_EX + "           - " + Fore.LIGHTBLUE_EX + "  Shows the current date and unixtime")
        print(Fore.LIGHTBLUE_EX + "netinfo" + Fore.LIGHTGREEN_EX + "        - " + Fore.LIGHTBLUE_EX + "  Shows some info about your local network")
        print(Fore.LIGHTBLUE_EX + "run <args>" + Fore.LIGHTGREEN_EX + "     - " + Fore.LIGHTBLUE_EX + "  Allows you to run a file in your current working directory")
        print(Fore.LIGHTBLUE_EX + "exit" + Fore.LIGHTGREEN_EX + "           - " + Fore.LIGHTBLUE_EX + "  Close this window")
        print(Fore.WHITE + "\n======================================================================================================================")
    
    elif SISSHELL == "whoami":
        print(Fore.LIGHTGREEN_EX + "Current Host: " + Fore.CYAN + USERNAME)
    elif SISSHELL == "sys":
        print("\n")
        print(Fore.LIGHTBLUE_EX + "   _____ _____  _____ _____ _    _ ______ _      _      " + Fore.LIGHTGREEN_EX + "  Running: SISSHELL")
        print(Fore.LIGHTBLUE_EX + "  / ____|_   _|/ ____/ ____| |  | |  ____| |    | |     " + Fore.LIGHTGREEN_EX + "  Version: Beta 1.0") 
        print(Fore.LIGHTBLUE_EX + " | (___   | | | (___| (___ | |__| | |__  | |    | |     " + Fore.LIGHTGREEN_EX + "  Username: " + USERNAME)
        print(Fore.LIGHTBLUE_EX + "  \___ \  | |  \___ \ ___ \|  __  |  __| | |    | |     " + Fore.LIGHTGREEN_EX + "  Device Name: " + HOST)
        print(Fore.LIGHTBLUE_EX + "  ____) |_| |_ ____) |___) | |  | | |____| |____| |____ " + Fore.LIGHTGREEN_EX + "  OS: " + OS)
        print(Fore.LIGHTBLUE_EX + " |_____/|_____|_____/_____/|_|  |_|______|______|______|" + Fore.LIGHTGREEN_EX + "  Memory: " + str(MEM) + " GB")
        print("\n")
    elif SISSHELL == "reg-admin":
        if os.path.exists("C:/Users/" + USERNAME + "/AppData/Local/SISSHELL/master-data.txt"):
            print(Fore.RED + 'An admin account was already created!\nDo you want to replace the password?\nType y or n to do that!')
            print(Fore.RED + 'If you want to remove the admin account, type "rm-admin"!')
            ADMIN_RESET_PW = input(str(Fore.LIGHTBLUE_EX + "SISSHELL" + Fore.WHITE + "/" + Fore.LIGHTGREEN_EX + USERNAME + Fore.WHITE + "/" + Fore.CYAN + "ADMIN" + Fore.WHITE + " (y/n/rm-admin) > " + Fore.YELLOW))
            if ADMIN_RESET_PW == "y" or ADMIN_RESET_PW == "Y":
                print()
            elif ADMIN_RESET_PW == "n" or ADMIN_RESET_PW == "N":
                print(Fore.RED + "Cancelled!")
            elif ADMIN_RESET_PW == "rm-admin":
                print(Fore.LIGHTBLUE_EX + "Please enter the Admin-Account's password to proceed!")
                RM_ADMIN_PW = pwinput.pwinput(str(Fore.LIGHTBLUE_EX + "SISSHELL" + Fore.WHITE + "/" + Fore.LIGHTGREEN_EX + USERNAME + Fore.WHITE + "/" + Fore.CYAN + "ADMIN" + Fore.WHITE + " > " + Fore.YELLOW), mask="*")
                os.chdir("C:/Users/" + USERNAME + "/AppData/Local/SISSHELL")
                with open("master-data.txt", "r") as pw:
                    PW_RM_ADMIN = pw.read()
                    pw.close()
                if RM_ADMIN_PW == PW_RM_ADMIN:
                    print(Fore.LIGHTBLUE_EX + "Please confirm, that you want to do this!")
                    RM_ADMIN_CONFIRM = input(str(Fore.LIGHTBLUE_EX + "SISSHELL" + Fore.WHITE + "/" + Fore.LIGHTGREEN_EX + USERNAME + Fore.WHITE + "/" + Fore.CYAN + "ADMIN" + Fore.WHITE + " (y/n) > " + Fore.YELLOW))
                    if RM_ADMIN_CONFIRM == "y" or RM_ADMIN_CONFIRM == "Y":
                        os.chdir("C:/Users/" + USERNAME + "/AppData/Local/SISSHELL")
                        os.system("del master-data.txt")
                        print(Fore.LIGHTGREEN_EX + "Admin-Account was removed!")
                    elif RM_ADMIN_CONFIRM == "n" or RM_ADMIN_CONFIRM == "N":
                        print(Fore.RED + "Cancelled action of removing the Admin-Account!")
                    else:
                        print(Fore.RED + "Invalid input!\nAction cancelled!")
                else:
                    print(Fore.RED + "Wrong password!\nThe action was cancelled!")
            else:
                print(Fore.RED + "Invalid input! Action was cancelled!")
        else:
            print(Fore.LIGHTBLUE_EX + "To create an admin account, you'll need to set a password and confirm it!")
            ADMIN_SET_PW = pwinput.pwinput(str(Fore.LIGHTBLUE_EX + "SISSHELL" + Fore.WHITE + "/" + Fore.LIGHTGREEN_EX + USERNAME + Fore.WHITE + "/" + Fore.CYAN + "ADMIN" + Fore.WHITE + " > " + Fore.YELLOW), mask="*")
            print(Fore.LIGHTBLUE_EX + "Confirm this password by entering it again!")
            ADMIN_SET_PW_CONFIRM = pwinput.pwinput(str(Fore.LIGHTBLUE_EX + "SISSHELL" + Fore.WHITE + "/" + Fore.LIGHTGREEN_EX + USERNAME + Fore.WHITE + "/" + Fore.CYAN + "ADMIN" + Fore.WHITE + " > " + Fore.YELLOW), mask="*")
            if ADMIN_SET_PW == ADMIN_SET_PW_CONFIRM:
                os.chdir("C:/Users/" + USERNAME + "/AppData/Local/SISSHELL")
                with open("master-data.txt", "w") as pw:
                    pw.write(str(ADMIN_SET_PW))
                    pw.close()
                print(Fore.LIGHTGREEN_EX + "Password set!")
            else:
                print(Fore.RED + "The value of the password confirmation wasn't equal to the set password!\nThe action was cancelled!")
    try:
        ECHOCHECK = []
        ECHO = ""
        ECHOCHECK.clear()
        ECHOCHECK[:0] = SISSHELL
        if ECHOCHECK[0] == "e" and ECHOCHECK[1] == "c" and ECHOCHECK[2] == "h" and ECHOCHECK[3] == "o" and ECHOCHECK[4] == " ":
            ECHOCHECK.remove("e")
            ECHOCHECK.remove("c")
            ECHOCHECK.remove("h")
            ECHOCHECK.remove("o")
            ECHOCHECK.remove(" ")
            ECHO = "".join(ECHOCHECK)
            print(Fore.WHITE + ECHO)
    except IndexError:
        pass
    except Exception:
            print(Fore.RED + "An unknown exception happened!")
    try:
        TITLECHECK = []
        TITLE = ""
        TITLECHECK.clear()
        TITLECHECK[:0] = SISSHELL
        if TITLECHECK[0] == "t" and TITLECHECK[1] == "i" and TITLECHECK[2] == "t" and TITLECHECK[3] == "l" and TITLECHECK[4] == "e" and TITLECHECK[5] == " ":
            TITLECHECK.remove("t")
            TITLECHECK.remove("i")
            TITLECHECK.remove("t")
            TITLECHECK.remove("l")
            TITLECHECK.remove("e")
            TITLECHECK.remove(" ")
            TITLE = "".join(TITLECHECK)
            os.system("title " + TITLE)
            print(Fore.LIGHTGREEN_EX + "Changed title of the Shell for this session!")
    except IndexError:
        pass
    except Exception:
            print(Fore.RED + "An unknown exception happened!")
    if SISSHELL == "title-reset":
        os.system("title SISSHELL")
    elif SISSHELL == "time":
        print(Fore.CYAN + "Current Date: " + Fore.LIGHTGREEN_EX + DATE)
        print(Fore.CYAN + "Current Unixtime: " + Fore.LIGHTGREEN_EX + str(UNIX))
    elif SISSHELL == "netinfo":
        
        print(Fore.CYAN + "Your local host name: " + Fore.LIGHTGREEN_EX + HOST)
        print(Fore.CYAN + "Your local IP address: " + Fore.LIGHTGREEN_EX + LOCALIP)
        print(Fore.CYAN + "Your MAC Address: " + Fore.LIGHTGREEN_EX + MAC)
        print(Fore.CYAN + "Network Adapters: " + Fore.LIGHTGREEN_EX + str(NICLIST))
    try:
        if SISSHELL.startswith("cd "):
            CD = SISSHELL[3:]
            try:  
                os.chdir(CD)
            except FileNotFoundError:
                print(Fore.RED + "This directory doesn't exist on your device!")
            except Exception:
                print(Fore.RED + "An unknown exception happened during the execution of this command!")
            
    except:
        pass
    if SISSHELL == "ls":
        print(Fore.CYAN + str(os.listdir()))
    elif SISSHELL == "pwd" or SISSHELL == "cwd" or SISSHELL == "whereami":
        print(Fore.CYAN + os.getcwd())
    try:
        if SISSHELL.startswith("run "):
            RUN = SISSHELL[4:]
            os.system("start " + RUN)
    except FileNotFoundError:
        print(Fore.RED + "This file doesn't exist in your current working directory or the path you entered was wrong!")
    except IndexError:
        pass
    except Exception:
        print(Fore.RED + "An unknown exception happened while trying to run this file!")
    
    try:
        if SISSHELL.startswith("md "):
            MD = SISSHELL[3:]
            os.mkdir(MD)
    except FileExistsError:
        print(Fore.RED + "This folder already exists in that directory!")
    except IndexError:
        pass
    except PermissionError:
        print(Fore.RED + "You've no permissions to create directories in that directory!")
    except Exception:
        print(Fore.RED + "An unknown exception happened during the creation of the folder!")
    try:
        if SISSHELL.startswith("cf "):
            CF = SISSHELL[3:]
            with open(str(CF), "w") as cf:
                cf.write("")
                cf.close()
                print(Fore.LIGHTGREEN_EX + "A new file was created!")
    except IndexError:
        pass
    except PermissionError:
        print(Fore.RED + "You've no permission to create files in that directory!")
    except FileExistsError:
        print(Fore.RED + "This file already exists in the current working directory!")
    except Exception:
        print(Fore.RED + "An unknown exception happened during the creation of the file!")
    try:
        if SISSHELL.startswith("sf "):
            SF = SISSHELL[3:]
            with open(str(SF), "r") as sf_filecheck:
                sf_filecheck.read()
                sf_filecheck.close()
            print(Fore.LIGHTBLUE_EX + "Enter an option: ")
            print(Fore.LIGHTGREEN_EX + "read")
            print(Fore.LIGHTGREEN_EX + "write")
            print(Fore.LIGHTGREEN_EX + "delete")
            SF_ACTION = input(str(Fore.LIGHTBLUE_EX + "SISSHELL" + Fore.WHITE + "/" + Fore.LIGHTGREEN_EX + USERNAME + Fore.WHITE + "/" + Fore.CYAN + "SF" + Fore.WHITE + " > " + Fore.YELLOW))
            if SF_ACTION == "read":
                with open(str(SF), "r") as sf_read:
                    SF_READ_CONTENT = sf_read.read()
                    print(SF_READ_CONTENT)
                    sf_read.close()
            elif SF_ACTION == "write":
                with open(str(SF), "w") as sf_write:
                    print(Fore.CYAN + "Type in the content of the file!")
                    SF_WRITE_CONTENT_INPUT = input(str(Fore.LIGHTBLUE_EX + "SISSHELL" + Fore.WHITE + "/" + Fore.LIGHTGREEN_EX + USERNAME + Fore.WHITE + "/" + Fore.CYAN + "SF" + Fore.WHITE + "/" + Fore.LIGHTGREEN_EX + "WRITE" + Fore.WHITE + " > " + Fore.YELLOW))
                    SF_WRITE_CONTENT = sf_write.write(str(SF_WRITE_CONTENT_INPUT))
            elif SF_ACTION == "delete":
                os.system("del " + str(SF))
            else:
                print(Fore.RED + "Invalid input! Select between: read, write or delete!")
    except IndexError:
        pass
    except PermissionError:
        print(Fore.RED + "You can't interact with that file!")
    except FileNotFoundError:
        print(Fore.RED + "Wasn't able to find this file in the current working directory!")
    except Exception:
        print(Fore.RED + "An unknown exception happened during the process of interacting with that file!")
    if SISSHELL == "exit":
        sys.exit()
    elif SISSHELL == "shutdown" or SISSHELL == "sd":
        print(Fore.LIGHTGREEN_EX + "Enter the shutdown time-limit! (Must be an Integer)")
        SD_TIME = input(str(Fore.LIGHTBLUE_EX + "SISSHELL" + Fore.WHITE + "/" + Fore.LIGHTGREEN_EX + USERNAME + Fore.WHITE + "/" + Fore.CYAN + "SD" + Fore.WHITE + "/" + Fore.LIGHTGREEN_EX + "TIME" + Fore.WHITE + " > " + Fore.YELLOW))
        try:
            int(SD_TIME)
        except ValueError:
            print(Fore.RED + "This input isn't an integer!")
        except Exception:
            print(Fore.RED + "The process was cancelled due to an unknown exception!")
        else:
            print(Fore.LIGHTGREEN_EX + "What should be the reason for the shutdown?")
            SD_REASON = input(str(Fore.LIGHTBLUE_EX + "SISSHELL" + Fore.WHITE + "/" + Fore.LIGHTGREEN_EX + USERNAME + Fore.WHITE + "/" + Fore.CYAN + "SD" + Fore.WHITE + "/" + Fore.LIGHTGREEN_EX + "REASON" + Fore.WHITE + " > " + Fore.YELLOW))
            print(Fore.LIGHTGREEN_EX + "Please confirm.")
            SD_CONFIRM = input(str(Fore.LIGHTBLUE_EX + "SISSHELL" + Fore.WHITE + "/" + Fore.LIGHTGREEN_EX + USERNAME + Fore.WHITE + "/" + Fore.CYAN + "SD" + Fore.WHITE + "/" + Fore.LIGHTGREEN_EX + "CONFIRM" + Fore.WHITE + " (y/n) > " + Fore.YELLOW))
            if SD_CONFIRM == "Y" or SD_CONFIRM == "y":
                try:
                    os.system("shutdown /s /t " + str(SD_TIME) + " /c " + '"' + str(SD_REASON) + '"')
                    print(Fore.LIGHTRED_EX + "Shutting down in " + SD_TIME + ' seconds.\nType "cancel" to cancel the shutdown')
                    SD_CANCEL = input(str(Fore.LIGHTBLUE_EX + "SISSHELL" + Fore.WHITE + "/" + Fore.LIGHTGREEN_EX + USERNAME + Fore.WHITE + "/" + Fore.CYAN + "SD" + Fore.WHITE + "/" + Fore.LIGHTRED_EX + "CANCEL" + Fore.WHITE + " > " + Fore.YELLOW))
                    if SD_CANCEL == "cancel":
                        try:
                            os.system("shutdown -a")
                            print(Fore.LIGHTGREEN_EX + "The shutdown was cancelled!")
                        except Exception:
                            print(Fore.RED + "Due to an unknown exception, you weren't able to cancel the shutdown!")
                except IndexError:
                    pass
                except Exception:
                    print(Fore.RED + "An unknown and unexpected exception happened during this process!")
            elif SD_CONFIRM == "N" or SD_CONFIRM == "n":
                print(Fore.LIGHTGREEN_EX + "Shutdown cancelled!")
    try:
        if SISSHELL.startswith("dd "):
            DD = SISSHELL[3:]
            try:
                os.rmdir(str(DD))
                print(Fore.LIGHTGREEN_EX + "Directory deleted!")
            except IndexError:
                pass
            except PermissionError:
                print(Fore.RED + "You can't interact with this! (Not a directory or you don't have the permissions to delete this (or both)!)")
            except Exception:
                print(Fore.RED + "An unknown unexpected exception happened during this process!")
    except IndexError:
        pass
    except PermissionError:
        print(Fore.RED + "You don't have the permission to delete this directory!")
    except NotADirectoryError:
        print(Fore.RED + "The object, that you were trying to delete isn't a directory!")
    except Exception:
        print(Fore.RED + "An unknown unexpected exception happened during this process!")
    try:
        if SISSHELL.startswith("uz "):
            UZ = SISSHELL[3:]
            with zipfile.ZipFile(str(UZ), "r") as uz:
                if SISSHELL.startswith("uz "):
                    UZ = SISSHELL[3:]
                UZDIRRAW = UZ.rstrip(".zip")
                UZDIR = os.mkdir(UZDIRRAW)
                uz.extractall(str(UZDIRRAW))
                uz.close()
                
    except IndexError:
        pass
    except FileNotFoundError:
        print(Fore.RED + "This file doesnt exist in your current working directory or you entered a wrong path!")
    except zipfile.BadZipFile:
        print(Fore.RED + "This file isn't a ZIP-File or is not a readable ZIP-File!")
    except FileExistsError:
        print(Fore.RED + "The new directory you were trying to create by extracting the ZIP-File already exists in that directory!")
    except Exception:
        print(Fore.RED + "An unknown unexpected exception happened during this process!")
