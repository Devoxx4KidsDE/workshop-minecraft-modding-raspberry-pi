![Devoxx4Kids](http://www.devoxx4kids.de/wp-content/uploads/2015/07/cropped-header_hp.jpg)

# Devoxx4Kids - Minecraft modding with Raspberry Pi

![Minecraft](https://s-media-cache-ak0.pinimg.com/736x/a4/2c/f1/a42cf121fbcf008b82f576c98cb0791a.jpg)

This repository provides materials, useful information, and examples for a workshop to create a simple mod in
Minecraft running on a Raspberry Pi.


[Anleitung auf Deutsch](README_DE.md)


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
Games > Minecraft Pi
```
Choose a world (if you want a flat world, there is a script to flat an existing world or easily copy the data
of an empty world available in this repository).

Start a game via python:
```sh
python path/to/game.py
```
in which you can change 'path/to/game.py' with 'games/collect-blocks/game-collect-blocks.py' for example.


## Hello World example

1. Start a world in Minecraft.
2. In a new terminal execute the following command from _d4k-minecraft-pi/_:
```sh
python example/helloWorld.py
```
The Text "Hello World" appears in the chat.

Check out the other games available in [games](games). Have fun :bowtie:


## Add the flat world

Minecraft will build by default a world with mountains and valleys.
For our purpose it is more useful and easier for the kids to have a flat world so they do not have to deal
with the third dimension from the beginning.

Go to the directory of this repository:
```sh
cd d4k-minecraft-pi
```
Execute the script which will copy the files to your Minecraft folder:
```sh
./flat_world/add-flat-world-to-minecraft.sh
```
You can now choose the flat_world at the beginning of the game.