# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 12:30:03 2020

@author: alexl
"""
def menu_parcela():
    print('\nPARCELA')
    print('\n -Dar de alta una parcela (A)\n -Dar de baja una parcela (B)\n -Información de las parcelas (I)\n -Existe parcela (E)\n -Volver al menú (M)')

def alta_parcela(dParcelas):
    print('\nHa seleccionado la opción de dar de alta una parcela.\n\nIntruduzca los siguientes datos:\n')               #texto introductorio
    idP = input('Identificador de la parcela (alfanumérico): ')                                                          #idP = identificador alfanumérico (verificar que no existe ya en el sistema)
    while idP in dParcelas:                                                                                              #mientras el usuario introduzca un identificador que ya está presente en dParcelas
        print('\nEl identificador que ha introducido ya consta en el sistema. Vuelva a intentarlo:')                     #mensaje de error
        idP = input('Identificador de la parcela (alfanumérico): ')                                                      #idP = identificador alfanumérico (verificar que no existe ya en el sistema)
    tipoP = input('Tipo de suelo (A,B,C,D,E): ')                                                                         #tipoP = tipo de suelo (A,B,C,D,E)
    while tipoP != 'A' and tipoP != 'B' and tipoP != 'C' and tipoP != 'D' and tipoP != 'E':                              #mientras el usuario introduzca un tipo de suelo que no se corresponde con el aceptado por el programa
        print('\nError. Para introducir el tipo de suelo los valores aceptados son A,B,C,D,E. Vuelve a intentarlo.')     #imprime menseje de error
        tipoP = input('Tipo de suelo (A,B,C,D,E): ')                                                                     #el usuario vuelve a introducir tipoP = tipo de suelo (A,B,C,D,E)
    while True:                                                                                                          #bucle infinito
        try:                                                                                                             #try-catch (control de errores)
            tamañoP = int(input('Tamaño en hectáreas: '))                                                                #tamañoP = tamaño de la patcela en hectáreas 
            break                                                                                                        #si tamañoP es un número entero se sale del bucle infinito
        except ValueError:                                                                                               #si tamañoP no es un número entero (ValueError) se sale del bucle infinito 
            print('\nEl número que ha introducido no es entero. Vuelva a intentarlo.')                                   #mensaje de error
    dParcelas.update({idP : [tipoP, tamañoP]})                                                                           #dParcelas = {idP : [tipoP, tamañoP]}, diccionario en el que se almacenan los datos de las parcelas 
    print('\nCOMPLETADA LA CREACIÓN DE LA PARCELA')                                                                      #mensaje de creación completada
    print('\nID Parcela: ', idP,'\nSuelo: ', tipoP, '\nTamaño: ', tamañoP,'hectáreas')
    Parcelas_sorted = sorted(dParcelas.items())                                                                          #ordeno los elementos del dic dParcelas en la lista Parcelas_sorted
    dParcelas.clear()                                                                                                    #vacío del dic dParcelas para reordenar sus elementos
    for parcelas in range(len(Parcelas_sorted)):                                                                         #convierte en dic la lista Parcelas_sorted
        dParcelas.update({Parcelas_sorted[parcelas][0]: Parcelas_sorted[parcelas][1]})                                   #el diccionario dParcelas tiene sus elementos ordenados por los identificadores
    #muestra el diccionario dParcelas
    print('\nPARCELAS')                                                                                                  #imprime: 'PARCELAS'
    print('\nID: Suelo, Tamaño\n')                                                                                       #datos a mostrar
    for parcela in dParcelas:                                                                                            #para cada parcela en el dic dParcelas
        print(parcela, ':', dParcelas[parcela][0],',', dParcelas[parcela][1])                                            #imprime sus datos

def baja_parcela(dParcelas):
    if dParcelas == {}:                                                                                                  #si el dic dParcelas está vacío no se puede dar de baja ninguna parcela
            print('\nTodavía no consta ninguna parcela en el sistema. No se puede eliminar ninguna parcela.')
    else:                                                                                                                #si no, se pregunta la parcela que se quiere dar de baja y se procede a su eliminación
        print('\nHa seleccionado la opción de dar de baja una parcela.')
        p = input('Introduzca el identificador de la parcela que quiere eliminar: ')
        if p in dParcelas:                                                                                               #si el identificador está en el dic dParcelas, se elimina la informacion de esa parcela
            dParcelas.pop(p)
            print('\nSe ha eliminado la parcela', p)
        else:                                                                                                            #si el identificador no está en el dic dParcelas, mensaje de error y vuelve al menú inicial
            print('\nEl identificador de la parcela que ha introducido no consta en el sistema.')
    
def info_parcela(dParcelas):
    #muestra el diccionario dParcelas
    print('\nPARCELAS')#imprime: 'PARCELAS'
    print('\nID: Suelo, Tamaño\n')#datos a mostrar
    if dParcelas == {}: #si el dic dParcelas está vacío mensaje informativo
        print('No consta ninguna parcela en el sistema.')
    else: #si constan parcelas en el dic dParcelas muestra el dic
        for parcela in dParcelas:                                                                                            #para cada parcela en el dic dParcelas
            print(parcela, ':', dParcelas[parcela][0],',', dParcelas[parcela][1])

def existe_parcela(dParcelas):
    print('\nFuncionalidad que permite consultar si existe o no una parcela en el sistema.')
    parcela = input('Introduzca el nombre de la parcela que desea consultar: ')
    if parcela in dParcelas:
        print('\nLa parcela ', parcela, 'ya consta en el sistema.')
    else:
        print('\nLa parcela ', parcela, 'no consta en el sistema.')

def parcela(dParcelas):
    menu_parcela()
    P = input('Introduzca la opcicón (A,B,I,E o M): ')                                                                           #se pregunta la opción a escoger
    while P != 'A' and P != 'B' and P != 'I' and P != 'E' and P != 'M':  #mientras P sea distinto a A y B y I y M mensaje de error y vuelve a preguntar P
        print('\nEl caracter que ha introducido es incorrecto. Vuelva a intentarlo.')
        P = input('Introduzca la opcicón (A,B,I,E o M): ')
    if P == 'A':
        alta_parcela(dParcelas)
    elif P == 'B':
        baja_parcela(dParcelas)
    elif P == 'I':
        info_parcela(dParcelas)
    elif P == 'E':
        existe_parcela(dParcelas)
    elif P == 'M':
        print('\nHa seleccionado la opción de volver al menú principal.')