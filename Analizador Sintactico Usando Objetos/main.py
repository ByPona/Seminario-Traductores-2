class Terminal(object):
    def __init__(self, cadena, id):
        self.cadena = cadena
        self.id = id

    def __str__(self):
        return "%s - %s" % (self.cadena, self.id)

    def darcadena(self):
        return self.cadena

    def darid(self):
        return self.id

class NoTerminales(object):
    def __init__(self, simbolo, regla):
        self.simbolo = simbolo
        self.regla = regla

    def __str__(self):
        return "%s - %s" % (self.simbolo, self.regla)

class Estado(object):
    def __init__(self, estado):
        self.estado = estado

    def __str__(self):
        return "%s" % (self.estado)

cadena = input("Dame la cadena a analizar: ")


contador = 0
activador = 0
catch = 0
lista = list()

identificador_resultado = ""
entero_resultado = ""
simbolo_resultado = ""
real_resultado = ""
cadena_resultado = ""
tipo_resultado = ""

opSuma_resultado = ""
opMul_resultado = ""
opRelac_resultado = ""
opOr_resultado = ""
opAnd_resultado = ""
opNot_resultado = ""
opIgualdad_resultado = ""

puntoycoma_resultado = ""
coma_resultado = ""
parentesis_resultado = ""
llaves_resultado = ""
igual_resultado = ""

if_resultado = ""
while_resultado = ""
return_resultado = ""
else_resultado = ""
pesos_resultado = ""

cadena_resultado = ""

        
cadena = cadena + " "
longitud = len( cadena)
longitud = longitud

