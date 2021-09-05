from identificar import Identificar_codigo_ascii as k

class Notacion:

    def __init__(self):
        self.estado  = 0

    def automataNotacion(self, texto):
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
                elif(letra == 46):
                    self.estado = 4
                elif(k.es_letra_E(letra)):
                    self.estado = 6
                else:
                    cadenaRechazada = True
            #.
            if(self.estado == 4):
                if(k.es_digito(letra)):
                    self.estado = 5
                # else:
                #     self.estado = 1
            #digito+
            if(self.estado == 5):
                if(k.es_digito(letra)):
                    self.estado = 5
                elif(k.es_letra_E(letra)):
                    self.estado = 6
                else:
                    cadenaRechazada = True
            if(self.estado == 6):
                #si es digito
                if(k.es_digito(letra)):
                    self.estado = 9
                #si es un +
                elif(letra == 43):
                    self.estado = 7
                #si es un -
                elif(letra == 45):
                    self.estado = 8
                # else:
                #     cadenaRechazada = True
            if(self.estado == 7):
                if(k.es_digito(letra)):
                    self.estado = 9
                else:
                    self.estado = 6
            if(self.estado == 8):
                if(k.es_digito(letra)):
                    self.estado = 9
                else:
                    self.estado = 6
            if(self.estado == 9):
                if(k.es_digito(letra)):
                    self.estado = 9
                else:
                    cadenaRechazada = True

            pos = pos + 1

        if(cadenaRechazada):
            return 'Numero en notación cientifica invalido'
        
        if(self.estado == 5 or self.estado == 3 or self.estado == 9):
            return 'Numero en notación cientifica valido'
       
          