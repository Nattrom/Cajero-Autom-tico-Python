saldo = 1000
pin_correcto = "1234"
intentos = 3

# Autenticación
while intentos > 0:
    pin = input("Ingrese su PIN: ")

    if pin == pin_correcto:
        print("Acceso concedido\n")
        break
    else:
        intentos -= 1
        print("PIN incorrecto. Intentos restantes:", intentos)

if intentos == 0:
    print("Tarjeta bloqueada")
    exit()

# Menú del cajero
while True:

    print("\n--- CAJERO AUTOMÁTICO ---")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    # Consultar saldo
    if opcion == "1":
        print("Su saldo actual es:", saldo)

    # Retirar dinero
    elif opcion == "2":
        retiro = float(input("Ingrese monto a retirar: "))

        if retiro <= 0:
            print("Monto inválido")
        elif retiro > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= retiro
            print("Retiro exitoso")
            print("Nuevo saldo:", saldo)

    # Depositar dinero
    elif opcion == "3":
        deposito = float(input("Ingrese monto a depositar: "))

        if deposito <= 0:
            print("Monto inválido")
        else:
            saldo += deposito
            print("Depósito exitoso")
            print("Nuevo saldo:", saldo)

    # Salir 
    elif opcion == "4":
        print("Gracias por usar el cajero automático")
        break

    else:
        print("Opción inválida. Intente nuevamente.")