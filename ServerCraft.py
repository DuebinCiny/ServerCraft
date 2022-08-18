# ServerCraft Version 0.1.0 - The first version!
# importing modules

# Intro
print("ServerCraft V 0.1.0")
print("Welcome to ServerCraft: an application to easily and quickly install a Minecraft server!")
print("Note: This project/application is not affilated with Mojang, Microsoft, or any official Minecraft branding.")
print("Upcoming update: Presets! One input creates a server based on a preset for which server software to use!")

# Collecting User Intentions
mode = input("Would you like to use beginner (enter 'b') or advanced (enter 'a') configuration?")

if mode == 'b':
    print("Now you will select what type of server installation you would like to perform. ")
    print("The options for a beginner configuration are Standard (Vanilla installation), Forge (Modded Configuration), Spigot, Bukkit, or Paper.")
    info_yn = input("Would you like to see info for any of the configurations? (y/n)")
    if info_yn == 'y':
        while info_yn == 'y':
            info = input("To select which server software to get info from, enter the configuration name in ALL lowercase OR to exit the info page, enter 'exit'")
            if info == 'info standard':
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
    beginner_mode = input("What type of server would you like to make? Enter 'standard', 'forge', 'bukkit', 'spigot', or 'paper' to create a Minecraft server using the respective server software.")