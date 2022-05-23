import re
from clases import refer
list_ref = list()
globals()['cont']=''
globals()['prim']=0

class traduccion_sasm():
    def __init__(self):

        self.codigo = list()
        self.posicionvar = 4
        self.comienzo = 0
        self.cantidadparametros = 0
    def primer_trad(self, bandera, code):
        self.bandera = bandera
        self.code = code


        if self.bandera == 6:
            self.codigo.append(str(self.code)+': db 0')

        if self.bandera == 10 or self.bandera == 12:
            if globals()['prim']==0:
                self.codigo.append('section .text \n')
                self.codigo.append('global '+str(self.code)+'\n')
                self.codigo.append('\n'+str(self.code)+':' + '\n \t'  +'PUSH rbp \n\t' + 'MOV rbp, rsp \n\t' 'SUB rsp, 48 \n\t')
                globals()['prim']=1
            else:
                patron = re.compile("[global]+")
                for n in range(len(self.codigo)):
                    if patron.match(self.codigo[n]) != None:

                        self.codigo[n] = self.codigo[n] + ', ' + str(self.code) 
                        break
                        
                    else:
                        pass
                self.codigo.append('\n'+str(self.code)+':' + '\n \t'  +'PUSH rbp \n\t' + 'MOV rbp, rsp \n\t' 'SUB rsp, 48 \n\t')
            globals()['cont']= self.code   

    def segundo_trad(self, bandera, valor, var):
        self.bandera = bandera
        self.valor = valor
        self.var = var
        bandera = 0
        posicionaux =0
        if self.bandera == 21:

            for n in list_ref:
                if self.var == n.var and n.contexto == globals()['cont']:
                    bandera = 1
                    posicionaux = n.pos
                    break
                else:
                    bandera = 0
            if bandera ==1:
                self.codigo.append('\tMOV WORD [rbp -' + str(posicionaux)+'] , '+str(self.valor)+'\n')
            elif bandera == 0:
                self.codigo.append('\tMOV WORD [rbp -' + str(self.posicionvar)+'] , '+str(self.valor)+'\n')
                list_ref.append(refer(self.var, globals()['cont'], self.posicionvar))
                self.posicionvar +=4
        if self.bandera == 22:

            for n in list_ref:
                if n.var == self.valor:

                    self.codigo.append('\tMOV rax, QWORD [rbp -' + str(n.pos)+']\n')
                    break
            self.codigo.append('\tMOV QWORD [rbp -' + str(self.posicionvar)+'] , rax \n\t')
            list_ref.append(refer(self.var, globals()['cont'], self.posicionvar))

        if self.bandera == 23:

            self.codigo.append('\tMOV WORD [rbp -' + str(self.posicionvar)+'] , '+str(self.valor))
            list_ref.append(refer(self.var, globals()['cont'], self.posicionvar))
            self.posicionvar +=4

    def op_ret_trad(self, bandera, variables, contexto, num):
        self.bandera = bandera
        self.variables = variables
        self.contexto = contexto
        self.partederecha = num
        i =0
        contador = 0
        vuelta = 0
        bandera = 0
        banderarealizada = 0
        cad = 'MOV rax, '
        cad2 = 'MOV rdi, '
        banderadigito =0
        while contador < self.partederecha:
            for obj in self.variables:
                
                for obj2 in list_ref:
                    if obj.cad == obj2.var and obj.contexto == obj2.contexto and obj.contexto == globals()['cont'] or obj.cad.isdigit() and banderadigito==0:
                        if vuelta == 0:
                            if bandera ==0:
                                if obj.cad.isdigit():
                                    cad = cad + ''+obj.cad
                                    banderadigito=1
                                else:
                                    cad = cad + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.codigo.append('\t' + cad +'\n')
                            else:
                                if obj.cad.isdigit():
                                    cad2 = cad2 + ''+obj.cad
                                else:
                                    cad2 = cad2 + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.codigo.append('\t' + cad2+'\n')
                            i = 0
                            vuelta += 1
                            contador +=1
                            
                        else:
                            if bandera ==0:
                                if obj.cad.isdigit():
                                    cad2 = cad2 + ''+obj.cad
                                    
                                    
                                else:
                                    cad2 = cad2 + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.codigo.append('\t' + cad2+'\n')
                                vuelta += 1
                            else:
                                if self.bandera[0]=='+':
                                    self.codigo.append('\t'+'ADD rax, rdi'+'\n')
                                elif self.bandera[0]=='*':
                                    self.codigo.append('\t'+'MUL rax, rdi'+'\n')
                                self.bandera.pop(0)
                                banderarealizada= 1
                                vuelta -= 1
                                cad = 'MOV rax, '
                                cad2 = 'MOV rdi, '
                                cad2 = cad2 + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.codigo.append('\t' + cad2+'\n')
                                             
                            i = 0
                            
                            contador +=1

                        if (vuelta ==2 or contador >= self.partederecha):
                            try:
                                if self.bandera[0]=='+':
                                    self.codigo.append('\t'+'ADD rax, rdi'+'\n')
                                elif self.bandera[0]=='*':
                                    self.codigo.append('\t'+'MUL rax, rdi'+'\n')
                                self.bandera.pop(0)
                            except:
                                pass
                            
                            vuelta = 0
                            bandera = 1
                            cad = 'MOV rax, '
                            cad2 = 'MOV rdi, '
                            break
                    else:
                        i+1
                        banderadigito=0

    def op_trad(self, bandera, var1, variables, contexto, num):
        self.bandera = bandera
        self.var1 = var1
        self.variables = variables
        self.contexto = contexto
        self.partederecha = num
        i =0
        contador = 0
        vuelta = 0
        bandera = 0
        banderarealizada = 0
        cad = 'MOV rax, '
        cad2 = 'MOV rdi, '
        banderadigito =0
        while contador < self.partederecha:
            for obj in self.variables:
                
                for obj2 in list_ref:
                    if obj.cad == obj2.var and obj.contexto == obj2.contexto and obj.contexto == globals()['cont'] or obj.cad.isdigit() and banderadigito==0:
                        if vuelta == 0:
                            if bandera ==0:
                                if obj.cad.isdigit():
                                    cad = cad + ''+obj.cad
                                    banderadigito=1
                                else:
                                    cad = cad + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.codigo.append('\t' + cad +'\n')
                            else:
                                if obj.cad.isdigit():
                                    cad2 = cad2 + ''+obj.cad
                                else:
                                    cad2 = cad2 + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.codigo.append('\t' + cad2+'\n')
                            i = 0
                            vuelta += 1
                            contador +=1
                            
                        else:
                            if bandera ==0:
                                if obj.cad.isdigit():
                                    cad2 = cad2 + ''+obj.cad
                                    
                                    
                                else:
                                    cad2 = cad2 + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.codigo.append('\t' + cad2+'\n')
                                vuelta += 1
                            else:
                                if self.bandera[0]=='+':
                                    self.codigo.append('\t'+'ADD rax, rdi'+'\n')
                                elif self.bandera[0]=='*':
                                    self.codigo.append('\t'+'MUL rax, rdi'+'\n')
                                self.bandera.pop(0)
                                banderarealizada= 1
                                vuelta -= 1
                                cad = 'MOV rax, '
                                cad2 = 'MOV rdi, '
                                cad2 = cad2 + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.codigo.append('\t' + cad2+'\n')
                                             
                            i = 0
                            
                            contador +=1

                        if (vuelta ==2 or contador >= self.partederecha):
                            try:
                                if self.bandera[0]=='+':
                                    self.codigo.append('\t'+'ADD rax, rdi'+'\n')
                                elif self.bandera[0]=='*':
                                    self.codigo.append('\t'+'MUL rax, rdi'+'\n')
                                self.bandera.pop(0)
                            except:
                                pass
                            
                            vuelta = 0
                            bandera = 1
                            cad = 'MOV rax, '
                            cad2 = 'MOV rdi, '
                            break
                    else:
                        i+1
                        banderadigito=0

        for obj in list_ref:
            if self.var1 == obj.var and self.contexto == obj.contexto:
                self.codigo.append('\t''MOV QWORD [rbp -'+ str(obj.pos)+'], ' + 'rax\n')

    def parametros(self, cantidad, nombre):
        self.cantidad = cantidad
        self.nombre = nombre
        i =0
        if self.comienzo == 0:
            self.comienzo = self.posicionvar +20
        else:
            self.comienzo = self.comienzo
        while i < cantidad:
            self.codigo.append('MOV QWORD [rbp -' +str(self.comienzo)+'], rdi \n')
            list_ref.append(refer(self.nombre, globals()['cont'], self.comienzo))
            i+=1
            self.comienzo+=4


    def func_trad(self):
        if globals()['cont']=='main':
            self.codigo.append('\n\t' 'ADD rsp, 48 \n\t'+ 'MOV rsp, rbp \n\t' +'MOV rax, 60 \n\t'+'MOV rdi, 0 \n\t' + 'syscall \n\t')
        else:
            self.codigo.append('\n\t' 'ADD rsp, 48 \n\t'+ 'MOV rsp, rbp \n\t' +'POP rbp \n\t' + 'ret \n\t')
        self.posicionvar = 4
        self.comienzo = 0

    def trad_ret(self, cad, contexto):
        self.cad = cad
        self.contexto = contexto
        for obj in list_ref:
            if self.cad == obj.var and self.contexto == obj.contexto:
                self.codigo.append('MOV rax, QWORD [rbp -'+ str(obj.pos)+']\n')

    def call_func(self, enviados, llamado, nombre):
        self.enviados = enviados
        self.llamado = llamado
        self.nombre = nombre
        for obj in list_ref:
            if self.enviados == obj.var and globals()['cont'] == obj.contexto:
                self.codigo.append('\t''MOV rax, QWORD [rbp -'+ str(obj.pos)+']\n')
        self.codigo.append('\t''MOV rdi, rax')
        self.codigo.append('\n\t''call '+ str(nombre))
        for obj in list_ref:
            if self.llamado == obj.var and globals()['cont'] == obj.contexto:
                self.codigo.append('\n\t''MOV QWORD [rbp -'+ str(obj.pos)+'], rax\n\t')
    
    def call_funcnum(self, enviados, llamado, nombre):
        self.enviados = enviados
        self.llamado = llamado
        self.nombre = nombre
        vuelta = 0
        for obj in self.enviados:
            self.codigo.append('\t''MOV ax,' +str(obj.cad)+ '\n')
            if vuelta == 0:
                
                self.codigo.append('\t''MOV rdi, rax')
                vuelta+=1
            elif vuelta ==1:
                self.codigo.append('\t''MOV rsi, rax')
        
        self.codigo.append('\n\t''call '+ str(nombre))
        for obj in list_ref:
            if self.llamado == obj.var and globals()['cont'] == obj.contexto:
                self.codigo.append('\n\t''MOV QWORD [rbp -'+ str(obj.pos)+'], rax\n\t')
     
    def print_func(self, valor):
        for obj in list_ref:
            if obj.var == valor and globals()['cont'] == obj.contexto:
                self.codigo.insert(0, 'section .data  \n\tprimr: db  "La impresion es := %lf",10,0 \nsection .bss \n\tresp: resq 2\n')
                self.codigo.insert(2, '\nextern printf\n')
                self.codigo.append('\n\tPUSH qword[rbp -'+str(obj.pos)+']')
                self.codigo.append('\n\tFILD dword[rsp]')
                self.codigo.append('\n\tFSTP qword[rel resp]')
                self.codigo.append('\n\tADD rsp, 8')
                self.codigo.append('\n\tMOVSD xmm0,qword[rel resp]')
                self.codigo.append('\n\tMOV rdi, primr')
                self.codigo.append('\n\tMOV al, 1')
                self.codigo.append('\n\tcall printf WRT ..plt \n\t')

    def gettraduccion(self):
        for obj in self.codigo:
            print(obj)
        Archivo=open("prueba.asm","w")
        for i in range(len(self.codigo)):
            Archivo.write(self.codigo[i])   
        del self.codigo[:]
        Archivo.close()



    def __repr__(self):
        aux = ("Variable: "+str(self.var)+ " Contexto: "+str(self.contexto)+ " Pos: "+str(self.pos))
        return aux
