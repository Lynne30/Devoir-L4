#1
chenn = "Mwen Renmen Lanati"
print(chenn.lower())


print(chenn.split())

majiskil =print(chenn.title())

var_rekipere = chenn.split()
for i in var_rekipere :
    print (i[0])

for i in chenn : 
    if i=="a":
        print ("@")
    else :
        print (i,end="")  

chenn2 = "AYITICHERI"
chenn2=chenn2[::-1]
print (chenn2.upper())

chenn3= "Kanal la pap kanpe"
print (chenn3.index("a"))

Totala =0
for i in range(len(chenn3)) :
    if chenn3[i]== "a" or chenn[i]=="A":
        Totala +=i 
print(Totala)

list1= []
for i in range(len(chenn3)):
    if chenn3[i] == "a":
        list1.append(i)
print(list1)

chenn3=chenn3.replace(" ", "")
print(chenn3)
