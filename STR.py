#1Nan yon chenn karaktè, mete tout karaktè yo an miniskil
chenn = "Mwen Renmen Lanati"
print(chenn.lower())

#Nan yon chenn karaktè, koupe chenn nan tout kote ki gen espas. Epi afiche yon lis ki gen chak eleman yo.
print(chenn.split())

#Nan yon chenn karaktè, mete tout premye lèt chak mo an majiskil.
majiskil =print(chenn.title())

#Nan yon chenn karaktè, rekipere premye lèt chak mo. Epi afiche yon nouvo chenn ak tout inisyal sa yo.
var_rekipere = chenn.split()
for i in var_rekipere :
    print (i[0])

#Ranplase tout karaktè "a" ki nan yon chenn pa "@"
for i in chenn : 
    if i=="a":
        print ("@")
    else :
        print (i,end="")  
        
#Mete yon chenn karaktè devan dèyè, answit mete l an majiskil.
chenn2 = "AYITICHERI"
chenn2=chenn2[::-1]
print (chenn2.upper())

#Afiche endeks premye karaktè "a" ki nan yon chenn. 
chenn3= "Kanal la pap kanpe"
print (chenn3.index("a"))

#Afiche total tout endeks karaktè "a" ki nan yon chenn (Kit se a majiskil oubyen miniskil).
Totala =0
for i in range(len(chenn3)) :
    if chenn3[i]== "a" or chenn[i]=="A":
        Totala +=i 
print(Totala)


#Kreye yon lis ki gen endeks tout karaktè "a" ki nan yon chenn (Sèlman a miniskil). 
list1= []
for i in range(len(chenn3)):
    if chenn3[i] == "a":
        list1.append(i)
print(list1)

#Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen (Pa kontwole espas yo).
chenn3=chenn3.replace(" ", "")
print(chenn3)
