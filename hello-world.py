print ("Hallo ich bin
 ein Computer")

name = input("Wie ist dein Name")

print("Hallo schön dich zu sehen" , name, "!")
print ("dein Name ist",len(name),"Zeichen lang!")

alter = input("Wie alt bist du")
alter = int(alter)
if(alter > 100):
    print("Das ist wohl ein Scherz- oder :-)")
else:
    print ("In einem Jahr wirst du",int(alter)+1,".")
print("Tschüss...")