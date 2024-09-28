'''
    Copyright 07/16/2023 
    Author: Igor G. G. Paulo 07/16/2023
'''

while True:
    print ('=============================================' * 3)
    nae = int(input('Escolhas elegiveis:')) # numero de apostas elegiveis

    rp = int(input('Resultados possiveis:')) # Resultados posssiveis

    tp = nae**2 * rp
    print(tp, 'apostas a serem feitas')
    sair = input('sair do programa [Y]/[N]:')
    if sair == 'Y':
        break


