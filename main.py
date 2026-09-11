from cajero import *

cajero = Cajero(1234,100000)

intentos_restantes=3
acceso_concedido= False

while intentos_restantes > 0:
    try:
        pin =int(input(f"Ingrese su pin (intentos restantes:{intentos_restantes}): "))
    except ValueError:
        print ("Error: el pin debe ser un numero entero. ") 
        intentos_restantes -=1
        continue
    
    if cajero.validar_pin(pin):
        print("n¡Ingreso exitoso!")
        acceso_concedido=True
        break
    else:
        intentos_restantes-=1
        if intentos_restantes > 0:
            print("PIN incorrecto. intente de nuevo. ")
        else:
            print("PIN incorrecto. Acceso denegado. ")

if acceso_concedido: 
    
    while True:
         print("\nCajero Automático")
         print("1- Extraer Dinero")
         print("2- Consultar Saldo")
         print("3- Salir")

         try:
            opcion = int(input("seleccione una opcion: "))
         except ValueError:
            print("Error debe ingresar un nuemro válido, ")    
            continue

    
         if opcion == 1:
            monto = float(input("Ingrese el monto a extraer: "))
            resultado = cajero.extraer_dinero(monto)
            print(resultado)
            print(f"Saldo disponible:$ {cajero.consultar_saldo()}")
        
         if opcion == 2:
            print(f"Saldo disponible:$ {cajero.consultar_saldo()}")
    
         if opcion == 3:
             print("Gracias por venir retire su tarjeta")
         break
    

