#Equação segundo grau
a = int(input("Digite o valor de A: "))
if a != 0:
    b = int(input("Digite o valor de B: "))
    c = int(input("Digite o valor de C: "))
    delta = b**2-4*a*c
    if delta <0:
        print("O programa não possui raizes!")
    elif delta == 0:
        x = -b/(2*a)
        print("O X é igual a",x)
    else:
        x1 = (-b+delta**0.5)/2*a
        x2 = (-b-delta**0.5)/2*a
        print("O X1 é igual %d e o X2 é igual %d."%(x1,x2))
else:
    print("Não é uma equação do segundo grau!")
