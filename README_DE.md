# Devoxx4Kids - Minecraft modding mit dem Raspberry Pi
Dieses Repository stellt Materialien, nützliche Informationen und Beispiele für eine einfache Modifikation
von Minecraft auf dem Raspberry Pi bereit.


[Instructions in english](README.md)

## Vorbereitungen

Zum Installieren von Minecraft auf dem Raspberry Pi müssen folgende Befehle ausgeführt werden:
```sh
sudo apt-get update
sudo apt-get install minecraft-pi
```
Das Spiel kann entweder vom Terminal aus mit
```sh
minecraft-pi
```
oder über das Startmenü
```
Games > Minecraft Pi
```
gestartet werden.


Sobald Minecraft gestartet ist, kann eine Welt geladen werden.

Unter ['Laden der flachen Welt'](#flatworld) wird erläutert wie eine vorbereitete Welt
ohne Berge und Tälern geladen werden kann.

Zum Starten einer Modifikation mit Python muss folgender Befehl ausgeführt werden:
```sh
python path/to/game.py
```
wobei 'path/to/game.py' zum Beispiel durch 'games/game-timeout.py' ersetzt werden kann.


## 'Hello World' Beispiel
Starten des 'helloWorld' Beispiels:

1. Öffne eine beliebige Welt in Minecraft
2. Starte ein neues Terminal und führe folgenden Befehl aus dem Ordner _d4k-minecraft-pi/_ aus:
    ```sh
    python example/helloWorld.py
    ```
4. Der Text "Hello World" wird im Chat von Minecraft ausgegeben.


Sehen Sie sich auch die weiteren Spiele unter [games](games) an! Viel Spaß :bowtie:


## <a name="flatworld"></a>Laden der flachen Welt

Minecraft erzeugt standardmäßig eine Welt mit Bergen und Tälern. Für unseren Zweck ist besser und einfacher
für die Kinder mit einer flachen Welt zu starten, sodass sie sich von Anfang an nicht mit der
dritten Dimension beschäftigen müssen.

Ausführen des Skripts, welches die Welt in das Spieleverzeichnis kopiert:
Führen sie das Script _add-flat-world-to-minecraft.sh_ aus dem Ordner _d4k-minecraft-pi/_ mit folgendem Befehl aus:
```sh
./flat_world/add-flat-world-to-minecraft.sh
```
um die 'flache Welt' zu Minecraft aufzunehmen.

Nun können Sie zu Beginn des Spiels die 'flache Welt' auswählen und laden.


## Möglicher Ablauf für die Arbeit mit den Kindern - basierend auf dem Spiel unter games/game-timeout.py
* Starten des helloWorld und Durchgehen der Befehle
* Programmatisch erste Blöcke setzen
* OPTIONAL: Zu Spielstart den Spieler an seine Startkoordinaten teleportieren
* Konzept der while-Schleifen einführen
* Abfragen der Block-Hit-Events, Ausgabe in die Konsole (mit print)
* OPTIONAL ABER EMPFOHLEN: Setzen von "world_immutable", um zu verhindern, dass die Welt vom Spieler verändert wird. (Block-Events werden nur mit der rechten Maustaste und dem Schwert getriggert)
* Konzept der for-in-Schleife einführen
* Konzept der if-Abfragen einführen
* Beschränken der Ausgabe auf einen bestimmten Block-Typ
* Konzept der Punkte einführen