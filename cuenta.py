class Cuenta:
     
     def __init__(self,pin,saldo_inicial):
       self.__pin = pin
       self.__saldo=saldo_inicial

     def verificar_pin(self, pin_ingresado): 
         return self.__pin== pin_ingresado
     
     def obtener_saldo(self):
         return self.__saldo

     def modificar_saldo(self, nuevo_saldo):
         if nuevo_saldo>=0:
             self.__saldo=nuevo_saldo
