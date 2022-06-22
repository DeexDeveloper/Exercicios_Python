'''
Escreva uma função que obtenha o maior número da sequência de números
'''

def maior(lista):
    n_maior = 0
    for i in lista:
        if i > n_maior:
            n_maior=i
    return n_maior
b = [1,200,30,4,500]
print(maior(b))
