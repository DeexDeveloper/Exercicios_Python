# LOJA DE TINTA

import math
#Recebendo a área e calculando os litros
area = int(input("Digite a área, em m², a ser pintada:"))
#Colocando os 10% de folga
area = math.ceil(area*1.1)

#Calculando os litros necessários
litros = area // 6
if litros % 6 > 0 :
    litros = litros + 1

print("A área com folga é de:",area,"\nVocê vai precisar de",litros,"litros de tinta")
#Comprar apenas latas de 18 litros
latas = litros // 18
if litros % 18 > 0:
    latas = latas + 1
print("Você devera comprar", latas, "latas de tinta. Totalizando R$", latas*80)

#Comprar apenas galões de litros
galoes = litros // 4
if litros % 4 > 0:
    galoes = galoes + 1
print("Você devera comprar", galoes, "latas de tinta. Totalizando R$", galoes*25)

#Mesclar os dois
galoes = 0
latas = litros // 18
litros_restantes = litros % 18
if litros_restantes <= 3*4 :
    galoes = litros_restantes // 4
    if litros_restantes % 4 > 0 :
        galoes = galoes + 1
else :
    latas = latas + 1
print("Serão necessárias", latas,"latas de tinta de 18 litros.")
print("Serão necessárias", galoes,"galões de tinta de 4 litros.")
print("Ao custo de R$",latas*80+galoes*25)
