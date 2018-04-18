#Zahlenraten.py
Versuch = False
import random 
zufallszahl = random.randint(1,5)

#Benutzer soll die Zahl dews COmpzuetrs erraten
while(Versuch == False):
    v = input ("Geben sie eine zufällige Zahl zwischen 1 und 5 ein!")
    if(int(v) == zufallszahl):
        Versuch = True
        print ("Sehr gut")
    else:
        print ("Nächster Versuch:")

# Ausgabe wie viele Versuche waren nötig