import os
acumuladorPasajeroE = 0
acumuladorPasajeroC = 0
acumuladorPasajeroV = 0
listaRut = []
acum = 0
TotalC=0
TotalV=0
TotalE=0
def crearAvion(filas,asientos):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(asientos):
            matriz[i].append("D ")
    return matriz

def estadoAvion(matriz):
    for i in range(len(matriz)):
        print()
        avion[0][0] = "1)"
        avion[1][0] = "2)"
        avion[2][0] = "3)"
        avion[3][0] = "4)"
        avion[4][0] = "5)"
        avion[5][0] = "6)"
        for j in range(len(matriz[i])):
            print(matriz[i][j],end=' ')

def disponibilidadAsientos(matriz):
    asientosDisponibles = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == "D ":
                asientosDisponibles += 1
    return asientosDisponibles

def comprarPasaje(fila,asiento,avion):
    if avion[fila-1][asiento] == "D ":
        avion[fila-1][asiento] = "X "
        return 1
    else:
        return 0

def cancelarPasaje(fila,asiento,avion):
    if avion[fila-1][asiento] == "D ":
        avion[fila-1][asiento] = "X "
        return 1
    else:
        return 0

#Programa principal
print("                                  =====  AVIÓN BOEING 717 ======")
filas = 6
asientos = 34
print("\n   AV AV AV AV AV AC AC AC AC AE AE AE AE AE AE AE AE AC AC AC AC AC AC AC AC AC AC AC AC AC AC AC AC")
print()
avion = crearAvion(filas,asientos)
estadoAvion(avion)
print( "\n   01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33")
print("")
print("mapa de asientos: [AC] Asiento Común | [AV] Asiento Vip    | [AE] Asiento Econimico")
print("=====================================================================================================")

estado = 0

while estado == 0:
    
    print("\n=== Menú de Linea Aérea Flash ======")
    print("1.-Comprar Pasajes")
    print("2.-Mostrar Ubicaciones disponibles")
    print("3.-Ver listado de pasajeros")
    print("4.-Buscar pasajero")
    print("5.-Reasignar asiento")
    print("6.-Mostrar ganacias totales")
    print("7.-Salir")
    print("====================================")

    opcion = int(input("Ingrese la  operación que desea realizar:"))
    os.system("cls")
