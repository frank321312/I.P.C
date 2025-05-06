## Necesitamos escribir un programa de cobro en el supermercado. La función debe recibir un número entero que representa el monto a pagar y debe permitir al usuario que ingrese valores, hasta que el pago se haya realizado en su totalidad. Además, le debe ir indicando cuánto le queda por pagar. El programa no da vuelto.
## Hacer que el programa anterior dé vuelto si el monto ingresado es mayor al monto a pagar. Por ejemplo, si el monto a pagar es 500 y el usuario ingresa 600, el programa debe imprimir “Su vuelto es: 100” y “Pendientes: 0”.

def monto_a_pagar(monto):
    if (monto <= 0):
        print("El monto a pagar debe ser mayor a 0")
        return

    while (monto > 0):
        print(f"Su total a pagar es: {monto}")
        pago = int(input("Ingrese el monto a pagar: "))
        if (pago > 0):
            monto -= pago
            print(f"Faltan {monto} pesos por pagar")
        else:
            print("El monto a pagar debe ser mayor a 0")
    
    if (monto == 0):
        print("Pendientes: 0. Gracias por su compra.")
    else:
        print(f"Pendientes: 0. Su vuelto es: {abs(monto)}. Gracias por su compra.")

monto_a_pagar(500)