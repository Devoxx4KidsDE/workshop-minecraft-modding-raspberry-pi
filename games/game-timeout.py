# -*- coding: utf-8 -*-
from mcpi import minecraft, block
import time

mc = minecraft.Minecraft.create()
y = mc.getHeight(0,0)

mc.postToChat("Begin")
mc.setting("world_immutable", True)
mc.setBlock(-5, y-1, 5, block.GLOWING_OBSIDIAN)
mc.setBlock( -5, y, 5, block.GOLD_ORE)
mc.setBlock( -5, y, -5, block.GOLD_ORE)
mc.setBlock( 5, y, 5, block.GOLD_ORE)
mc.setBlock( 5, y, -5, block.GOLD_ORE)
mc.setBlock(5, y - 1, -5, block.GOLD_ORE)

mc.player.setTilePos(0, y, 0)
points = 0
timer = 5
while True:
    blockEvents = mc.events.pollBlockHits()
    for event in blockEvents:
        hitBlock = mc.getBlock(event.pos.x, event.pos.y, event.pos.z)
        if hitBlock == block.GOLD_ORE.id:
            points += 1
            mc.setBlock(event.pos.x, event.pos.y, event.pos.z, block.AIR.id)
            timer += 3
        if hitBlock == block.GLOWING_OBSIDIAN.id:
            points += 3
            mc.setBlock(event.pos.x, event.pos.y, event.pos.z, block.GRASS.id)
            timer += 5
        if points == 7:
            mc.postToChat("Du hast gewonnen in " + str(timer) + " Sekunden")
            break
    timer -= 1
    print timer
    time.sleep(1)
    if timer == 0:
        mc.postToChat("deine Zeit ist um, du hast verloren :(")
        break
