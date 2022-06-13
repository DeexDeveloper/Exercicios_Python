#SEQUENCIA FIBONACCI
a = int(1)
b = int(1)

#Intervalo que o Fibonacci vai ser calculado
while a <= 50000 or b <= 50000 :
    print(a)
    a += b
    print(b)
    b += a
