#Zahlenreihen.py

#n = input ("Bitte n eingeben:")
#n = int (n)
n = 1000
for i in range (1,n+1):
    if (i < n):
        print (i, end="<")
    else: 
        print (i)

#alle geraden Zahlen von 1 bis n ausgeben
for i in range (1,n+1):
    if (i % 2 == 0):
        print (i, end = " ")
print()
print()
# Alle ungeraden Zahle von 1 bis n ausgeben
for i in range (1,n+1):
    if (i % 2):
        print (i, end = " ")
print()
print()
# alle Zahlen von 1 bis n die sich /9 teilen lassen ausgebn
for i in range (1,n+1):
    if (i % 9 == 0):
        if(i + 1 != n):
            print (i, end = " ")
        else:
            print (i)