while contador<longitud:


    if  cadena[contador].isalpha() == True:
        while cadena[contador].isalpha() == True or cadena[contador].isdigit() == True:
            identificador_resultado = identificador_resultado +  cadena[contador]
            contador=contador+1
        #Se revisa el tipo
        if ("int" == identificador_resultado) or ("float" == identificador_resultado) or ("void" == identificador_resultado):
            tipo_resultado = identificador_resultado
            #print(f"{tipo_resultado:<20}{'Tipo':>6}{'4':>17}")
            objeto = Terminal(tipo_resultado, "4")
            lista.append(objeto)
        elif "if" == identificador_resultado:
            if_resultado = identificador_resultado
            #print(f"{if_resultado:<20}{'Condicional':>13}{'19':>11}")
            objeto = Terminal(if_resultado, "19")
            lista.append(objeto)
        elif "while" == identificador_resultado:
            while_resultado = identificador_resultado
            #print(f"{while_resultado:<20}{'Ciclo':>7}{'20':>17}")
            objeto = Terminal(while_resultado, "20")
            lista.append(objeto)
        elif "return" == identificador_resultado:
            return_resultado = identificador_resultado
            #print(f"{return_resultado:<20}{'Retorno':>9}{'21':>15}")
            objeto = Terminal(return_resultado, "21")
            lista.append(objeto)
        elif "else" == identificador_resultado:
            else_resultado = identificador_resultado
            #print(f"{else_resultado:<20}{'Condicional':>13}{'22':>11}")   
            objeto = Terminal(else_resultado, "22")
            lista.append(objeto)    
        else:
            #print(f"{identificador_resultado:<20}{'Identificador':>15}{'0':>8}")
            objeto = Terminal(identificador_resultado, "0")
            lista.append(objeto)
                

    elif cadena[contador].isdigit() == True:
        while cadena[contador].isdigit() == True or cadena[contador] == ".":
            entero_resultado = entero_resultado +  cadena[contador]
            if  cadena[contador] == ".":
                activador = activador+1
                contador=contador+1
        if activador == 1:
            real_resultado = entero_resultado
            #print(f"{real_resultado:<20}{'Real':>6}{'2':>17}")
            objeto = Terminal(real_resultado, "2")
            lista.append(objeto)
        else:
            #print(f"{entero_resultado:<20}{'Entero':>8}{'1':>15}")
            objeto = Terminal(entero_resultado, "1")
            lista.append(objeto)
            
    elif ("+" ==  cadena[contador]) or ("-" ==  cadena[contador]):
        opSuma_resultado =  cadena[contador]
        contador = contador+1
        #print(f"{opSuma_resultado:<20}{'opSuma':>8}{'5':>15}")
        objeto = Terminal(opSuma_resultado, "5")
        lista.append(objeto)
            
    elif ("*" ==  cadena[contador]) or ("/" ==  cadena[contador]):
        opMul_resultado =  cadena[contador]
        contador = contador+1
        #print(f"{opMul_resultado:<20}{'opMul':>7}{'6':>16}")
        objeto = Terminal(opMul_resultado, "6")
        lista.append(objeto)

    elif ("<" ==  cadena[contador]) or (">" ==  cadena[contador]):
        opRelac_resultado =  cadena[contador]
        contador = contador+1
        if "=" ==  cadena[contador]:
            opRelac_resultado = opRelac_resultado +  cadena[contador]
            contador = contador+1
        #print(f"{opRelac_resultado:<20}{'opRelac':>9}{'7':>14}")
        objeto = Terminal(opRelac_resultado, "7")
        lista.append(objeto)

    elif("|" ==  cadena[contador]) and ("|" ==  cadena[contador+1]):
        opOr_resultado = "||"
        contador = contador+2
        #print(f"{opOr_resultado:<20}{'opOr':>6}{'8':>17}")
        objeto = Terminal(opOr_resultado, "8")
        lista.append(objeto)

    elif("&" ==  cadena[contador]) and ("&" ==  cadena[contador+1]):
        opAnd_resultado = "&&"
        contador = contador+2
        #print(f"{opAnd_resultado:<20}{'opAnd':>7}{'9':>16}")
        objeto = Terminal(opAnd_resultado, "9")
        lista.append(objeto)

    elif "!" ==  cadena[contador]:
        contador = contador+1
        if "=" ==  cadena[contador]:
            opIgualdad_resultado = "!="
            #print(f"{opIgualdad_resultado:<20}{'opIgualdad':>12}{'11':>12}")
            objeto = Terminal(opIgualdad_resultado, "11")
            lista.append(objeto)
            contador = contador+1
        else:
            opNot_resultado = "!"
            #print(f"{opNot_resultado:<20}{'opNot':>7}{'10':>17}")
            objeto = Terminal(opNot_resultado, "10")
            lista.append(objeto)

    elif "=" ==  cadena[contador]:
        contador = contador+1
        if "=" ==  cadena[contador]:
            opIgualdad_resultado = "=="
            #print(f"{opIgualdad_resultado:<20}{'opIgualdad':>12}{'11':>12}")
            objeto = Terminal(opIgualdad_resultado, "11")
            lista.append(objeto)
            contador = contador+1
        else:
            igual_resultado = "="
            #print(f"{igual_resultado:<20}{'Igual':>7}{'18':>17}")
            objeto = Terminal(igual_resultado, "18")
            lista.append(objeto)

    elif("&" ==  cadena[contador]) and ("&" ==  cadena[contador+1]):
        opAnd_resultado = "&&"
        contador = contador+2
        #print(f"{opAnd_resultado:<20}{'opAnd':>7}{'9':>16}")
        objeto = Terminal(opAnd_resultado, "9")
        lista.append(objeto)

    elif ";" ==  cadena[contador]:
        puntoycoma_resultado = ";"
        contador = contador+1
        #print(f"{puntoycoma_resultado:<20}{'PuntoyComa':>12}{'12':>12}")
        objeto = Terminal(puntoycoma_resultado, "12")
        lista.append(objeto)

    elif "," ==  cadena[contador]:
        coma_resultado = ","
        contador = contador + 1
        #print(f"{coma_resultado:<20}{'Coma':>6}{'13':>18}")
        objeto = Terminal(coma_resultado, "13")
        lista.append(objeto)
                
    elif "(" ==  cadena[contador]:
        parentesis_resultado = "("
        contador = contador + 1
        #print(f"{parentesis_resultado:<20}{'Parentesis':>12}{'14':>12}")
        objeto = Terminal(parentesis_resultado, "14")
        lista.append(objeto)

    elif ")" ==  cadena[contador]:
        parentesis_resultado = ")"
        contador = contador + 1
        #print(f"{parentesis_resultado:<20}{'Parentesis':>12}{'15':>12}")
        objeto = Terminal(parentesis_resultado, "15")
        lista.append(objeto)

    elif "{" ==  cadena[contador]:
        llaves_resultado = "{"
        contador = contador + 1
        #print(f"{llaves_resultado:<20}{'Llaves':>8}{'16':>16}")
        objeto = Terminal(llaves_resultado, "16")
        lista.append(objeto)

    elif "}" ==  cadena[contador]:
        llaves_resultado = "}"
        contador = contador + 1
        #print(f"{llaves_resultado:<20}{'Llaves':>8}{'17':>16}")
        objeto = Terminal(llaves_resultado, "17")
        lista.append(objeto)

    elif  cadena[contador]==" ":
        contador=contador+1

    else:
        if "$" ==  cadena[contador]:
            simbolo_resultado =  cadena[contador]
            #print(f"{simbolo_resultado:<20}{'Simbolo':>9}{'23':>15}")
            objeto = Terminal(simbolo_resultado, "23")
            lista.append(objeto)
            contador=contador+1
        else:
            while catch<2:
                if "'" ==  cadena[contador]:
                    catch = catch+1
                elif '"' ==  cadena[contador]:
                    catch = catch+1
                cadena_resultado = cadena_resultado +  cadena[contador]
                contador=contador+1
            #print(f"{cadena_resultado:<20}{'Cadena':>8}{'3':>16}")
            objeto = Terminal(cadena_resultado, "3")
            lista.append(objeto)

    identificador_resultado = ""
    entero_resultado = ""
    simbolo_resultado = ""
    real_resultado = ""
    cadena_resultado = ""
    tipo_resultado = ""

    opSuma_resultado = ""
    opMul_resultado = ""
    opRelac_resultado = ""
    opOr_resultado = ""
    opAnd_resultado = ""
    opNot_resultado = ""
    opIgualdad_resultado = ""

    puntoycoma_resultado = ""
    coma_resultado = ""
    parentesis_resultado = ""
    llaves_resultado = ""
    igual_resultado = ""

    if_resultado = ""
    while_resultado = ""
    return_resultado = ""
    else_resultado = ""
    pesos_resultado = ""

    cadena_resultado = ""

