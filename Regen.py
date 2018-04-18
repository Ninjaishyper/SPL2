#regen.py
regen = True
regenschirm = False
while(regen):
 
    eingabe = input("Regnet es noch? (ja/nein) ")
    if (eingabe=="nein"):
        regen = False
        print("Geh raus")
    elif (eingabe == "ja"):
        if (regenschirm == False):
            eingabeR = input("Haben Sie einen Regenschirm(ja/nein)")
            if (eingabeR == "ja"):
                regen = False
                print("Geh nach drauen")
            else:    
                print("Warten Sie  ein bisschen")
        regenschirm = True
    else:
        print("Bitt nur ja oder nein eingeben")
#print("Jetzt regnet es nicht mehr!")
        
                
            
        

        