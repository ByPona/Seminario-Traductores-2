class Lexico(object):

    def __init__(self, cadena):
        self.cadena = cadena

    def evaluarcadena(self):   
        contador = 0
        cadena_resultado = ""
        entero_resultado = ""
        self.cadena = self.cadena + " "
        longitud = len(self.cadena)

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
                print(f"{entero_resultado:<20}{'Real':>6}")

            cadena_resultado = ""
            entero_resultado = ""
            if self.cadena[contador]==" ":
                contador=contador+1

        return ""
