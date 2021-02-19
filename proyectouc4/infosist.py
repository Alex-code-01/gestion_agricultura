# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 12:30:41 2020

@author: alexl
"""
#El usuario introduce el número 4 en el menú inicial para visualizar la información del sistema
def infosist(dParcelas, dCultivos, asign):
    """
    Muestra la información del estado completo del sistema:
        -Estado Parcelas
        -Cultivos pendientes
        -Histórico producción
    """
    print('\nHa seleccionado la opción de mostrar la Información del Sistema.')                  #texto introductorio
    #CULTIVOS
    for cultivo in dCultivos:                                                                    #para cada cultivo en dCultivos
        if cultivo in asign:                                                                     #si el cultivo está en el diccionario asign
            if dCultivos[cultivo][4] == '0':                                                     #si tiempoC contiene el valor '0' (ya ha finalizado)
                parcela = asign[cultivo]                                                         #denomino parcela a parcela que tiene asignada el cultivo en el diccionario asign 
                print('\nEl cultivo', cultivo, 'ha finalizado en la parcela', parcela)
                if dParcelas[parcela][0] != dCultivos[cultivo][1]:                                                 #si el tipo de suelo inicial de la parcela es distinto del nuevo tipo de suelo (el que queda tras el cultivo) 
                    dParcelas[parcela][0] = dCultivos[cultivo][1]                                                  #cambia el tipo de suelo de la parcela por el nuevo tipo de suelo del cultivo
                    print('\nEl nuevo tipo de suelo de la parcela', parcela, 'es del tipo', dParcelas[parcela][0]) #imprime: 'El nuevo tipo de suelo de la parcela es ...'
                else:                                                                                              #si el tipo de suelo inicial de la parcela coincide con el nuevo tipo de suelo (el que queda tras el cultivo)
                    print('\nLa parcela', parcela, 'mantendrá el mismo tipo de suelo (', dParcelas[parcela][0],')')#imprime: 'El tipo de suelo se mantiene'
                print('\nSe han producido', dParcelas[parcela][1],'hectáreas del cultivo', cultivo)                #imprime las hectáreas producidas
                print('\nLa parcela', parcela, 'ha sido liberada.')
                asign.pop(cultivo)                                                                                 #elimina el cultivo del dic asign (asignaciones)
            else:                                                                                #si tiempoC es ditinto de '0'
                print('\nLa parcela', asign[cultivo],'tiene asignado el cultivo', cultivo)       #imprime:'La parcela correspondiente tiene asignado el cultivo'
        else: #si el cultivo no está en el dic asign
            print('\nEl cultivo',cultivo,'ha quedado libre.')                                    #imprime: 'El cultivo ha quedado libre'
    #PARCELAS
    for parcela in dParcelas:                                                                    #para cada parcela en el diccionario dParcelas
        if parcela not in asign.values():                                                        #si la parcela no está en los valores del diccionario asign (si a la parcela no se le ha asignado un cultivo)
            print('\nLa parcela', parcela, 'ha quedado libre.')                                  #imprime: 'La parcela ha quedado libre'