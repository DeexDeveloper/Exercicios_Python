'''
Escreva uma função que obtenha a multiplicação de vários números de entrada
'''

def multiplica(lista):
    mult = 1
    for i in lista:
        mult*=i
    return mult
b = [1,2,3,4,5]
print(multiplica(b))
