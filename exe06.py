#Ler dois valores para as variáveis A e B e efetuar a troca dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores após a efetivação do processamento da troca.

A = 5
B = 10

temp = A
A = B
B = temp


print(f"O valor de A é: {A}")
print(f"O valor de B é: {B}")