#Questo programma genera tutte le combinazioni possibili
import os, time
listaCaratteri = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ".", ",", "-", "_", "@", "+",":","/","\",","!","£","$","%","&","1","2","3","4","5","6","7","8","9","0"]
def testaPassword(password):
    print(password)
    with open(file, "a") as o:
         o.write(password)
         o.write("""
""")


def carattere1():
    for c1 in listaCaratteri:
       psw = c1
       testaPassword(psw)

def carattere2():
    for c1 in listaCaratteri:
       psw = c1
       for c2 in listaCaratteri:
          psw = c1+c2
          testaPassword(psw)

def carattere3():
    for c1 in listaCaratteri:
     psw = c1
     for c2 in listaCaratteri:
           for c3 in listaCaratteri:
               psw = c1+c2+c3  
               testaPassword(psw)

def carattere4():
    for c1 in listaCaratteri:
     psw = c1
     for c2 in listaCaratteri:
           for c3 in listaCaratteri:
              for c4 in listaCaratteri:
                psw = c1+c2+c3+c4   
                testaPassword(psw)

def carattere5():
    for c1 in listaCaratteri:
     psw = c1
     for c2 in listaCaratteri:
           for c3 in listaCaratteri:
              for c4 in listaCaratteri:
                for c5 in listaCaratteri:
                    psw = c1+c2+c3+c4+c5
                    testaPassword(psw)

def carattere6():
    for c1 in listaCaratteri:
     psw = c1
     for c2 in listaCaratteri:
           for c3 in listaCaratteri:
              for c4 in listaCaratteri:
                for c5 in listaCaratteri:
                    for c6 in listaCaratteri:
                        psw = c1+c2+c3+c4+c5+c6
                        testaPassword(psw)

def carattere7():
    for c1 in listaCaratteri:
     psw = c1
     for c2 in listaCaratteri:
           for c3 in listaCaratteri:
              for c4 in listaCaratteri:
                for c5 in listaCaratteri:
                    for c6 in listaCaratteri:
                        for c7 in listaCaratteri:
                            psw = c1+c2+c3+c4+c5+c6+c7
                            testaPassword(psw)

def carattere8():
    for c1 in listaCaratteri:
     psw = c1
     for c2 in listaCaratteri:
           for c3 in listaCaratteri:
              for c4 in listaCaratteri:
                for c5 in listaCaratteri:
                    for c6 in listaCaratteri:
                        for c7 in listaCaratteri:
                            for c8 in listaCaratteri:
                                psw = c1+c2+c3+c4+c5+c6+c7+c8
                                testaPassword(psw)

def carattere9():

    for c1 in listaCaratteri:
     psw = c1
     for c2 in listaCaratteri:
           for c3 in listaCaratteri:
              for c4 in listaCaratteri:
                for c5 in listaCaratteri:
                    for c6 in listaCaratteri:
                        for c7 in listaCaratteri:
                            for c8 in listaCaratteri:
                                for c9 in listaCaratteri:
                                    psw = c1+c2+c3+c4+c5+c6+c7+c8+c9
                                    testaPassword(psw)

def carattere10():
    for c1 in listaCaratteri:
     psw = c1
     for c2 in listaCaratteri:
           for c3 in listaCaratteri:
              for c4 in listaCaratteri:
                for c5 in listaCaratteri:
                    for c6 in listaCaratteri:
                        for c7 in listaCaratteri:
                            for c8 in listaCaratteri:
                                for c9 in listaCaratteri:
                                    for c10 in listaCaratteri:
                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10
                                        testaPassword(psw)

dom = input("Da quanti caratteri deve essere composta la password?:")
file = input("In che file vuoi salvare le password? ")
print("Le password verranno scitte qui sotto e nel file->", file )

time.sleep(2)
#####################
if dom == "1":
    carattere1()

elif dom == "2":
    carattere2()

elif dom == "3":
    carattere3()

elif dom == "4":
    carattere4()

elif dom == "5":
    carattere5()

elif dom == "6":
    carattere6()

elif dom == "7":
    carattere7()

elif dom == "8":
    carattere8()

elif dom == "9":
    carattere9()

elif dom == "10":
    carattere10()  

elif dom == "1-2":
    carattere1()
    carattere2()

elif dom == "1-2-3":
    carattere1()
    carattere2()
    carattere3()

elif dom == "1-2-3-4":
    carattere1()
    carattere2()
    carattere3()
    carattere4()

elif dom == "1-2-3-4-5":
    carattere1()
    carattere2()
    carattere3()
    carattere4()
    carattere5()

elif dom == "1-2-3-4-5-6":
    carattere1()
    carattere2()
    carattere3()
    carattere4()
    carattere5()
    carattere6()

elif dom == "1-2-3-4-5-6-7":
    carattere1()
    carattere2()
    carattere3()
    carattere4()
    carattere5()
    carattere6()
    carattere7()

elif dom == "1-2-3-4-5-6-7-8":
    carattere1()
    carattere2()
    carattere3()
    carattere4()
    carattere5()
    carattere6()
    carattere7()
    carattere8()

elif dom == "1-2-3-4-5-6-7-8-9":
    carattere1()
    carattere2()
    carattere3()
    carattere4()
    carattere5()
    carattere6()
    carattere7()
    carattere8()
    carattere9()

elif dom == "1-2-3-4-5-6-7-8-9-10":
    carattere1()
    carattere2()
    carattere3()
    carattere4()
    carattere5()
    carattere6()
    carattere7()
    carattere8()
    carattere9()
    carattere10()
