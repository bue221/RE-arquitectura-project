#automatas
from real import Real 
from entero import Entero
from notacion import Notacion
from mail import Email

class Model:

    def __init__(self):
        pass

    def verifyEmail(self, value):
        return Email().automataEmail(value)

    def verifyEntero(self, value):
          return Entero().automataEntero(value)
    
    def verifyReal(self, value):
        return Real().automataReal(value)

    def verifyNotacionCientifica(self, value):
        return Notacion().automataNotacion(value)