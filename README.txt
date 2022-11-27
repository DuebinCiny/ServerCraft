# ServerCraft
A tool that makes it easy, quick, and simple to install a minecraft server with a large variety of configurations.
Prerequisites (For exe users):
Java JDK 17

Prerequisites (For users running the python script directly):
Java JDK 17, Python 3, as well as the following python module(s): requests

How to setup (Executable File):
Download the latest EXE file from the releases section on the github. Run the EXE.

How to setup (Python script):
Download the zip file of the repository by clicking the code button and clicking download zip file.
Extract the python script and the .pkl file and put them in a folder together. Run the python script.

How to use the program:
Read the introduction notice, then press enter. 
If you would like to see info about the configuration types, enter 'y', otherwise, enter 'n'.
Choose a configuration by typing the name of the configuration type listed you would like to use, then press enter. (IMPORTANT: Currently, 'standard' is the only functional configuration type, so select standard. Future releases will add the other configuration types.)
Type the name of the server you would like to use, then press enter. This will be used as the name for the folder containing your server, and can be changed later.
Enter the maximum amount of ram you would like the server to have, then press enter.
Enter the amount of ram you would like to allocate to the server, then press enter.
Enter the minecraft server version you would like to use, then press enter.
The server jar file will now be downloaded and depending on your internet speed, may take a moment. Wait until the prompt asking if you would like to enable the GUI
shows up.
If you would like to enable the minecraft server GUI which can be used to see currently online players, enter commands directly into the server, and see resource usage, type 'yes', then press enter. Otherwise, type 'no', then press enter. 
You server installation is now complete!

Running your minecraft server:
Open the folder on your desktop that has the name you chose for your server earlier. Run the start.bat file to launch the server. 
A few files will be generated inside the folder. Open the EULA.txt file and change false to true, then save the file and close it.
By doing so, you are agreeing to minecraft's End User Liscence Agreement.
Run the start.bat file again and your server should now be running on localhost! You can join it by going into a minecraft client on the host computer and joining the ip address 'localhost'.
The server runs on port 25565 by default, but can be changed in server.properties.
Note: You must port foward for users outside your network to join.

How to disable the command prompt server output:
Open the start.bat file in a text editor, then add a line at the end '@echo off' then save the file.

How to join from other computers on your local network.
In the multiplayer tab of a minecraft client, click direct connect or add a new server, and enter the local ip address of the host machine in the ip field.
The name of the server does not matter.
At the end of the ip address, type ':25565', or replace 25565 with the port you chose in server.properties.
You should now be able to join the server on your local network using that ip adress.
If you cannot connect, check the firewall and network rules on your host machine.
