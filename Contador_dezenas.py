# Contador de centenas, dezenas e unidades

print("ATENÇÂO\nDIGITE UM NÚMERO MENOR QUE 1000")
centenas = int(0)
dezenas = int(0)
unidades = int(0)

valor = int(input("Digite o valor:"))
if valor < 1000 :
    centenas = valor // 100
    valor = valor % 100
    dezenas = valor // 10
    valor = valor % 10
    unidades = valor // 1
    if unidades > 1 :
        texto_uni = "unidades."
    else :
        texto_uni = "unidade."
    if dezenas > 1 :
        texto_dez = "dezenas."
    else :
        texto_dez = "dezena."    
    if centenas > 1 :
        texto_cen = "centenas."
    else :
        texto_cen = "centena."
    print("O seu número contém,",centenas,texto_cen)
    print("O seu número contém,",dezenas,texto_dez)
    print("O seu número contém,",unidades,texto_uni)
else :
    print("Valor maior ou igual a 1000")
