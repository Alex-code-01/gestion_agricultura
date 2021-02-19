# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 12:30:07 2020

@author: alexl
"""
#El usuario introduce el número 3 en el menú inicial y posteriormente solicita la simulación de Asignación de Cultivos (AC)        
def asignacion(dParcelas, dCultivos, asign):
    """
    El sistema sasigna automáticamente cultivos a las parcelas según sus características mientras tengas disponibilidad.
    Debe ir mostrando por pantalla las asignaciones que va realizando.
    """
    print('\nHa seleccionado la simulación Asiganción de Cultivos.\n') #texto introductorio
    print('\nASIGNACION DE CULTIVOS\n')
    if dParcelas == {} or dCultivos == {}: #si no constan parcelas o cultivos en el sistema no se pueden realizar asignaciones
        print('No se pueden realizar asignaciones. Para ello debe haber al menos una parcela y un cultivo registrado en el sistema.')
    else:                                                                  #si constan parcelas y cultivos en el sistema
        for parcela in dParcelas:                                          #para cada parcela en dParcelas
            for cultivo in dCultivos:                                      #para cada cultivo en dCultivos
                if dParcelas[parcela][0] == dCultivos[cultivo][0]:         #si tipoP = tipoC
                    if dParcelas[parcela][1] >= dCultivos[cultivo][3]:     #si tamañoP (tamaño de la parcela) es mayor o igual a tamañomin (tamaño mínimo requerido para el cultivo)
                        if parcela not in asign.values():                  #si la parcela no está ya en asign, es decir, si esta parcela aún no está relacionada
                            if cultivo not in asign:                       #si el cultivo no está ya en asign, es decir, si el cultivo aún no ha sido asignado a ninguna parcela
                                print('Se asigna el cultivo', cultivo,'a la parcela', parcela, '\n')  #imprime mensaje de asignación completada
                                asign.update({cultivo: parcela})                                      #actualiza el diccionario asign con la estructura ({parcela: cultivo})
        asign_sorted = sorted(asign.items())                                        #ordeno los lementos del dic asign en la lista asign_sorted
        asign.clear()                                                               #elimina los elementos del diccionario asign para reordenar sus elementos
        for asignacion in range(len(asign_sorted)):                                 #convierto en dic la lista asign_sorted
            asign.update({asign_sorted[asignacion][0]: asign_sorted[asignacion][1]})#el diccionario asign tiene sus elementos ordenados por los identificadores
        if asign == {}:                                                             #si finalmente no se han producido asignaciones (las parcelas y cultivos no han sido compatibles)
            print('No se han producido asignaciones.')