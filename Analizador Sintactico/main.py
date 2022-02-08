from analizador import Sintactico

def formula1():
    prueba = input("Dame la cadena: ")

    entrada = list()
    cadena = Sintactico(prueba)
    entrada = cadena.evaluarcadena()

    entrada.append("$")

    pila = list()
    pila.append("$0")

    salida = list()

    contador = 0
    d = 2
    dstr = ""

    #Metodo evaluar 
    for n in entrada:
        if n.isalpha() == True:
            pila.append(n)
            pila.append(d)
            dstr = str(d)
            salida.append("d"+dstr)
            d = d+1
            contador = 1
    
        elif contador == 1:
            if n == "+":
                pila.append(n)
                pila.append(d)
                dstr = str(d)
                salida.append("d"+dstr)
                d = d+1
                contador = 0
            elif n == "$":
                salida.append("r1")
    
    if len(pila) == 7:
        print("Valido")

    else:
        print("Invalido")

def formula2():
    prueba = input("Dame la cadena: ")


    entrada = list()
    cadena = Sintactico(prueba)
    entrada = cadena.evaluarcadena()

    entrada.append("$")

    pila = list()
    pila.append("$0")

    salida = list()

    contador = 0
    d = 2
    dstr = ""

    #Metodo evaluar 
    for n in entrada:
        if n.isalpha() == True:
            pila.append(n)
            pila.append("2")
            salida.append("d2")
            contador = 1
    
        elif contador == 1:
            if n == "+":
                pila.append(n)
                pila.append("3")
                salida.append("d3")
                contador = 0
            elif n == "$":
                salida.append("r2")

    if pila[-1] == "3":
        print("Invalido")

    else:
        print("Valido")

        
#Funcion Principal
opc = int(input("Elige la formula a usar: \n(1) id+id \n(2) id+r1|id\nOpcion: "))

if opc == 1:
    formula1()

else:
    formula2()

