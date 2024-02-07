#Ler dois valores numéricos inteiros (representados pelas variáveis A e B) e apresentar o resultado armazenado em memória do quadrado da diferença do primeiro valor (variável A) em relação ao segundo valor (variável B).

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

resultado = (a - b)**2

print(f"O quadrado da diferença do primeiro valor (variável A) em relação ao segundo valor (variável B) é {resultado}")
