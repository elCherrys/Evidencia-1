from collections import namedtuple
Llanta = namedtuple("Llanta", "Folio, Fecha_venta, Descripcion, Cantidad, Precio")
lista_llantas = []

while True:
    print(" ")
    print("******************************************")
    print("*  MENU DE REGISTRO DE VENTA DE LLANTAS  *")
    print("******************************************")
    print(" ")
    print("Buenos dias, bienvendido a la venta de llantas que opcion desea realizar *INDICAR EL NUMERO DE LA OPCION*")
    print("OPCION 1, REGISTRAR UNA VENTA")
    print("OPCION 2, CONULTA DE VENTA")
    print("OPCION 3, SALIR DEL MENU")
    respuesta = (int(input("Cual opcion escogeras?: ")))
    if respuesta == 1:
        folio = (int(input("Introduce el numero de folio: ")))
        fecha_venta = (str(input("Introduce la fecha de la venta: ")))
        descripcion = (str(input("Da una breve descripcion de la llanta vendida: ")))
        cantidad = (int(input("Cuantas llantas se vendieron: ")))
        precio = (float(input("Cual fue el precio por llanta: ")))
        total_pago = cantidad * precio
        print(f"El total a pagar es {total_pago}")
        IVA = total_pago/1.16
        pago_final = total_pago + IVA
        print(f"El monto final con IVA incluido es de {pago_final}")
        venta_en_turno = Llanta(folio, fecha_venta, descripcion, cantidad, precio)
        lista_llantas.append(venta_en_turno)
    elif respuesta == 2:
        folio_a_buscar = (int(input("Introduce el numero de folio que quieres consultar: ")))
        for elemento in lista_llantas:
            if elemento.Folio == folio_a_buscar:
                print(f"Fecha de venta: {elemento.Fecha_venta}")
                print(f"Descripcion: {elemento.Descripcion}")
                print(f"Cantidad: {elemento.Cantidad}")
                print(f"Precio: {elemento.Precio}")
                break
        else:
            print("No se tiene registro de ese folio")
    elif respuesta == 3:
        break