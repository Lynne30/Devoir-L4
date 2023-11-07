#Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif
n = int (input ("Rantre pi gwo nonb ou vle nan lis ou a : \n"))
list1 = []
for i in range(n + 1) :
    if i%2 == 0:
        list1.append(i)
print(f"Premye lis nou an ki fet ak nonb ki divizib pa 2 : {list1} \n")

#Ou gen yon lis antye, konvèti l an yon lis chenn
chenn1= ''.join(map(str,list1))
print(f"Lis chenn lan se :{chenn1} \n")

#Ou gen yon lis chenn ki an miniskil, konvèti an yon lis chenn majiskil
Majiskil = chenn1.upper()
print(f"Lis la an majiskil se : {Majiskil} \n")

#Ou gen yon lis, kreye yon nouvo lis ki fèt ak eleman ki nan endèks ki divizib pa 3 yo sèlman
list2=[]
for i in range(len(list1)):
    if i % 3 ==0:
        list2.append(list1[i])
print ( f"Nonb ki nan endeks divizib pa 3 yo se :{list2} \n" )

#Ou gen lis eleman, kreye yon nouvo lis ki gen chak 3 eleman yo gwoupe anndan yon tipl.
list3 = []
for i in range(0, len(list1),3):
    gwoup= tuple (list1[i:i+3])
    list3.append(gwoup)
print(f"Eleman yo regwoupe pa 3 nan list sa a : {list3} \n")

#Ou gen yon lis, ki gen yon pakèt eleman ki repete. Konvèti l an yon lis, ki pa gen okenn doublon
listSanDoublon= list(set(list1 + list3))
print(f"List ki San Doublon an se :{listSanDoublon} \n")

#Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman komen ant 2 lis yo
listSanDoublon1 = list(set(list1 + list2))
print(f"Eleman komen yo se : {listSanDoublon1} \n")

#Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman distenge ant 2 lis yo
list4= list1 + listSanDoublon1
ListDistenge = []
for element in list1:
    if element not in listSanDoublon1 :
        ListDistenge.append(element)
for element in listSanDoublon1:
    if element not in list1 :
        ListDistenge.append(element)
print(f"Nou te melanje List1 ak list san doublon. \ n Eleman nan premye lis la se {list1}, eleman nan list san doublon an se{listSanDoublon1} \n Lis distenge a se : {ListDistenge} \n")

#Ou gen yon diksyonè. Kreye yon nouvo lis ak kle yo sèlman, epi yon lòt ak valè yo sèlman
diksyone = { 'nom': 'Simy', 'prenom' :'Lynne', 'lekol': 'ESIH'}
lisKle = list(diksyone.keys())
lisVale = list(diksyone.values())
print(f"Nan diksyone sa, kle yo se {lisKle} epi vale yo se {lisVale} \n ")

#Reyini 3 lis ansanm, san okenn doublon
Denyelist= list(set(list1 + list2+ listSanDoublon1))
print(f"Denye lis la reyini 3 li ansanm. Vale yo se {Denyelist} \n")