objeto = Terminal("$", 23)
lista.append(objeto)

pila = list()
objeto = Terminal("$0", 500)
pila.append(objeto)

salida = list()

contador = 0
d = 2
dstr = ""

if len(lista) < 6:

    for n in lista:
        cadena = n.darcadena()
        if cadena[0].isalpha() == True or cadena[0].isdigit():
            pila.append(n)
            dstr = str(d)
            objeto = Terminal(d, 500)
            pila.append(objeto)
            dstr = "d" + dstr
            estado = Estado(dstr)
            salida.append(estado)
            d = d+1
            contador = 1

        elif contador == 1:
            if cadena == "+":
                pila.append(n)
                dstr = str(d)
                objeto = Terminal(d, 500)
                dstr = "d" + dstr
                estado = Estado(dstr)
                salida.append(estado)
                d = d+1
                contador = 0
            elif cadena == "$":
                estado = Estado("r1")
                salida.append(estado)


    if len(pila) == 6:
        estado = Estado("r0")
        salida.append(estado)
        pila = list()
        objeto = Terminal("$0", 500)
        pila.append(objeto)
        objeto = NoTerminales("E1", "id+id")
        pila.append(objeto)
        print("Valido")

    else:
        print("Invalido")

else:
    for n in lista:
        cadena = n.darcadena()
        if cadena[0].isalpha() == True or cadena[0].isdigit():
            pila.append(n)
            objeto = Terminal("2", 500)
            pila.append(objeto)
            estado = Estado("d2")
            salida.append(estado)
            contador = 1
        
        elif contador == 1:
            if cadena == "+":
                pila.append(n)
                objeto = Terminal("3", 500)
                pila.append(objeto)
                estado = Estado("d3")
                salida.append(estado)
                contador = 0
            elif cadena == "$":
                estado = Estado("r2")
                salida.append(estado)
    
    aux = pila[-1]
    aux2 = aux.darcadena()

    if aux2 == "3":
        print("Invalido")
    else:
        print("Valido")
        estado = Estado("r0")
        salida.append(estado)
        pila = list()
        objeto = Terminal("$0", 500)
        pila.append(objeto)
        objeto = NoTerminales("E1", "id+r1|id")
        pila.append(objeto)


