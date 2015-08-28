from mcpi import minecraft, block
import time

def flatWorld(mc, x, z):
    mc.setBlocks(-10 + x,-10,-10 + z,10 + x,0,10 + z, block.GRASS.id)
    mc.setBlocks(-10 + x,0,-10 + z,10 + x,35,10 + z, block.AIR.id)   

mc = minecraft.Minecraft.create()
for xVal in range(-7, 7):
    for zVal in range(-7, 7):
        flatWorld(mc, xVal*20,zVal *20)
        print "x: " + str(xVal) + " z: " + str(zVal)
        time.sleep(1)
