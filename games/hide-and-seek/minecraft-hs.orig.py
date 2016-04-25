#www.stuffaboutcode.com
#Raspberry Pi, Minecraft - verstecken spielen

#import the minecraft.py module from the minecraft directory
import minecraft.minecraft as minecraft
#import minecraft block module
import minecraft.block as block
#import time, so delays can be used
import time
# Importiere das random Modul um Zufallszahlen zu erzeugen.
import random
# Importiere das math Modul um die Quadratwurzelfunktion (sqrt) zu benutzen.
import math

# Funktion um Vektoren mit Fliesskommazahlen in Vektoren mit
# ganzen Zahlen umzuwandeln.
def runde3DVektor(einVektor):
    return minecraft.Vec3(int(einVektor.x), int(einVektor.y), int(einVektor.z))

# Funktion um den Abstand zwischen zwei Vektoren zu berechnen
def berechneAbstandZwischenZweiPunkten(punkt1, punkt2):
    xd = punkt2.x - punkt1.x
    yd = punkt2.y - punkt1.y
    zd = punkt2.z - punkt1.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))
    
if __name__ == "__main__":

    # Erzeuge ein Mincecraft-Objekt und verbinde dich
    # damit mit dem Minecraft server.
    # Minecraft muss auf dem selben Rechner laufen und
    # sich in einem Spiel befinden.
    mc = minecraft.Minecraft.create()

    # Schreibe eine Nachricht in den Chat
    mc.postToChat("Heute wollen wir in Minecraft Verstecken spielen.")

    time.sleep(2)
    
    # Ermittle die Position des Spielers
    spielerPosition = mc.player.getPos()
    
    # Erzeuge eine Zufallsposition in einer Distanz von maximal 50 Bloecken und bis zu 50
    # Bloecken ueber oder unter dem Spieler. Der versteckte Block wird an dieser Stelle
    # positioniert werden.
    zufaelligePosition = runde3DVektor(spielerPosition)
    zufaelligePosition.x = random.randrange(zufaelligePosition.x - 50, zufaelligePosition.x + 50)
    zufaelligePosition.y = random.randrange(zufaelligePosition.y - 5, zufaelligePosition.y + 5)
    zufaelligePosition.z = random.randrange(zufaelligePosition.z - 50, zufaelligePosition.z + 50)
    print zufaelligePosition
    
    # Positioniere den versteckten Diamant-Block
    mc.setBlock(zufaelligePosition.x, zufaelligePosition.y, zufaelligePosition.z, block.DIAMOND_BLOCK)
    mc.postToChat("Ich habe einen Diamanten versteckt - finde ihn!!")
    
    #Versteckspiel starten
    aufDerSuche = True
    letzteSpielerPosition = spielerPosition
    letzterAbstandVomBlock = berechneAbstandZwischenZweiPunkten(zufaelligePosition, letzteSpielerPosition)
    startZeit = time.time()
    while (aufDerSuche == True):
        # Position des Spielers ermitteln
        spielerPosition = mc.player.getPos()
        # Wenn sich der Spieler bewegt hat
        if letzteSpielerPosition != spielerPosition:
            #print "letzterAbstandVomBlock = " + str(letzterAbstandVomBlock)
            abstandVomBlock = berechneAbstandZwischenZweiPunkten(zufaelligePosition, spielerPosition)
            #print "abstandVomBlock = " + str(abstandVomBlock)
            if abstandVomBlock < 2:
                # Block Gefunden!
                aufDerSuche = False
            else:
                if abstandVomBlock < letzterAbstandVomBlock:
                    mc.postToChat("Waermer " + str(int(abstandVomBlock)) + " Bloecke entfernt")
                if abstandVomBlock > letzterAbstandVomBlock:
                    mc.postToChat("Kaelter " + str(int(abstandVomBlock)) + " Bloecke entfernt")
            
            letzterAbstandVomBlock = abstandVomBlock
            
        time.sleep(2)
    zielZeit = time.time() - startZeit
    mc.postToChat("Super gemacht! - Du hast " + str(int(zielZeit)) + " Sekunden gebraucht, um den versteckten Diamanten zu finden.")

    time.sleep(5)
    
    mc.postToChat("http://www.devoxx4kids.org")
