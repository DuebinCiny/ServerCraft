# ServerCraft Version 0.1.0 - The first version!
# importing modules
    # import requests
import pickle
import os
import requests
# startup tasks
current_directory = os.path.dirname(__file__)
incorrectversion = False
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
with open(current_directory + r"\\vanilla_server_urls.pkl", "rb") as handle:
    vanilla_server_urls = pickle.load(handle)
# Intro
print("This is a very early version of this application. It only supports vanilla servers at this time, and future builds")
print("will include support for other server softwares. The server softwares listed other than vanilla will not actually function.")
print("Also, it is reccommended to maximize the console window you are running this in for the best readability.")
input("Press enter if you understand.")
print("ServerCraft V 0.1.0")
print("Welcome to ServerCraft: an application to easily and quickly install a Minecraft server!")
print("Note: This project/application is not affilated with Mojang, Microsoft, or any official Minecraft branding.")
print("Next major update: Bungeecord support. Will add the ability to setup a bungeecord network of multiple Minecraft servers.")
print("NOTICE: Java JDK MUST be installed for you Minecraft Server to run and this app to work properly. Make sure Java is installed before creating servers.")
# Collecting User Intentions
print("Now you will select what type of server installation you would like to perform. ")
print("standard (Vanilla installation), forge (Modded Configuration), spigot, bukkit, or paper.")
info_yn = input("Would you like to see info for any of the configurations? (y/n)")
if info_yn == 'y':
    while info_yn == 'y':
        info = input("To select which server software to get info for, enter the configuration name in ALL lowercase OR to exit the info page, enter 'exit'")
        if info == 'standard':
            print("A standard, default configuration of the vanilla minecraft server software.")
            print("Here is the Wiki page for more info: https://minecraft.fandom.com/wiki/Tutorials/Setting_up_a_server")
        elif info == 'forge':
            print("A forge configuration will install a forge server allowing for you to run server side mods on your server!")
            print("More configuration info can be found at the Wiki: https://minecraft.fandom.com/wiki/Tutorials/Setting_up_a_Minecraft_Forge_server")
        elif info == 'bukkit':
            print("A bukkit configuration will install a server using the bukkit software which allows you to perform more advanced and useful configuration than a typical Vanilla server and allows for the use of plugins.")
            print("More information on bukkit configuration and usage can be found at the Wiki: https://bukkit.fandom.com/wiki/Main_Page")
        elif info == 'spigot':
            print("A spigot configuration is very similar in functionality to a bukkit configuration, allowing for even more advanced configuration and plugins. Spigot is based off of Bukkit and will act very similarly.")
            print("More information on Spigot can be found at the official Wiki: https://www.spigotmc.org/wiki/index/")
        elif info == 'paper':
            print("A Paper configuration will install a server using the paper server software. Paper is a light-weight alternative to Spigot that can vastly improve server performance and is reccommended if running servers on a lower spec computer.")
            print("More information about Paper can be found at the official documentation page: https://docs.papermc.io/paper")
        elif info == 'exit':
            print('Exiting Info Page.')
            info_yn = 'n'
        else:
            print("That is not a valid configuration type. (Did you use lowercase and spell correctly?)")
configuration_type = input("What type of server would you like to make? Enter the name of the confiuration you would like to create a Minecraft server with.")
config_type_check = True
while config_type_check == True:
    if configuration_type in ("standard","forge","spigot","bukkit","paper"):
        config_type_check = False
    else:
        configuration_type = input("You have entered an invalid selection. Please enter a valid server installation type.")
print("Let's get started with setting up your " + configuration_type + " minecraft server installation!")
print("First, lets gather some information to make your server exactly how you want it.")
name = input("What would you like to name your server?")
print("You will now be asked how much memory to give to the server. An example confiuration for a computer with 8GB of total memory is 4GB max and 2GB allocated.")
print("(1000MB = 1GB)")
(ram_xms) = str(input("How much memory (RAM) would you like to allocate to the server? Please enter the value as a number in megabytes (MB). This is usually half of your maximum memory."))
(ram_xmx) = str(input("What would you like the max memory consumtion of the server to be? Please enter the value as a number in megabytes (MB). For best relability, it is recommended you do not give more than half of your computer's RAM to the server, otherwise this could cause instabilities and crashes."))
print("Now, the server will be downloaded and we can get to the fun part. Running your server!")
print("Note: The server will be automatically installed to the desktop in a folder with the name you previously chose, but you can always move the server after the installation is complete.")
if configuration_type == 'standard':
    version = input("One last thing. What version of minecraft would you like to run your server on? (Use x.x.x format Example: 1.19.2 | 1.2.5 - Latest release compatible) List of versions here: https://mcversions.net/")
    if version not in vanilla_server_urls:
        incorrectversion = True
    while incorrectversion == True:
        if version not in vanilla_server_urls:
            version = input("You have entered an incorrect version. Please enter a valid version selection.")
        if version in vanilla_server_urls:
            incorrectversion = False
    path = os.path.join(desktop, name)
    os.mkdir(path)
    server_url = vanilla_server_urls.get(version)
    response = requests.get(server_url)
    open(path + r"\\server.jar", "wb").write(response.content)
    if input("Would you like to enable the server GUI? Otherwise it will just display a command prompt.") == 'yes':
        nogui = False
    else:
        nogui = True
    print("The command prompt output will be enabled by default but it can be disabled by adding a second line '@echo off' to the start.bat file in the " + name + " folder.")
    if nogui:
        batchfile = open(path + r'\\start.bat','w+')
        batchfile.write('java -Xmx' + ram_xmx + 'M -Xms' + ram_xms + 'M -jar server.jar nogui')
        batchfile.close()
    if not nogui:
        batchfile = open(path + r'\\start.bat','w+')
        batchfile.write('java -Xmx' + ram_xmx + 'M -Xms' + ram_xms + 'M -jar server.jar')
        batchfile.close()
    print("Setup Complete! Run the start.bat file in the " + name + " folder and open the eula.txt file that is generated. Then, change false to true, save the document and run the start.bat again.")
    print("Your server is now ready!")
    print("Note: This server will only be available on your local network. In order for players outside your network to join, you must portfoward, which this tool cannot aid in.")
    input("Thank you for using ServerCraft! I hope it was useful to you! Press enter to close the application.")
