#Ou gen yon diksyonè. Rekipere tout valè yo, gras ak kle yo epi retounen yon lis valè.
Diksyonè = {}

while True: 
    kle=input ("Antre yo nouvo kle pou diksyone a oubyen tape 'q' pou w kite : \n")
    if kle.lower()== 'q':
        break
    valè = input("Antre vale pou kle a :".format(kle))
    Diksyonè[kle]= valè   
Kle = list(Diksyonè.keys())
Valè = list(Diksyonè.values())
print(f"Diksyonè a se {Diksyonè} \n")
 
#Mande itilizatè a, tape yon valè... epi verifye si l gen akolad devan ak dèyè.
valè2 = input("Rantre yon valè nan yon diksyonè")
if kle in Diksyonè:
    valè2 = Diksyonè[kle]
    if valè2.startswith("{") and valè2.endswith("}"):
        print(f"Valè a gen akolad devan ak deye {valè2} \n")
    else :
        print(f"Valè a gen akolad devan ak deye {valè2}\n")
else:
    print("Kle sapa nan diksyonè a \n")        




