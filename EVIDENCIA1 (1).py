import csv
import numpy as np
from collections import namedtuple
import os
import sys
import sqlite3
from sqlite3 import Error

Llanta = namedtuple("Llanta", "Folio, Fecha_venta, Descripcion, Cantidad, Precio, IVA, Pago_final")
lista_llantas = []


while True:
    print(" ")
    print("******************************************")
    print("*  MENU DE REGISTRO DE VENTA DE LLANTAS  *")
    print("******************************************")
    print(" ")
    print("Buenos dias, bienvendido a la venta de llantas que opcion desea realizar *INDICAR EL NUMERO DE LA OPCION*")
    print("OPCION 1, REGISTRAR UNA VENTA")
    print("OPCION 2, CONULTA DE VENTA ESPECIFICA")
    print("OPCION 3, CONULTA DE TODAS LAS VENTAS")
    print("OPCION 4, SALIR DEL MENU")
    respuesta = (int(input("Cual opcion escogeras?: ")))
    print("-------------------------")
    if respuesta == 1:
        Folio = (int(input("Introduce el numero de folio: ")))
        fecha_venta = (str(input("Introduce la fecha de la venta: ")))
        descripcion = (str(input("Da una breve descripcion de la llanta vendida: ")))
        cantidad = (int(input("Cuantas llantas se vendieron: ")))
        precio = (float(input("Cual fue el precio por llanta: ")))
        total_pago = cantidad * precio
        print(f"El total a pagar es {total_pago}")
        iva = total_pago/1.16
        pago_final = total_pago + iva
        print(f"El monto final con iva incluido es de {pago_final}")
        venta_en_turno = Llanta(Folio, fecha_venta, descripcion, cantidad, precio, iva, pago_final)
        lista_llantas.append(venta_en_turno)
        
        try:
            with sqlite3.connect("Venta_llantas.db") as conn:
                cur = conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS Llantas (Folio INTEGER PRIMARY KEY, fecha_venta TEXT NOT NULL, descripcion TEXT NOT NULL, cantidad INTEGER NOT NULL, precio REAL NOT NULL, iva REAL NOT NULL, pago_final REAL NOT NULL);")
                valores = {"Folio": Folio, "fecha_venta": fecha_venta, "descripcion": descripcion, "cantidad": cantidad, "precio": precio, "iva": iva, "pago_final": pago_final} 
                cur.execute("INSERT INTO Llantas VALUES(:Folio, :fecha_venta, :descripcion, :cantidad, :precio, :iva, :pago_final)", valores)
                registros = cur.fetchall()
                print("Tabla creada")
               
        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        finally:
            if conn:
                conn.close()
    elif respuesta == 2:
        Folio_a_buscar = (int(input("Introduce el numero de folio que quieres consultar: ")))
        for elemento in lista_llantas:
            if elemento.Folio == Folio_a_buscar:
                print(f"Fecha de venta: {elemento.Fecha_venta}")
                print(f"Descripcion: {elemento.Descripcion}")
                print(f"Cantidad: {elemento.Cantidad}")
                print(f"Precio: {elemento.Precio}")
                print(f"IVA: {elemento.IVA}")
                print(f"Pago_final: {elemento.Pago_final}")
                break
        else:
            print("No se tiene registro de ese folio")
    elif respuesta == 3:
        for elemento in lista_llantas:
            print(f"Fecha de venta: {elemento.Folio}")
            print(f"Fecha de venta: {elemento.Fecha_venta}")
            print(f"Descripcion: {elemento.Descripcion}")
            print(f"Cantidad: {elemento.Cantidad}")
            print(f"Precio: {elemento.Precio}")
            print(f"IVA: {elemento.IVA}")
            print(f"Pago_final: {elemento.Pago_final}")
            print("----------------------------------------")
    elif respuesta == 4:
        break