class Lexico(object):

    def __init__(self, cadena):
        self.cadena = cadena

    def evaluarcadena(self):   
        contador = 0
        activador = 0
        catch = 0

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

        
        self.cadena = self.cadena + " "
        longitud = len(self.cadena)

        while contador<longitud:


            if self.cadena[contador].isalpha() == True:
                while self.cadena[contador]!=" ":
                    identificador_resultado = identificador_resultado + self.cadena[contador]
                    contador=contador+1
                #Se revisa el tipo
                if ("int" == identificador_resultado) or ("float" == identificador_resultado) or ("void" == identificador_resultado):
                    tipo_resultado = identificador_resultado
                    print(f"{tipo_resultado:<20}{'Tipo':>6}{'4':>17}")
                elif "if" == identificador_resultado:
                    if_resultado = identificador_resultado
                    print(f"{if_resultado:<20}{'Condicional':>13}{'19':>11}")
                elif "while" == identificador_resultado:
                    while_resultado = identificador_resultado
                    print(f"{while_resultado:<20}{'Ciclo':>7}{'20':>17}")
                elif "return" == identificador_resultado:
                    return_resultado = identificador_resultado
                    print(f"{return_resultado:<20}{'Retorno':>9}{'21':>15}")
                elif "else" == identificador_resultado:
                    else_resultado = identificador_resultado
                    print(f"{else_resultado:<20}{'Condicional':>13}{'22':>11}")       
                else:
                    print(f"{identificador_resultado:<20}{'Identificador':>15}{'0':>8}")
                

            elif self.cadena[contador].isdigit() == True:
                while self.cadena[contador]!=" ":
                    entero_resultado = entero_resultado + self.cadena[contador]
                    if self.cadena[contador] == ".":
                        activador = activador+1
                    contador=contador+1
                if activador == 1:
                    real_resultado = entero_resultado
                    print(f"{real_resultado:<20}{'Real':>6}{'2':>17}")
                else:
                    print(f"{entero_resultado:<20}{'Entero':>8}{'1':>15}")
            
            elif ("+" == self.cadena[contador]) or ("-" == self.cadena[contador]):
                opSuma_resultado = self.cadena[contador]
                contador = contador+1
                print(f"{opSuma_resultado:<20}{'opSuma':>8}{'5':>15}")
            
            elif ("*" == self.cadena[contador]) or ("/" == self.cadena[contador]):
                opMul_resultado = self.cadena[contador]
                contador = contador+1
                print(f"{opMul_resultado:<20}{'opMul':>7}{'6':>16}")

            elif ("<" == self.cadena[contador]) or (">" == self.cadena[contador]):
                opRelac_resultado = self.cadena[contador]
                contador = contador+1
                if "=" == self.cadena[contador]:
                    opRelac_resultado = opRelac_resultado + self.cadena[contador]
                    contador = contador+1
                print(f"{opRelac_resultado:<20}{'opRelac':>9}{'7':>14}")

            elif("|" == self.cadena[contador]) and ("|" == self.cadena[contador+1]):
                opOr_resultado = "||"
                contador = contador+2
                print(f"{opOr_resultado:<20}{'opOr':>6}{'8':>17}")

            elif("&" == self.cadena[contador]) and ("&" == self.cadena[contador+1]):
                opAnd_resultado = "&&"
                contador = contador+2
                print(f"{opAnd_resultado:<20}{'opAnd':>7}{'9':>16}")

            elif "!" == self.cadena[contador]:
                contador = contador+1
                if "=" == self.cadena[contador]:
                    opIgualdad_resultado = "!="
                    print(f"{opIgualdad_resultado:<20}{'opIgualdad':>12}{'11':>12}")
                    contador = contador+1
                else:
                    opNot_resultado = "!"
                    print(f"{opNot_resultado:<20}{'opNot':>7}{'10':>17}")

            elif "=" == self.cadena[contador]:
                contador = contador+1
                if "=" == self.cadena[contador]:
                    opIgualdad_resultado = "=="
                    print(f"{opIgualdad_resultado:<20}{'opIgualdad':>12}{'11':>12}")
                    contador = contador+1
                else:
                    igual_resultado = "="
                    print(f"{igual_resultado:<20}{'Igual':>7}{'18':>17}")

            elif("&" == self.cadena[contador]) and ("&" == self.cadena[contador+1]):
                opAnd_resultado = "&&"
                contador = contador+2
                print(f"{opAnd_resultado:<20}{'opAnd':>7}{'9':>16}")

            elif ";" == self.cadena[contador]:
                puntoycoma_resultado = ";"
                contador = contador+1
                print(f"{puntoycoma_resultado:<20}{'PuntoyComa':>12}{'12':>12}")

            elif "," == self.cadena[contador]:
                coma_resultado = ","
                contador = contador + 1
                print(f"{coma_resultado:<20}{'Coma':>6}{'13':>18}")
                
            elif "(" == self.cadena[contador]:
                parentesis_resultado = "("
                contador = contador + 1
                print(f"{parentesis_resultado:<20}{'Parentesis':>12}{'14':>12}")

            elif ")" == self.cadena[contador]:
                parentesis_resultado = ")"
                contador = contador + 1
                print(f"{parentesis_resultado:<20}{'Parentesis':>12}{'15':>12}")

            elif "{" == self.cadena[contador]:
                llaves_resultado = "{"
                contador = contador + 1
                print(f"{llaves_resultado:<20}{'Llaves':>8}{'16':>16}")

            elif "}" == self.cadena[contador]:
                llaves_resultado = "}"
                contador = contador + 1
                print(f"{llaves_resultado:<20}{'Llaves':>8}{'17':>16}")

            elif self.cadena[contador]==" ":
                contador=contador+1

            else:
                if "$" == self.cadena[contador]:
                    simbolo_resultado = self.cadena[contador]
                    print(f"{simbolo_resultado:<20}{'Simbolo':>9}{'23':>15}")
                    contador=contador+1
                else:
                    while catch<2:
                        if "'" == self.cadena[contador]:
                            catch = catch+1
                        elif '"' == self.cadena[contador]:
                            catch = catch+1
                        cadena_resultado = cadena_resultado + self.cadena[contador]
                        contador=contador+1
                    print(f"{cadena_resultado:<20}{'Cadena':>8}{'3':>16}")

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

        return ""
