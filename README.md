# Devoxx4Kids - Minecraft modding with Raspberry Pi
This Repository provides materials and usefull informations and examples for a workshop to create a simple mod in Minecraft running on a Raspberry Pi.

## Getting Started
Minecraft is for Free on a Raspberry Pi.
Install Minecraft for pi on your Raspberry Pi
```sh
sudo apt-get update
sudo apt-get install minecraft-pi
```
now you can start the normal game via terminal:
```sh
minecraft-pi
```
or open the start menu and go to:
```
Games>Minecraft Pi
```
choose a world (if you want a flat world, there is a script to flat an existing world or easyl copy the data of an empty world available in this repository)

start a game via python
```sh
python path/to/game.py
```

**For example**
starting the simple Game of this repository
Start a Wolrd in Minecraft
In a new Terminal go to the directory of this repository:
```sh
cd d4k-minecraft-pi
```
run the simple game:
```sh
python simpleGame.py
```
The Text "Hello World" should apear in the chat.

check out the other games available. Have fun :)

## Add the flat world
Go to the directory of this repository:
```sh
cd d4k-minecraft-pi
```
execute the script which will copy the files to your minecraft folder:
```sh
./copyFlatWorld.sh
```
you can now chose the flat_wolrd at the beginning of the game