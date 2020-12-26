
```
   _____   _   _              _  __  ______     _____     ____    _   _    _____ 
  / ____| | \ | |     /\     | |/ / |  ____|   |  __ \   / __ \  | \ | |  / ____|
 | (___   |  \| |    /  \    | ' /  | |__      | |__) | | |  | | |  \| | | |  __ 
  \___ \  | . ` |   / /\ \   |  <   |  __|     |  ___/  | |  | | | . ` | | | |_ |
  ____) | | |\  |  / ____ \  | . \  | |____    | |      | |__| | | |\  | | |__| |
 |_____/  |_| \_| /_/    \_\ |_|\_\ |______|   |_|       \____/  |_| \_|  \_____|
                                                                                 
```

# Snakepong By Simon and Aaron

Snakepong is een combinatie van 2 klassieke videogames. Deze legendarische games zijn gecombineerd in 1 spel, Snakepong. Het is een multiplayer game waarbij men de ander moet verslaan door een hogere score te halen dan de ander voordat de snake doodgaat door zijn eigen fout.

![demo snakepong](img/demo.jpg?raw=true "proffessional example")

## installation

To run our game these are the commands you have to execute in the terminal

note : you have to open the terminal from the repository snakepong

```powershell

pip install pygame
py src/main.py
```

To quit the game press x(keyboard) or the x on the pygame terminal

## controls

### Snake:

pijltjes op het toetsenbord

### pong paddle:

z : naar boven </br>
s : naar beneden

## Analyse probleem

### componentenlijst

##### main file:
Deze code neemt alles samen en zorgt voor ook voor de basis functionaliteit.

##### snake:
De snake beweegt in segmenten die elk aangemaakt worden met de sprite class

##### walls:
De muren bestaan uit de afmetingen van de pygame origineel dachten we muren nodig te hebben. Maar door pygame is de game niet in de console maar een pop up scherm.

##### ball:
De ball class hebben we zo simpel mogelijk proberen houden, in plaats van complexere dingen te doen met graden en richting, laten we de ball in bewegen over een bepaalde snelheid over de x en y as en dan door dat te inverteren als deze ergens tegenbots verandert deze van richting.

##### pongpaddle:

De pong paddle is vlot gemaakt met behulp van de spirit. deze moet enkel naar boven en benden kunnen bewegen.

##### controller:
Deze functionaliteit zit verwerkt in de main file omdat het zeer makkelijk gaat om de controls binnen te halen met behulp van pygame


## Code schema