#VENTA DE ASIENTOS
    if opcion == 1:
        print("                                  =====  AVIÓN BOEING 717 ======")
        print()
        print("   AV AV AV AV AV AC AC AC AC AE AE AE AE AE AE AE AE AC AC AC AC AC AC AC AC AC AC AC AC AC AC AC AC")
        print()
        print("1) D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D")  
        print("2) D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D")  
        print("3) D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D")  
        print("4) D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D")  
        print("5) D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D")  
        print("6) D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D  D")  
        print("   01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33")
        print()
        print("mapa de asientos: [AC] Asiento Común | [AV] Asiento Vip    | [AE] Asiento Econimico")
        print("=====================================================================================================")
        print("=== TIPOS DE ASIENTOS === ")
        print("1.- Asiento común : $60.000 [CLP]")
        print("2.- Asiento Economico: $50.000 [CLP]")
        print("3.- Asiento vip: $80.000 [CLP] + espacio adicional para piernas")

        asientoT = int(input("Ingrese el Tipo de asiento que desea:"))
        if asientoT == 1:
            ValorC = 60000
            print("=== Datos de pasajero ===")
            asientoC = int(input("Cuantos asientos desea comprar:"))
            if asientoC<=disponibilidadAsientos(avion):
                acumuladorPasajeroC+=asientoC
                TotalC= asientoC*ValorC
                for c in range(asientoC):
                    rut = int(input("Ingrese su rut(sin código verificador):"))
                    while rut in listaRut:
                        rut = int(input("El rut ya esta ingresado en la aerolinea, ingrese uno diferente: "))
                    acum+=1
                    listaRut.append(rut)
                    fila = int(input(f"En que fila desea su asiento[1-6]: "))
                    asiento = int(input(f"Que asiento desea[6-9] ó [18-33]: "))
                    if asiento>=6 and asiento<=9 or asiento>18 and asiento<=33:
                        respuesta = comprarPasaje(fila,asiento,avion)
                        if respuesta == 1:
                            print("Asiento reservado")
                            
                        else:
                            print("Asiento ocupado")
                    else:
                        print("asiento no corresponde al seleccionado")
                        
            else:
                print(f"La cantidad de asientos ingresados es superior a {disponibilidadAsientos(avion)} asientos")
                input("Presione ENTER para volver al menú...")
            
                    
        elif asientoT == 2:
            ValorE = 50000
            print("== Datos de pasajero ==")
            asientoE = int(input("Cuantos asientos desea comprar:"))
            if asientoE<=disponibilidadAsientos(avion):
                acumuladorPasajeroE+=asientoE
                TotalE= asientoE*ValorE
                for c in range(asientoE):
                    rut = int(input("Ingrese su rut(sin código verificador):"))
                    while rut in listaRut:
                        rut = int(input("El rut ya esta ingresado en la aerolinea, ingrese uno diferente: "))
                    acum+=1
                    listaRut.append(rut)
                    acum+=1
                    listaRut.append(rut)
                    fila = int(input(f"En que fila desea su asiento [1-6]: "))
                    asiento = int(input(f"Que asiento desea [10-17]: "))
                    if asiento>=10 and asiento<=17:
                        respuesta = comprarPasaje(fila,asiento,avion)
                        if respuesta == 1:
                            print("Asiento reservado")
                            
                        else:
                            print("Asiento ya ocupado")
                            
                    else:
                        print("asiento no corresponde al seleccionado")
                        
            else:
                print(f"La cantidad de asientos ingresados es superior a {disponibilidadAsientos(avion)} asientos")
                input("Presione ENTER para volver al menú...")
                    
        elif asientoT == 3:
            ValorV = 80000
            print("== Datos de pasajero ==")
            asientoV = int(input("Cuantos asientos desea comprar:"))
            if asientoT<=disponibilidadAsientos(avion):
                acumuladorPasajeroV+=asientoV
                TotalV= asientoV*ValorV
                for c in range(asientoV):
                    rut = int(input("Ingrese su rut(sin codigo verificador):"))
                    while rut in listaRut:
                        rut = int(input("El rut ya esta ingresado en la aerolinea, ingrese uno diferente: "))
                    acum+=1
                    listaRut.append(rut)
                    acum+=1
                    listaRut.append(rut)
                    fila = int(input(f"En que fila desea su asiento[1-6]: "))
                    asiento = int(input(f"Que asiento desea[1-5]: "))
                    if asiento>=1 and asiento<=5:
                        respuesta = comprarPasaje(fila,asiento,avion)
                        if respuesta == 1:
                            print("Asiento reservado") 
                        else:
                            print("Asiento ya ocupado")
                        
                    else:
                        print("Asiento no corresponde al seleccionado")
                        
            else:
                print(f"La cantidad de asientos ingresados es superior a {disponibilidadAsientos(avion)} asientos")
                input("Presione ENTER para volver al Menú...")
                
        else:
            print("OPCION INVALIDA")
        input("Presione ENTER para volver al Menú...")
        os.system("cls")
            
        
    elif opcion == 2:
        print("\n   AV AV AV AV AV AC AC AC AC AE AE AE AE AE AE AE AE AC AC AC AC AC AC AC AC AC AC AC AC AC AC AC AC")
        estadoAvion(avion)
        print( "\n   01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33")
        print("")
        print("mapa de asientos: [AC] Asiento Común | [AV] Asiento Vip    | [AE] Asiento Economico")
        print()
        print(f"Asientos Disponibles: {disponibilidadAsientos(avion)}")
        print()
        print("=====================================================================================================")

    elif opcion == 3:
        print("=== Listado de pasajeros ===")
        for c in range(acum):
            listaRut.sort()
            print(f"{listaRut[c]}")
        print("\n")
        input("presione ENTER para volver al menú...")
        os.system("cls")
    elif opcion ==4:
        print("==== Buscar pasajero ====")
        rut=int(input("Ingrese el Rut del pasajero que Buscar: "))
        if rut==rut:
            print("el pasajero está registrado")
        elif rut!=rut:
            print("el pasajero no esta registrado")
        else:
            print("Opción invalida")
        input("Presione ENTER para volver al menú...")
        
    elif opcion == 5:
        print("=== Reasignar asiento ===")
        estadoAvion(avion)
        print()
        print(f"Asientos Disponibles: {disponibilidadAsientos(avion)}")
        rut=int(input("Ingrese el Rut del pasajero: "))
        
        if rut==rut:
            rut=int(input("ingrese nuevo rut:"))
            print("asiento reasignado")
        elif rut!=rut:
            print("el pasajero no esta registrado")
        else:
            print("Opción invalida")
        input("Presione ENTER para volver al Menú...")
        
    elif opcion == 6:
        print("======== TOTAL DE GANANCIAS ==================")
        print(f"TIPO DE ASIENTO  \t CANTIDAD\t TOTAL ")
        print(f"Asiento Comun:   \t{acumuladorPasajeroC} \t\t{TotalC} ")
        print(f"Asiento Economico:  \t{acumuladorPasajeroE} \t\t{TotalE}")
        print(f"Asiento Vip:        \t{acumuladorPasajeroV} \t\t{TotalV}")
        print("==============================================")
        input("presione ENTER para volver al menú...")
        os.system("cls")
        
    elif opcion == 7:
        break
        os.system("cls")

    else:
        print("OPCION INVALIDA")
        input("Presione ENTER para volver al Menú...")
os.system("cls")
