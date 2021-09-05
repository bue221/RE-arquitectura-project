#automatas
from real import Real 
from entero import Entero
from notacion import Notacion
from mail import Email

class Model:

    def __init__(self):
        self.emailRegex = r'([a-zA-Z0-9._-]+)@([\w]+)\.([a-zA-Z])+'

    def verifyEmail(self, value):
        return Email().automataEmail(value)
        # if(re.search(self.emailRegex, value)):
        #     return 'Correo electronico valido'
        # else:
        #     return 'Correo electronico invalido'

    def verifyEntero(self, value):
          return Entero().automataEntero(value)
    
    def verifyReal(self, value):
        return Real().automataReal(value)

    def verifyNotacionCientifica(self, value):
        return Notacion().automataNotacion(value)