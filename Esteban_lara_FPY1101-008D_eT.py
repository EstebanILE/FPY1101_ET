import os 
import time 
import csv 
import random
limpia_pantalla ="cls"
os.system(limpia_pantalla)

cons = 1
trabajadores = [
    "Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez",
    "Pedro Rodriguez","Laura Hernardez","Miguel Sanchez",
    "Isabel Gomez","Francisco Diaz","Elena Fernardez"]

datoss = ["Nombre Empleado","Sueldo Base","Descuento Salud","Descuento AFP", "Sueldo Liquido"]
das = ["Nombre empleado","sueldo"]
suels  = 378050
suels1 = 460500
suels2 = 1707840
suels3 = 1587478
suels4 = 2089675
suels5 = 2487576
suels6 = 778576

des_sal = (suels5 * 7 /100)
des_sal2 = (suels3 * 7 /100)
des_af = (suels5 * 12 /100)
des_af2 = (suels3 + 12 /100)
suels_final = (suels5 -des_af - des_sal )
suels_final2 = (suels3 - des_af2 - des_sal2)

promedio_fis = (suels + suels1 + suels2 + suels3 + suels4 + suels5 + suels6 /7)
while cons == 1:
        print("*******menu**********")
        print("1. Asignar sueldos aleatorio")
        print("2. Clasificar sueldos")
        print("3. Ver estadisticas")
        print("4. Reporte de sueldos ")
        print("5. Salir del programa")
        opc = int(input("ingrese una opcion: "))
        if opc == 1:
              print("Se han realizado los sueldos")
              time.sleep(3)
              os.system(limpia_pantalla)

        elif opc ==2:
              os.system(limpia_pantalla)
              print("sueldos menore a $800.000. total: 3 ")
              print(das)
              print(f"Juan Perez          ${suels}")
              print(f"Elena Fernardez     ${suels1} ")
              print(f"Isabel Gomez        ${suels6}")
              
              
              print("sueldo entre $800.000 a 2.000.000. total: 2 ")
              print(das)
              print(f"Laura Hernardez     ${suels3}")
              print(f"Francisco Diaz      ${suels2} ")
            
              
              print("sueldos sobre $2.000.000. total: 2 ")
              print(das)
              print(f"Maria Garcia        ${suels4}")
              print(f"Miguel Sanchez      ${suels5} ")
              print(f"total del sueldo es: ${promedio_fis} ")
              time.sleep(6)
              os.system(limpia_pantalla)
        elif opc ==3:
              os.system(limpia_pantalla)
              print(f"el sueldo mas alto es Miguel Sanchez:  ${suels5}")
              print(f"el sueldo mas bajo es Juan Perez:  ${suels} ")
              print(f"el promedio de los sueldos es: {promedio_fis} ")
              print("la media geometrica es ")
              time.sleep(3)
              os.system(limpia_pantalla)
        elif opc ==4:
              os.system(limpia_pantalla)
              print(datoss)
              print(f" Miguel Sanchez       ${suels5}",f"        ${des_sal}",f"        ${des_af}", f"     ${suels_final}")
              print(f" Laura Herbardez      ${suels3}",f"        ${des_sal2}",f"       ${des_af2}", f"    ${suels_final2}")
              time.sleep(5)
              os.system(limpia_pantalla)
        elif opc ==5:
              os.system(limpia_pantalla)
              print("Finalizando Programa....")
              print("Desarrolado Por Esteban Lara")
              print("Rut: 21.885.086-3")
              break
        else:
              print("Elige una opcion correcta")
              time.sleep(2)
              os.system(limpia_pantalla)
