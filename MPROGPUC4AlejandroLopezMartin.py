# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 12:35:21 2020

@author: alexl
"""
def menu():
    """
    Menú inicial del programa.
    Muestra las distintas funciones que tiene el programa.
    Las funciones van asignadas a un valor numérico.
    En el caso de que el usuario no introduzca un valor numérico se mostrará un mensaje de error.
    """
    print('\n-----------------------------')
    print('MENU PROYECTO UC4\n 1)Parcela\n 2)Cultivo\n 3)Simular\n 4)Info sistema\n 5)Datos\n 6) Rendimiento\n 0)Salir')                 #menú inicial
    print('-----------------------------')
    while True:                                                                                                         #bucle infinito
        try:                                                                                                            #try-catch(control de errores)
            return int(input("Introduce la opción(1, 2, 3, 4, 5, 6 o 0): "))                                               #introducir una opción (1,2,3,4,5)
            break                                                                                                       #si el número introducido es entero se sale del bucle infinito
        except ValueError:                                                                                              #si se produce un ValueError
            print('\nError. Debe introducir un número entero! (del 0 al 6 el programa realizará diferentes funciones)') #mensaje de error y se continúa en el bucle infinito

#diccionarios:
dParcelas = {} #dic en el que se almacena la info de las parcelas
dCultivos = {} #dic en el que se almacena la info de los cultivos
asign = {}     #dic en el que se almacenan las asignaciones realizadas (opción 3(AC) en el menú inicial)
#dParcelas = {'P1': ['A', 100], 'P2': ['B',80], 'P3': ['C', 25], 'P4': ['E', 30]}
#dCultivos = {'C1': ['A','B', True, 90, 12], 'C2': ['B', 'B', False, 78, 4], 'C3': ['C', 'B', True, 30, 2], 'C4': ['A', 'E', True, 20, 3]}
from proyectouc4 import parcela, cultivo, asignacion, pasodias, infosist, mostrardics, datos, rendimiento
opmenu = 1
#bucle infinito para elegir entre las diferentes opciones hasta que el usuario quiera salir(0) 
while opmenu != 0:
    opmenu = menu()
    if opmenu == 1:   #si introduce el número 1 en el menú inicial se activará la función parcela()
        parcela.parcela(dParcelas)
    elif opmenu == 2: #si introduce el número 2 en el menú inicial se activará la función cultivo()
        cultivo.cultivo(dCultivos)
    elif opmenu == 3: #si introduce el número 3 en el menú inicial se solicitará al usuario que especifique el tipo de simulación que quiere:
        d = input('\nHa seleccionado la opción de Simular.\n →Asignación de Cultivos(AC)\n →Paso de los Días(PD)\n →Volver al Menú principal(M)\n\nSeleccione el tipo de simulación que se quiere: ')
        if d == 'AC':   #si introduce'AC' se activará la función asignacion()
            asignacion.asignacion(dParcelas, dCultivos, asign)
            mostrardics.mostrardics(dParcelas, dCultivos, asign)
        elif d == 'PD': #si introduce 'PD' se activará la función pasodias()
            mostrardics.mostrardics(dParcelas, dCultivos, asign)
            pasodias.pasodias(dParcelas, dCultivos, asign)
        elif d == 'M':  #si introduce 'M' se volverá al menú principal
            print('\nHa seleccionado volver al menú principal.\n')
        else:           #si se equivoca al introducir el tipo de simulación se devolverá un mansaje de error y se volverá al menú principal
            print('\nError al solicitar la simulación. Vuelve a intentarlo.')
    elif opmenu == 4: #si introduce el número 4 en el menú inicial se activará la función infosist()
        infosist.infosist(dParcelas, dCultivos, asign)
        mostrardics.mostrardics(dParcelas, dCultivos, asign)
    elif opmenu == 5: #si introduce el número 5 en el menú inicial se activará la función datos()
        datos.datos(dParcelas, dCultivos)    
    elif opmenu == 6:
        rendimiento.rendimiento(dParcelas, dCultivos, asign)
    elif opmenu == 0: #si introduce el número 0 en el menú inicial se le preguntará si realmente quiere salir del programa
        salir = input('Está seguro de que quiere salir?(S en caso afirmativo, N en caso negativo): ')
        while salir != 'S' and salir != 'N':
            print('\nEl caracter que ha introducido no es reconocido por el sistema. Vuelva a intentarlo:')
            salir = input('Está seguro de que quiere salir?(S en caso afirmativo, N en caso negativo): ')
        if salir == 'S': #En caso afirmativo, se mostrarán los dics y se finalizará el programa    
            cambios = input('Quiere guardar el estado actual del sistema?(S en caso afirmativo, N en caso negativo): ')
            while cambios != 'S' and cambios != 'N':
                print('\nEl caracter que ha introducido no es reconocido por el sistema. Vuelva a intentarlo:')
                cambios = input('Quiere guardar el estado actual del sistema?(S en caso afirmativo, N en caso negativo): ')
            if cambios == 'S':
                print('\nPulse G para Guardar los Datos.')
                datos.datos(dParcelas, dCultivos)
            elif cambios == 'N':
                print('')
            print('\nHa optado por finalizar el programa PROYECTO UC4.')
            mostrardics.mostrardics(dParcelas, dCultivos, asign)
            print('\n\nFINALIZACIÓN DEL PROGRAMA PROYECTO UC4')
        elif salir == 'N': #en caso negativo, se volverá al menú principal
            print('\nHa optado por volver al programa.')
            opmenu = 0
    else:
    #si el usuario introduce el número distinto a los establecidos devolverá un mensaje de error y se volverá al menú principal
        print('\nError. Número incorrecto. El programa realiza distintas funciones introduciendo números del 0 al 6. \n\nVuelve a intentarlo:')
