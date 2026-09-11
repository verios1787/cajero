class Cajero:
    
    def __init__(self,pin,saldo):
        self.pin=pin
        self.saldo=saldo     
        
    def validar_pin(self,pin_ingresado: int):      
        return pin_ingresado == self.pin
                       
        
    def extraer_dinero(self,monto):
        if monto <= 0:
            return "El monto debe ser mayor a 0"
        if monto > self.saldo:
            return "Saldo insuficiente"
        
        self.saldo -= monto
        
        return f"Extracción realizada, retiraste ${monto}"

    def consultar_saldo(self):
        return self.saldo