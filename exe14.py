#Construir um programa que leia três valores numéricos inteiros (representados pelas variáveis A, B e C) e apresentar como resultado final, armazenado em memória, o valor do quadrado da soma dos três valores lidos.

a = int(input("Digite o valor da variável A: "))
b = int(input("Digite o valor da variável B: "))
c = int(input("Digite o valor da variável C: "))

resultado = (a + b + c)**2

print(f"o valor do quadrado da soma dos três valores lidos.são: {resultado}")