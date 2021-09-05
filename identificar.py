class Identificar_codigo_ascii:
    
    def __init__(self):
        pass

    def es_letra(letra):
        if((letra >= 65 and letra <=90) or (letra >= 97 and letra <=122)):
            return True
        return False

    def es_digito(letra):
        if((letra >= 48 and letra <=57)):
            return True
        return False
    
    def es_punto(letra):
        if((letra == 46)):
            return True
        return False

    def es_letra_E(letra):
        if((letra == 69) or (letra == 101)):
            return True
        return False

    def es_arroba(letra):
        if((letra == 64)):
            return True
        return False
        