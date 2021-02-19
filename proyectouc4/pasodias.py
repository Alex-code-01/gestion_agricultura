# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 12:30:09 2020

@author: alexl
"""
#El usuario introduce el número 3 en el menú inicial y posteriormente solicita la simulación de Paso de los Días (PD) 
def pasodias(dParcelas, dCultivos, asign):
    """
    Pide al usuario la cantidad de días a simular.
    Va avanzando día a día verificando si algún cultivo finaliza.
    Al finalizar el cultivo, la parcela queda libre y con el nuevo tipo de suelo (si aplica).
    Se guarda un histórico de lo producido.
    Debe ir mostrando por pantalla todas las transacciones que realiza.
    """
    print('\nHa seleccionado la simulación Paso de los Días.')                                 #texto introductorio
    while True:                                                                                #bucle infinito
        try:                                                                                   #try-catch (control de errores)
            dias = int(input('Introduce el número de días a simular: '))                       #dias(número entero) = valor introducido por el usuario que corresponden al nº de días a simular
            break                                                                              #si el dato es un número entero se sale del bucle infinito
        except ValueError:                                                                     #si se produce un error ValueError
            print('\nEl número que debe introducir debe ser entero. Vuelva a intentarlo:')     #imprime mensaje de error y continúa en el bucle infinito
    print('\n\nPASO DE LOS DIAS')                                                              #texto introductorio
    while dias >= 0:                                                                           #mientras dias sea mayor que 0
        for cultivo in dCultivos:                                                              #para cada cultivo en dCultivos
            if cultivo in asign:                                                               #si cultivo está en el diccionario asign
                if dCultivos[cultivo][4] == 1:                                                 #si tiempoC (variable del diccionario dCultivos) = 1
                    print('\nAl cultivo', cultivo,'le queda', dCultivos[cultivo][4],'día.')    #al correspondiente cultivo le quedan "tiempoC = 1" día
                    dCultivos[cultivo][4] = dCultivos[cultivo][4] - 1                          #disminuyo tiempoC en 1 unidad
                elif dCultivos[cultivo][4] == 0:                                               #si tiempoC ha llegado a 0
                    print('\nEl cultivo', cultivo, 'ha finalizado.')                           #imprime: 'El cultivo ha finalizado'
                    dCultivos[cultivo][4] = '0'                                                #en la valor tiempoC coloco '0' como string para diferenciarlo 
                elif dCultivos[cultivo][4] == '0':                                             #si tiempoC es '0'(es decir, si ya ha finalizado el cultivo) 
                    break                                                                      #continúa iterando
                else:                                                                          #si tiempoC es distinto de 0 y de 1
                    print('\nAl cultivo', cultivo,'le quedan', dCultivos[cultivo][4],'días.')  #al cultivo le quedan "tiempoC (!= 0 y 1)" días
                    dCultivos[cultivo][4] = dCultivos[cultivo][4] - 1                          #disminuyo tiempoC en 1 unidad
        dias = dias - 1                                                                #disminuyo dias en 1 unidad 