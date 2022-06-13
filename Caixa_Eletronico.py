#CAIXA ELETRÔNICO, VALORES ENTRE 10 E 600 REAIS

print('Atenção, você só pode sacar valores entre R$ 10,00 e R$ 600,00')
valor = int(input('Digite o valor de saque'))
notas100 = int(0)
notas50 = int(0)
notas20 = int(0)
notas10 = int(0)
notas5 = int(0)
notas1 = int(0)
resto = int(0)
if 10 <= valor <= 600 :
    if valor >= 100 :
        notas100 = valor // 100
        resto = valor % 100
        if resto >= 50 :
            notas50 = resto // 50
            resto = resto % 50    
        if resto >= 20 :
            notas20 = resto // 20
            resto = resto % 20
        if resto >= 10 :
            notas10 = resto // 10
            resto = resto % 10    
        if resto >= 5 :
            notas5 = resto // 5
            resto = resto % 5
        if resto > 0 :
            notas1 = resto // 1
    
    if 50 <= valor < 100 :
        notas50 = valor // 50
        resto = valor % 50    
        if resto >= 20 :
            notas20 = resto // 20
            resto = resto % 20
        if resto >= 10 :
            notas10 = resto // 10
            resto = resto % 10    
        if resto >= 5 :
            notas5 = resto // 5
            resto = resto % 5
        if resto > 0 :
            notas1 = resto // 1


    if 20 <= valor < 50 :
        notas20 = valor // 20
        resto = valor % 20
        if resto >= 10 :
            notas10 = resto // 10
            resto = resto % 10    
        if resto >= 5 :
            notas5 = resto // 5
            resto = resto % 5
        if resto > 0 :
            notas1 = resto // 1

    if 10 <= valor < 20 :
        notas10 = valor // 10
        resto = valor % 10
        if resto >= 5 :
            notas5 = resto // 5
            resto = resto % 5
        if resto > 0 :
            notas1 = resto // 1 

    if notas100 > 0 :
        print("Você precisa de",notas100,"notas de R$ 100,00")
    if notas50 > 0 :
        print("Você precisa de",notas50,"notas de R$ 50,00")
    if notas20 >0 :
        print("Você precisa de",notas20,"notas de R$ 20,00")
    if notas10 > 0:
        print("Você precisa de",notas10,"notas de R$ 10,00")
    if notas5 > 0 :
        print("Você precisa de",notas5,"notas de R$ 5,00")
    if notas1 > 0 :
        print("Você precisa de",notas1,"notas de R$ 1,00")
else :
    print('Esse valor não é possivel, tente novamente um valor entre 10 e 600')
