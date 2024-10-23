#!/usr/bin/env python

'''bones_practiques. Calcula la divisió entera de dos nombres.

Institut Icària
Programació - 1r Batxillerat - Curs 2024-25

A partir de dos nombres, dividend i divisor, el programa calcula el quocient i
el residu i els mostra per pantalla.
A part mostra la divisió realitzada per pantalla.
'''

__author__ = "Iker Zambrano"
__email__ = "izambrano@instituticaria.cat"
__date__ = "2024/10/21"

Dividend = int(input("Introdueix el dividend: "))
divisor = int(input("Introdueix el divisor: "))
Quocient = Dividend//divisor
residu = Dividend % divisor
print(f"Divisió: {Dividend}/{divisor}")
print(f"Quocient: {Quocient}")
print(f"Residu: {residu}")
