# ServerCraft Version 0.1.0 - The first version!
# importing modules
import os

# Checking if Java is installed
java = os.system("java -version")
if java == "'java' is not recognized as an internal or external command, operable program or batch file.":
    print("You must install Java to run this program. You can download Java at ")

# Intro
print("ServerCraft V 0.1.0")
print("Welcome to ServerCraft: an application to easily and quickly install a Minecraft server!")
print("Note: This project/application is not affilated with Mojang, Microsoft, or any official Minecraft branding.")
print("Next update: Bungeecord support. Will add the ability to setup a bungeecord network of multiple Minecraft servers.")
print("Future planned update(s): Presets! One input creates a server based on a preset for which server software to use!")

# Collecting User Intentions
mode = input("Would you like to use beginner (enter 'b') or advanced (enter 'a') configuration?")

if mode == 'b':
    print("Now you will select what type of server installation you would like to perform. ")
    print("The options for a beginner configuration are Standard (Vanilla installation), Forge (Modded Configuration), Spigot, Bukkit, or Paper.")
    info_yn = input("Would you like to see info for any of the configurations? (y/n)")
    if info_yn == 'y':
        while info_yn == 'y':
            info = input("To select which server software to get info from, enter the configuration name in ALL lowercase OR to exit the info page, enter 'exit'")
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
                print("A Paper configuration is one where the server software paper is used with no additional auto-config. Paper is a light-weight alternative to Spigot.")
                print("More information about Paper can be found at the official documentation page: https://docs.papermc.io/paper")
            elif info == 'exit':
                print('Exiting Info Page.')
                info_yn = 'n'
            else:
                print("That is not a valid configuration type. (Did you use lowercase and spell correctly?)")
    beginner_mode = input("What type of server would you like to make? Enter the name of the confiuration you would like to create a Minecraft server with.")
    if beinnger_mode == 'standard':
        print("Let's get started with setting up your standard minecraft server installation!")
        print("First, lets gather some information to make your server exactly how you want it.")
        name = input("What would you like to name your server?")
        print("You will now be asked how much memory to give to the server. An example confiuration for a computer with 8GB of total memory is 4GB max and 2GB allocated.")
        print("(1000MB = 1GB)")
        ram_xmx = input("What would you like the max memory consumtion of the server to be? Please enter the value as a number in megabytes (MB). For best relability, it is recommended you do not give more than half of your computer's RAM to the server, otherwise this could cause instabilities and crashes.")
        ram_xms = input("How much memory (RAM) would you like to allocate to the server? Please enter the value as a number in megabytes (MB). This is usually half of your maximum memory.")
