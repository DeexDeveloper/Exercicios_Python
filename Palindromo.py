### Palindromo

num = int(input("Digite um número, maior que 10, para verificar se ele é palíndromo: "))
aux = num
reverso = ultimo = 0
while aux > 0 :
    ultimo = aux % 10
    aux //= 10
    reverso = reverso*10+ultimo
if reverso == num :
    print("é um palíndromo")
else:
    print("não é um palíndromo")
