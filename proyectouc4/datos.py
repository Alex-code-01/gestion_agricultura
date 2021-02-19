# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:50:40 2020

@author: alexl
"""
def datos(dParcelas, dCultivos):
    """
    Función que permite guardar el estado actual del sistema o importar la información almacenada en un fichero externo.
    """
    print('\nDATOS')#texto introductorio
    print('\n -Guardar el estado actual(G).\n -Cargar datos de un fichero(C)\n -Volver al menú(M)')#menú
    opc = input('Introduce la opción (G,C,NF o M): ')#opción a simular
    while opc != 'G' and opc != 'C' and opc != 'M':#mientras la opción no sea reconocida por el sistema mensaje de error
        print('\nEl caracter que ha introducido no es reconocido por el sistema.')
        opc = input('Introduce la opción (G,C o M): ')    
    #si se opta por guardar los datos 
    if opc == 'G':
        #texto introductorio
        print('\nGUARDAR DATOS')
        #PARCELAS
        #se pregunta si quiere guardar los datos
        guardar_parc = input('PARCELAS: Quiere guardar los cambios? (S en caso afirmativo, N en caso negativo): ')
        #mientras la respuesta no sea ni positiva (S) ni negativa (N) mensaje de error
        while guardar_parc != 'S' and guardar_parc != 'N':
            print('\nEl caracter que ha introducido no es reconocido por el sistema.')
            guardar_parc = input('PARCELAS: Quiere guardar los cambios? (S en caso afirmativo, N en caso negativo): ')
        #en caso afirmativo
        if guardar_parc == 'S':
            #bucle infinito
            while True:
                #try-catch de errores
                try:
                    #se solicita el nombre del archivo en el que el usuario quiere guardar los datos
                    nombre_fichero = input('PARCELAS: Introduzca el nombre del fichero en el que quiere guardar la información: ')
                    #se le añade el string 'txt' para convertir el nombre introducido en el formato txt
                    nombre_fichero = nombre_fichero + '.txt' 
                    #abro el archivo en modo escritura
                    f = open(nombre_fichero, 'w')
                    """
                    Se utiliza el modo 'w' porque en caso de no existir se crea el archivo con el nombre indicado y, en caso de que 
                    exista el archivo, elimina el contenido existente y lo reescribe.
                    """
                    #si no se produce ningún error se rompe el bucle infinito
                    break 
                #si se produce algún error se mostrará la razón
                except IOError as e: 
                    print('IO Error = ', e.__doc__)             
            #se escriben los datos almacenados en el dic dParcelas en el archivo
            for parcelas in dParcelas:                   
                f.write(parcelas+',')#escribe la parcela+':'
                f.write(dParcelas[parcelas][0]+',')#escribe tipoP + ', ' 
                f.write('% s'%dParcelas[parcelas][1]+ '\n')#escribe tamañoP y cambia de línea 
            f.close()#se cierra el archivo
            #texto final
            print('\nPARCELAS: Los datos han sido guardados en el fichero', nombre_fichero) 
            print('\nPARCELAS: LOS DATOS HAN SIDO GUARDADOS CORRECTAMENTE')
        elif guardar_parc == 'N': #en caso negativo, mensaje informativo y se pasa a los CULTIVOS 
            print('\nPARCELAS: Ha optado por no guardar los datos permanentemente.')     
        #CULTIVOS
        #se pregunta si quiere guardar los datos
        guardar_cult = input('CULTIVOS: Quiere guardar los cambios? (S en caso afirmativo, N en caso negativo): ')
        #mientras la respuesta no sea ni positiva (S) ni negativa (N) mensaje de error
        while guardar_cult != 'S' and guardar_cult != 'N':
            print('\nEl caracter que ha introducido no es reconocido por el sistema.')
            guardar_cult = input('CULTIVOS: Quiere guardar los cambios? (S en caso afirmativo, N en caso negativo): ')
        #si se opta por guardar los datos
        if guardar_cult == 'S': 
            #bucle infinito
            while True:
                #try-catch de errores
                try:
                    #se solicita el nombre del archivo en el que el usuario quiere guardar los datos
                    nombre_fichero_cult = input('CULTIVOS: Introduzca el nombre con el que quiere guardar el fichero: ')
                    #se le añade el string 'txt' para convertir el nombre introducido en el formato txt
                    nombre_fichero_cult = nombre_fichero_cult + '.txt'
                    #abro el archivo en modo escritura
                    f = open(nombre_fichero_cult, 'w')
                    """
                    Se utiliza el modo 'w' porque en caso de no existir se crea el archivo con el nombre indicado y, en caso de que 
                    exista el archivo, elimina el contenido existente y lo reescribe.
                    """
                    #si no se produce ningún error se rompe el bucle infinito
                    break
                #si se produce algún error se mostrará la razón
                except IOError as e:
                    print('IO Error = ', e.__doc__) 
            #se escriben los datos almacenados en el dic dCultivos en el archivo
            for cultivos in dCultivos:#para cada cultivo en el dic dCultivos
                f.write(cultivos+',')#escribe idC + ':'
                f.write(dCultivos[cultivos][0]+',') #escribe tipoC + ', ' 
                f.write(dCultivos[cultivos][1]+',')#escribe tipoCactual + ', '
                f.write('% s'%dCultivos[cultivos][2]+',')#escribe tranfsuelo + ', '
                f.write('% s'%dCultivos[cultivos][3]+',')#escribe tamañomin + ', '
                f.write('% s'%dCultivos[cultivos][4]+'\n')#escribe tiempoC y salta de línea
            #se cierra el archivo
            f.close()
            #texto final
            print('\nCULTIVOS: Los datos han sido guardados en el fichero', nombre_fichero_cult)
            print('\nCULTIVOS: LOS DATOS HAN SIDO GUARDADOS CORRECTAMENTE')
        #en caso negativo, mensaje informativo y se finaliza 
        elif guardar_cult == 'N':
            print('\nCULTIVOS: Ha optado por no guardar los datos permanentemente.')
        print('\nCOMPLETADO EL PROCESO DE GUARDADO')
    #si se opta por cargar los datos
    elif opc == 'C':
        #texto introductorio
        print('\nCARGAR DATOS')
        #PARCELAS
        print('\nPARCELAS')
        #se pregunta si quiere dar de alta info
        arch_parc = input('PARCELAS: Quiere dar de alta información almacenada en algún fichero? (S en caso afirmativo, N en caso negativo): ')
        #mientras la respuesta no sea ni positiva (S) ni negativa (N) mensaje de error
        while arch_parc != 'S' and arch_parc != 'N':
            print('\nEl caracter que ha introducido no es reconocido por el sistema.')
            arch_parc = input('PARCELAS: Quiere dar de alta información almacenada en algún fichero? (S en caso afirmativo, N en caso negativo): ')
        #en caso afirmativo
        if arch_parc == 'S':
            #bucle infinito
            while True:
                #try-catch de errores
                try:
                    #se solicita el nombre del fichero
                    fichero_parc = input('PARCELAS: Introduce el nombre del archivo en el que se almacenan los datos: ')
                    #se le añade el string 'txt' para convertir el nombre introducido en el formato txt
                    fichero_parc = fichero_parc + '.txt'
                    #se abre el fichero en modo lectura, en caso de que no exista lanza una excepción FileNotFoundError
                    f = open(fichero_parc,'r')#abro el archivo en modo lectura 
                    #si no se produce ningún error se rompe el bucle infinito
                    break
                #en caso de que el fichero no exista, mensaje de error
                except IOError:
                    print('\nNo existe ningún archivo con el nombre ', fichero_parc)
                    print('\nPara cargar los datos de un archivo:\n\n -1º El archivo debe existir.\n -2º El archivo debe estar en la misma carpeta que este proyecto.')
                    print('\nVuelve a intentarlo:')
            #se importa la información del fichero
            for line in f: #para cada línea en el archivo
                lineSplit = line.split(',')#separación
                lineSplit[2] = int(lineSplit[2])#convierto a entero el valor tipoP
                dParcelas.update({lineSplit[0]: [lineSplit[1], lineSplit[2]]})#actualizo el dic dParcelas
                Parcelas_sorted = sorted(dParcelas.items())#ordeno los elementos del dic dParcelas en la lista Parcelas_sorted
                dParcelas.clear()#vacío del dic dParcelas para reordenar sus elementos
                for parcelas in range(len(Parcelas_sorted)):#convierte en dic la lista Parcelas_sorted
                    dParcelas.update({Parcelas_sorted[parcelas][0]: Parcelas_sorted[parcelas][1]})#el diccionario dParcelas tiene sus elementos ordenados por los identificadores
            #texto final
            print('\nPARCELAS: Las parcelas almacenadas en el fichero', fichero_parc,'han sido dadas de alta.')
            print('\nPARCELAS: COMPLETADO EL PROCESO DE CARGA DE DATOS')
            #se cierra el archivo
            f.close()
        #en caso negativo mensaje informativo y se pasa a los CULTIVOS
        elif arch_parc == 'N':
            print('\nPARCELAS: Ha optado por no dar de alta información almacenada.')
        #CULTIVOS
        #texto introductorio
        print('\nCULTIVOS')
        #se pregunta si quiere dar de alta información
        arch_cult = input('CULTIVOS: Quiere dar de alta información almacenada en algún fichero? (S en caso afirmativo, N en caso negativo): ')
        #mientras la respuesta no sea ni positiva (S) ni negativa (N) mensaje de error
        while arch_cult != 'S' and arch_cult != 'N':
            print('\nEl caracter que ha introducido no es reconocido por el sistema.')
            arch_cult = input('Quiere dar de alta los cultivos almacenados en el sistema? (S en caso afirmativo, N en caso negativo): ')
        #en caso afirmativo
        if arch_cult == 'S':
            #bucle infinito
            while True:
                #try-catch de errores
                try:
                    #se solicita el nombre del fichero
                    fichero_cult = input('CULTIVOS: Introduce el nombre del archivo en el que se almacenan los datos: ')
                    #se le añade el string 'txt' para convertir el nombre introducido en el formato txt
                    fichero_cult = fichero_cult +  '.txt'
                    #se abre el fichero en modo lectura, en caso de que no exista lanza una excepción FileNotFoundError
                    f = open(fichero_cult,'r')
                    #si no se produce ningún error se rompe el bucle infinito
                    break
                #en caso de que el fichero no exista, mensaje de error
                except IOError:
                    print('\nNo existe ningún archivo con el nombre ', fichero_cult)
                    print('\nPara cargar los datos de un archivo:\n\n -1º El archivo debe existir.\n -2º El archivo debe estar en la misma carpeta que este proyecto.')
                    print('\nVuelve a intentarlo:')
            #se importa la información del fichero
            for line in f:
                lineSplit = line.split(',')
                lineSplit[4] = int(lineSplit[4])
                lineSplit[5] = int(lineSplit[5])
                dCultivos.update({lineSplit[0]: [lineSplit[1], lineSplit[2], lineSplit[3], lineSplit[4], lineSplit[5]]})
                Cultivos_sorted = sorted(dCultivos.items()) #ordeno los elementos del dic dCultivos en la lista Cultivos_sorted
                dCultivos.clear() #elimino los elementos del dic dCultivos para reordenar sus elementos
                for cultivos in range(len(Cultivos_sorted)): #convierto en dic la lista Cultivos_sorted
                    dCultivos.update({Cultivos_sorted[cultivos][0]: Cultivos_sorted[cultivos][1]})#el diccionario dCultivos tiene sus elementos ordenados por los identificadores
            #texto final
            print('\nCULTIVOS: Los cultivos almacenados en el fichero', fichero_cult,'han sido dados de alta.')
            print('\nCULTIVOS: COMPLETADO EL PROCESO DE CARGA DE DATOS')
            #se cierra el archivo
            f.close()
        #en caso negativo mensaje informativo y se finaliza
        elif arch_cult == 'N':
            print('\nCULTIVOS: Ha optado por no dar de alta información almacenada.')        
    #si se opta por volver al menú inicial se vuelve
    elif opc == 'M':
        print('\nHa optado por volver al menú principal.')