# subnumeros
n = int(input("Digite o numero que deseja saber: "))
subproduto = int(input("Digite o número do número para verificar se é subproduto: "))
if n >= subproduto :
    aux_n = n
    aux_sub = subproduto
    dig_n = dig_sub = 0
    while aux_sub > 0:
        aux_sub //= 10
        dig_sub += 1
    aux_n = n
    while aux_n > 0 :
        verifica = aux_n%(10**dig_sub)
        if verifica == subproduto :
            print("Sim, é subproduto.")
            aux_n = 0
        aux_n //= 10
    if verifica != subproduto :
        print("Não é subproduto.")
else:
    print("O subproduto deve ser menor ou igual ao número.")
