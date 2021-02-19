# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 12:30:05 2020

@author: alexl
"""
#El usuario introduce el número 2 en el menú inicial para introducir los datos del cultivo.  
def cultivo(dCultivos):
    """
    Función que realiza distintos procesos en relación a los cultivos. 
    Permite dar de alta un cultivo, dar de baja un cultivo o consultar la información referente a los cultivos.
    """
    print('\nCULTIVO')
    print('\n -Dar de alta un cultivo (A)\n -Dar de baja un cultivo (B)\n -Información de los cultivos (I)\n -Volver al menú (M)')
    C = input('Introduzca la opcicón (A,B,I o M): ')          #se pregunta la opción a escoger
    while C != 'A' and C != 'B' and C != 'I' and C != 'M':  #mientras C sea distinto a A y B y I y M mensaje de error y vuelve a preguntar P
        print('\nEl caracter que ha introducido es incorrecto. Vuelva a intentarlo.')
        C = input('Introduzca la opcicón (A,B,I o M): ')
    while C == 'A':                                                                                 #si C es A (dar de alta)
        print('\nHa seleccionado la opción de dar de alta un cultivo.\n\nIntruduzca los siguientes datos:\n') #texto introductorio
        idC = input('Identificador del cultivo (alfanumérico): ') #idC = identificador alfanumérico único 
        while idC in dCultivos:                                    #mientras el usuario introduzca un identificador que ya está presente en dCultivos
            print('\nEl identificador que ha introducido ya consta en el sistema. Vuelva a intentarlo:') #mensaje de error
            idC = input('Identificador del cultivo (alfanumérico): ') #idC = identificador alfanumérico único 
        tipoC = input('Tipo de suelo (A,B,C,D,E): ')              #tipoC = tipo de suelo donde se puede plantar (A,B,C,D,E)
        while tipoC != 'A' and tipoC != 'B' and tipoC != 'C' and tipoC != 'D' and tipoC != 'E': #mientras el usuario introduzca un tipo de suelo incorrecto (distinto de A,B,C,D,E)
            print('\nError. Para introducir el tipo de suelo los valores aceptados son A,B,C,D,E. Vuelve a intentarlo.') #imprime mensaje de error
            tipoC = input('Tipo de suelo (A,B,C,D,E): ')           #tipoC = tipo de suelo donde se puede plantar (A,B,C,D,E)
        tipoCactual = input('Nuevo tipo de suelo (A,B,C,D,E): ')  #tipoCactual = nuevo tipo de suelo (A,B,C,D,E)
        while tipoCactual != 'A' and tipoCactual != 'B' and tipoCactual != 'C' and tipoCactual != 'D' and tipoCactual != 'E':  #mientras el usuario introduzca un tipo de suelo incorrecto (distinto de A,B,C,D,E)
            print('\nError. Para introducir el nuevo tipo de suelo los valores aceptados son A,B,C,D,E. Vuelve a intentarlo.') #imprime mensaje de error
            tipoCactual = input('Tipo de suelo actual (A,B,C,D,E): ')  #tipoCactual = nuevo tipo de suelo (A,B,C,D,E)
        if tipoC == tipoCactual:  #si el tipo de suelo inicial (tipoC) coincide con el nuevo tipo de suelo (tipoCactual) 
            transfsuelo = False   #transfsuelo =  = transforma el suelo (valor booleano) = False
        else:                     #si el tipo de suelo inicial (tipoC) no coincide con el nuevo tipo de suelo (tipoCactual)
            transfsuelo = True    #transfsuelo = transforma el suelo (valor booleano) = True
        while True:#bucle infinito
            try:#try-catch(control de errores)
                tamañomin = int(input('Tamaño mínimo en hectáreas: ')) #tamañomin = tamaño mínimo en hectáreas
                break#si los datos introducidos son numeros enteros se sale del bucle infinito
            except ValueError: #si se produce un ValueError
                print('\nEl número que ha introducido no es entero. Vuelva a intentarlo.') #mensaje de error y se continua en el bucle infinito
        while True:#bucle infinito
            try:#try-catch(control de errores)
                tiempoC = int(input('Tiempo de cultivo en días: '))    #tiempoC = tiempo de cultivo en días
                break #si los datos introducidos son numeros enteros se sale del bucle infinito
            except ValueError: #si se produce un ValueError
                print('\nEl número que ha introducido no es entero. Vuelva a intentarlo.') #mensaje de error y se continua en el bucle infinito
        dCultivos.update({idC : [tipoC, tipoCactual, transfsuelo, tamañomin, tiempoC]}) #dCultivos = diccionario en el que se almacenan los datos de los cultivos
        print('\nCOMPLETADA LA CREACIÓN DEL CULTIVO')#mensaje de creación completada
        print('\nID Cultivo: ', idC,' \nSuelo: ', tipoC,'\nNuevo suelo ', tipoCactual, '\nTamaño mínimo: ', tamañomin, 'hectáreas\nTiempo: ', tiempoC, ' días.')
        Cultivos_sorted = sorted(dCultivos.items()) #ordeno los elementos del dic dCultivos en la lista Cultivos_sorted
        dCultivos.clear() #elimino los elementos del dic dCultivos para reordenar sus elementos
        for cultivos in range(len(Cultivos_sorted)): #convierto en dic la lista Cultivos_sorted
            dCultivos.update({Cultivos_sorted[cultivos][0]: Cultivos_sorted[cultivos][1]})#el diccionario dCultivos tiene sus elementos ordenados por los identificadores
        #muestra el diccionario dCultivos
        print('\nCULTIVOS')
        print('\nID: Suelo, Nuevo suelo, Transforma suelo, Tamaño mínimo, Tiempo\n')
        for cultivo in dCultivos:
            print(cultivo, ':', dCultivos[cultivo][0], ',', dCultivos[cultivo][1], ',', dCultivos[cultivo][2], ',', dCultivos[cultivo][3], ',',dCultivos[cultivo][4])
        C = input('Quiere dar de alta otro cultivo?(A para dar de alta otro cultivo): ')     #se pregunta si quiere dar de alta otro cultivo                                                                                         
    if C == 'B':#si C es B (dar de baja)
        if dCultivos == {}: #si el dic dCultivos está vacío no se puede eliminar ningún cultivo
            print('\nTodavía no consta ningún cultivo en el sistema. No se puede eliminar ningún cultivo.')
        else: #si no, se pregunta el cultivo que se quiere dar de baja y se procede a su eliminación
            print('\nHa seleccionado la opción de dar de baja un cultivo.')
            c = input('Introduzca el identificador del cultivo que quiere eliminar: ')
            if c in dCultivos:
                dCultivos.pop(c)
                print('\nSe ha eliminado el cultivo', c)
            else:
                print('\nEl identificador del cultivo que ha introducido no consta en el sistema.')
    elif C == 'I': #si C es I (información), muestra el dic dCultivos
        #muestra el diccionario dCultivos
        print('\nCULTIVOS')
        print('\nID: Suelo, Nuevo suelo, Transforma suelo, Tamaño mínimo, Tiempo\n')
        if dCultivos == {}: #si el dic dCultivos está vacío mensaje informativo 
            print('No consta ningún cultivo en el sistema.')
        else: #si constan cultivos en el dic dCultivos muestra el dic 
            for cultivo in dCultivos:
                print(cultivo, ':', dCultivos[cultivo][0], ',', dCultivos[cultivo][1], ',', dCultivos[cultivo][2], ',', dCultivos[cultivo][3], ',',dCultivos[cultivo][4])
    elif C == 'M': #si C es M se vuelve al menú inicial
        print('\nHa seleccionado la opción de volver al menú principal.')