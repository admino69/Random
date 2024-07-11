import time
import rotatescreen as rs


import os
import getpass
USER_NAME = getpass.getuser()

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)   

#---------------------------------------

def rotate_primary_display():
    pd = rs.get_primary_display()
    angles = [90, 180, 270, 0]

    for i in range(5):
        while True:
            for x in angles:
                pd.rotate_to(x)
                time.sleep(0.1) # Adjust the sleep duration as needed

if __name__ == "__main__":
    rotate_primary_display()


