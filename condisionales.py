
Frutas=["apple","Bananas", "cherrys","grapes"]
edad=int(input("entre su edad:  "))
if edad >=18 :
    print("Eres mayor de edad")
    for x in range(6,30,5):
        for y in Frutas:
            print(x,y)
else: 
    print("Eres menor de edad")
    i = 1
    while i < edad:
        print(i)
        i += 1