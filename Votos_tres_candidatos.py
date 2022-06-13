# Maquina de votos com 3 candidatos
print(" ================ ATENÇÃO ================\nOs canditos e seus respectivos números são:\n 1 - Sanduiche de Merda\n 2 - Babaca Inútil\n 3 - Randy") 
invalido = candidato1 = candidato2 = candidato3 = 0
votantes = int(input("Digite a quantidade de votantes: "))
for cont in range(1,votantes+1) :
    #print(cont)
    voto = int(input("Digite o seu voto: "))
    if voto == 1 :
        candidato1 += 1
    elif voto == 2 :
        candidato2 += 1
    elif voto == 3 :
        candidato3 += 1
    else :
        invalido += 1
print(" ========================================")
print("O Sanduiche de Merda teve %i votos." % (candidato1))
print("O Babaca Inútil teve %i votos." % (candidato2))
print("O Randy teve %i votos." % (candidato3))
print("Tivemos %i votos inválidos."%(invalido))
