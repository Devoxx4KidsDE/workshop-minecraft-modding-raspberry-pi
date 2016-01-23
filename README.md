# Devoxx4Kids - Minecraft modding with Raspberry Pi
This repository provides materials, useful information, and examples for a workshop to create a simple mod in Minecraft running on a Raspberry Pi.

## Getting Started
Minecraft is for free on a Raspberry Pi.
Install Minecraft for pi on your Raspberry Pi:
```sh
sudo apt-get update
sudo apt-get install minecraft-pi
```
Now you can start the normal game via terminal:
```sh
minecraft-pi
```
Or open the start menu and go to:
```
Games>Minecraft Pi
```
Choose a world (if you want a flat world, there is a script to flat an existing world or easily copy the data of an empty world available in this repository).

Start a game via python:
```sh
python path/to/game.py
```

##Hello World example##
Starting the simple game of this repository.
Start a world in Minecraft.
In a new terminal go to the directory of this repository:
```sh
cd d4k-minecraft-pi/examples/
```
Run the simple game:
```sh
python helloWorld.py
```
The Text "Hello World" should appear in the chat.
Check out the other games available. Have fun :)

## Add the flat world

Minecraft will build by default a world with mountains and valleys.
For our purpose it is more useful and easier for the kids to have a flat world so they do not have to deal
with the third dimension from the beginning.

Go to the directory of this repository:
```sh
cd d4k-minecraft-pi
```
Execute the script which will copy the files to your minecraft folder:
```sh
./flat_world/add-flat-world-to-minecraft.sh
```
You can now choose the flat_world at the beginning of the game.

## Possible walkthrough for working with kids - based on the game at game/game-timeout.py:
* Run the helloWorld to see how it works.
* Set first blocks.
* OPTIONAL: on start reset the player to coordinates.
* Introduce the concept of a while-loop.
* Poll the block hit events and print them to see what happens.
* OPTIONAL BUT RECOMMENDED: set world immutable to avoid destroying the world without a hit event triggered (hit event only by sword with right mouse button)
* Introduce the concept of a for-in-loop.
* Introduce the concept of a if-conditions.
* Only print something if a specific block-type was hit.
* Add concept of points.
