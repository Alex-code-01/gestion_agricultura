# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 10:30:39 2021

@author: alexl
"""
def rendimiento(dParcelas, dCultivos, asign):
    if dParcelas != {} and dCultivos != {}:
        parcelas_libres = (len(list(dParcelas.keys()))-len(list(asign.keys())))/len(list(dParcelas.keys()))
        cultivos_libres = (len(list(dCultivos.keys()))-len(list(asign.keys())))/len(list(dCultivos.keys()))
        print('\nEl ', round(parcelas_libres*100), '% de las parcelas no están asignadas.')
        print('El ', round(cultivos_libres*100), '% de los cultivos no están asignados.')
    else:
        print('\nNo hay suficientes datos en el sistema')