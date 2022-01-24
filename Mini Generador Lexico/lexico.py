class Lexico(object):

    def __init__(self, cadena):
        self.cadena = cadena

    def evaluarcadena(self):   
        contador = 0
        cadena_resultado = ""
        entero_resultado = ""
        simbolo_resultado = ""
        self.cadena = self.cadena + " "
        longitud = len(self.cadena)
        longitud = longitud

        while contador<longitud:
            if self.cadena[contador].isalpha() == True:
                while self.cadena[contador]!=" ":
                    #print(self.cadena[contador])
                    cadena_resultado = cadena_resultado + self.cadena[contador]
                    contador=contador+1
                    #print(contador)
                print(f"{cadena_resultado:<20}{'Identificador':>15}")
                

            elif self.cadena[contador].isdigit() == True:
                while self.cadena[contador]!=" ":
                    entero_resultado = entero_resultado + self.cadena[contador]
                    contador=contador+1
                print(f"{entero_resultado:<20}{'Numero':>8}")

            else:
                simbolo_resultado = self.cadena[contador]
                print(f"{simbolo_resultado:<20}{'Simbolo':>9}")
                contador=contador+1

            cadena_resultado = ""
            entero_resultado = ""
            simbolo_resultado = ""
            if self.cadena[contador]==" ":
                contador=contador+1

            #print(contador)
            #print(longitud)
        return ""