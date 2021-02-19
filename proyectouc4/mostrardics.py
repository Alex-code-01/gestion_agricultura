# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 12:30:42 2020

@author: alexl
"""
def mostrardics(dParcelas, dCultivos, asign):
    """
    Muestra la información almacenada en los diccionarios.
    En caso de estar vacíos informará al usuario de esta circunstancia.
    En cualquier otro caso, mostrará la información contenida en dichos diccionarios.
    """
    print('\n\nINFORMACIÓN DEL SISTEMA')
    #muestra el diccionario de las Parcelas
    print('\nPARCELAS') #imprime: 'PARCELAS'
    if dParcelas == {}: #si el diccionario dParcelas está vacío: mensaje informativo
        print('\nTodavía no consta ninguna parcela en el sistema.')
    else: #si el dic dParcelas no está vacío se muestran sus elementos
        print('\nID: Suelo, Tamaño\n') #datos a mostrar
        for parcela in dParcelas:
            print(parcela, ':', dParcelas[parcela][0],',', dParcelas[parcela][1])
    #muestra el diccionario de los Cultivos
    print('\nCULTIVOS') #imprime: 'CULTIVOS'
    if dCultivos == {}: #si el diccionario dCultivos está vacío: mensaje informativo
        print('\nTodavía no consta ningún cultivo en el sistema.')
    else: #si el dic dCultivos no está vacío se muestran sus elementos
        print('\nID: Suelo, Nuevo suelo, Transforma suelo, Tamaño mínimo, Tiempo\n') #datos a mostrar
        for cultivo in dCultivos:
            print(cultivo, ':', dCultivos[cultivo][0], ',', dCultivos[cultivo][1], ',', dCultivos[cultivo][2], ',', dCultivos[cultivo][3], ',',dCultivos[cultivo][4])
    #muestra el diccionario asign
    print('\nASIGNACIONES') #imprime: 'ASIGNACIONES'
    if asign == {}: #si el diccionario asign está vacío: mensaje informativo
        print('\nTodavía no se ha realizado ninguna asignación.') 
    else: #si el dic asign no está vacío se muestran sus elementos
        print('\nCultivo : Parcela\n') #datos a mostrar
        for asignacion in asign: 
            print(asignacion, '→', asign[asignacion])