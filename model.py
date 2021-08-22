import re #paquete para el uso de expresiones regulares

class Model:

    def __init__(self):
        self.emailRegex = r'([a-zA-Z0-9._-]+)@([\w]+)\.([a-zA-Z])+'
        self.enteroRegex = r'^[+-]?[0-9]+$'
        self.realRegex = r'^[+-]?[\d]+\.?([\d]*$)'
        self.notacionCientificaRegex = r'^[+-]?[0-9]*\.?[0-9]+([eE][+-]?[0-9]+)'

    def verifyEmail(self, value):
        if(re.search(self.emailRegex, value)):
            return 'Correo electronico valido'
        else:
            return 'Correo electronico invalido'

    def verifyEntero(self, value):
        if(re.search(self.enteroRegex, value)):
            return 'Numero entero valido'
        else:
            return 'Numero entero invalido'
    
    def verifyReal(self, value):
        if(re.search(self.realRegex, value)):
            return 'Numero real valido'
        else:
            return 'Numero real invalido'

    def verifyNotacionCientifica(self, value):
        if(re.search(self.notacionCientificaRegex, value)):
            return 'Numero en notación cientifica valido'
        else:
            return 'Numero en notación cientifica invalido'