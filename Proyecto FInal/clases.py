class Variables:
    def __init__(self, cad, contexto):
        self.cad = cad
        self.contexto = contexto
    def __repr__(self):
        objeto = ("Variable: "+str(self.cad)+" Contexto: "+str(self.context))
        return objeto

class Retorno:
    def __init__(self, cad, tipo, context):
        self.cad = cad
        self.tipo = tipo
        self.context = context
    def __repr__(self):
        objeto = ("Valor/Variable: "+str(self.cad)+ " Tipo: "+str(self.tipo)+ " Contexto: "+str(self.context))
        return objeto
        
class Nodo:
    def __init__(self, data):
        self.data = data
        self.contadordefinicion =0

class Seg_Parametros(Nodo):
    def __init__(self, data, id, tipo):
        Nodo.__init__(self, data)
        self.id = id
        self.tipo = tipo
    def __repr__(self):
        objeto = ('Parametros' '\n'+ ' Tipo: '+str(self.data)+' Id: '+str(self.id) + ' Funcion: ' + str(self.tipo))
        return objeto

class Regla:
    def __init__(self, aux, num, elementos, regla):
        self.aux = aux
        self.num = num
        self.elementos = elementos
        self.regla = regla


class Plantilla_Pila:
    def __init__(self, cadena, tipo, pos):
        self.cad = cadena
        self.tipo = tipo
        self.pos = pos

    def __repr__(self):
        return str(self.__dict__)

class Terminal(Plantilla_Pila):
    def __init__(self, cadena, tipo, pos):
        Plantilla_Pila.__init__(self, cadena, tipo, pos)

class No_Terminal(Plantilla_Pila):
    def __init__(self, cadena, tipo, pos):
        Plantilla_Pila.__init__(self, cadena, tipo, pos)

class Estado(Plantilla_Pila):
    def __init__(self, cadena, tipo, pos, estado):
        Plantilla_Pila.__init__(self, cadena, tipo, pos)
        self.estado = estado

class refer():
    def __init__(self, var, contexto, pos):
        self.var = var
        self.contexto = contexto
        self.pos = pos