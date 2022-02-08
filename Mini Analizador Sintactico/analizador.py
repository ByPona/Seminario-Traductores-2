class Sintactico(object):

    def __init__(self, cadena):
        self.cadena = cadena

    def evaluarcadena(self):   
        contador = 0
        cadena_resultado = ""
        entero_resultado = ""
        self.cadena = self.cadena + " "
        longitud = len(self.cadena)
        lista = list()

        while contador<longitud:

            if self.cadena[contador].isalpha() == True:
                while self.cadena[contador].isalpha() == True:
                    cadena_resultado = cadena_resultado + self.cadena[contador]
                    contador=contador+1
                lista.append(cadena_resultado)
                
            elif self.cadena[contador] == "+":
                contador=contador+1
                lista.append("+")

            cadena_resultado = ""

            if self.cadena[contador]==" ":
                contador=contador+1

        return lista