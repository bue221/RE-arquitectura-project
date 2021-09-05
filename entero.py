from identificar import Identificar_codigo_ascii as k

class Entero:

    def __init__(self):
        self.estado  = 0

    def automataEntero(self, texto):
        cadenaRechazada = False
        pos = 0
        while(not cadenaRechazada and pos < len(texto)):
            letra = ord(texto[pos])

            #inicio
            if(self.estado == 0):
                #si es digito
                if(k.es_digito(letra)):
                    self.estado = 3
                #si es un +
                elif(letra == 43):
                    self.estado = 1
                #si es un -
                elif(letra == 45):
                    self.estado = 2
                else:
                    cadenaRechazada = True
            #+
            if(self.estado == 1):
                if(k.es_digito(letra)):
                    self.estado = 3
                else:
                    self.estado = 0
            #-
            if(self.estado == 2):
                if(k.es_digito(letra)):
                    self.estado = 3
                else:
                    self.estado = 0
            #digito+
            if(self.estado == 3):
                if(k.es_digito(letra)):
                    self.estado = 3
                else:
                    cadenaRechazada = True

            pos = pos + 1

        if(cadenaRechazada):
            return 'Numero invalido'

        if(self.estado == 3):
            return 'Numero entero valido'
       
             