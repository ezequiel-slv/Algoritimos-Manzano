#Ler quatro valores numéricos inteiros e apresentar os resultados armazenados em memória das adições e multiplicações utilizando o mesmo raciocínio aplicado quando do uso de propriedades distributivas para a máxima combinação possível entre as quatro variáveis. Não é para calcular a propriedade distributiva, deve-se apenas usar a sua forma de combinação. Considerando a leitura de valores para as variáveis A, B, C e D, devem ser feitas seis adições e seis multiplicações, ou seja, deve ser combinada a variável A com a variável B, a variável A com a variável C, a variável A com a variável D. Depois, é necessário combinar a variável B com a variável C e a variável B com a variável D e, por fim, a variável C será combinada com a variável D.

a = int(input("Digite um valor a variável A: "))
b = int(input("Digite um valor a variável B: "))
c = int(input("Digite um valor a variável C: "))
d = int(input("Digite um valor a variável D: "))

calculos_adic = [a + b, a + c, a + d, b + c, b + d, c + d]

calculos_mult = [a * b, a * c, a * d, b * c, b * d, c * d]

print(f"O resultado das adicões são: {calculos_adic} e resultado das multiplicações são: {calculos_mult}")