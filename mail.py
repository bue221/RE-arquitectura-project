from identificar import Identificar_codigo_ascii as k

class  Email:

    def __init__(self):
        self.estado = 0

    def automataEmail(self, texto):
        cadenaRechazada = False
        pos = 0
        while(not cadenaRechazada and pos < len(texto)):
            letra = ord(texto[pos])

            #inicio
            if(self.estado == 0):
                if(k.es_letra(letra)):
                    self.estado = 1
                else:
                    cadenaRechazada = True
            if(self.estado == 1):
                if(k.es_digito(letra)):
                    self.estado = 2
                if(k.es_letra(letra)):
                    self.estado = 3
                if(k.es_arroba(letra)):
                    self.estado = 4
            if(self.estado == 2):
                if(k.es_digito(letra)):
                    self.estado = 2
                if(k.es_letra(letra)):
                    self.estado = 3
                if(k.es_arroba(letra)):
                    self.estado = 4
            if(self.estado == 3):
                if(k.es_arroba(letra)):
                    self.estado = 4
                if(k.es_digito(letra)):
                    self.estado = 2
            if(self.estado == 4):
                if(k.es_letra(letra)):
                    self.estado = 4
                if(k.es_letra(letra)):
                    self.estado = 5
            if(self.estado == 5):
                if(k.es_letra(letra)):
                    self.estado = 6
                if(k.es_digito(letra)):
                    self.estado = 7
                if(k.es_punto(letra)):
                    self.estado = 8
            if(self.estado == 6):
                if(k.es_letra(letra)):
                    self.estado = 6
                if(k.es_digito(letra)):
                    self.estado = 7
                if(k.es_punto(letra)):
                    self.estado = 8
            if(self.estado == 7):
                if(k.es_letra(letra)):
                    self.estado = 6
                if(k.es_digito(letra)):
                    self.estado = 7
            if(self.estado == 8):
                if(k.es_letra(letra)):
                    self.estado = 9
            if(self.estado == 9):
                if(k.es_letra(letra)):
                    self.estado = 10
            if(self.estado == 10):
                if(k.es_letra(letra)):
                    self.estado = 11
            if(self.estado == 11):
                if(k.es_punto(letra)):
                    self.estado = 12
            if(self.estado == 12):
                if(k.es_letra(letra)):
                    self.estado == 12

            pos = pos + 1

        if(cadenaRechazada):
            return 'Email invalido'

        if(self.estado == 12):
            return 'Email valido'
        
        return 'Email invalido'
        
        
