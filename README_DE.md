# Devoxx4Kids - Minecraft modding mit dem Raspberry Pi
Dieses Repository stellt Materialien, nützliche Informationen und Beispiele bereit, um einen Workshop zum durchzuführen, bei dem eine einfache Mod in Minecraft auf dem Raspberry Pi erstellt wird.

## Vorbereitungen
Minecraft ist kostenlos auf einem Raspberry Pi verfügbar.

Zum installieren von Minecraft auf dem Raspberry Pi müssen folgende Befehle ausgeführt werden:
```sh
sudo apt-get update
sudo apt-get install minecraft-pi
```
Jetzt kann man das Spiel vom Terminal aus starten:
```sh
minecraft-pi
```
Oder über das Startmenü:
```
Games > Minecraft Pi
```
Zum Starten muss eine Welt geladen werden. (Wenn eine komplett flache Welt gespielt werden soll, gibt es in diesem Repository ein Skript, um eine existierende flache Welt zu laden.)

Zum starten einer Mod mit Python muss folgender Befehl ausgeführt werden:
```sh
python path/to/game.py
```

**Zum Beispiel**
Starten des 'simpleGame' dieses Repositorys:

1. Öffnen einer Welt in Minecraft
2. In einem neuen Terminal folgende Befehle ausführen:
    ```sh
    cd d4k-minecraft-pi
    ```
3. Starten der Mod:
    ```sh
    python simpleGame.py
    ```
4. Der Text "Hello World" sollte im Chat erscheinen.

Sehen Sie sich auch die anderen enthaltenen Spiele an! Viel Spaß :)

## Laden der flachen Welt
Wechseln in den Ordner des Repositorys:
```sh
cd d4k-minecraft-pi
```
Ausführen des Skripts, welches die Welt in das Spieleverzeichnis kopiert:
```sh
./copyFlatWorld.sh
```
Nun können Sie zu Beginn des Spiels die flache Welt laden.

## Möglicher Ablauf für die Arbeit mit den Kindern
* Starten des simpleGame und Durchgehen der Befehle
* Programmatisch erste Blöcke setzen
* OPTIONAL: Zu Spielstart den Spieler an seine Startkoordinaten teleportieren
* Konzept der while-Schleifen einführen
* Abfragen der Block-Hit-Events, Ausgabe in die Konsole (mit print)
* OPTIONAL ABER EMPFOHLEN: Setzen von "world_immutable", um zu verhindern, dass die Welt vom Spieler verändert wird. (Block-Events werden nur mit der rechten Maustaste und dem Schwert getriggert)
* Konzept der for-in-Schleife einführen
* Konzept der if-Abfragen einführen
* Beschränken der Ausgabe auf einen bestimmten Block-Typ
* Konzept der Punkte einführen
