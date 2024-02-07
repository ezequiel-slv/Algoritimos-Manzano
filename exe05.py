#Efetuar o cálculo e apresentar o valor de uma prestação de um bem em atraso, utilizando a fórmula PRESTAÇÃO ← VALOR + (VALOR * (TAXA / 100) * TEMPO).

tempo = float(input("Digite o tempo de atraso em meses: "))
valor_cobrado= 1200
taxa = 10
prestação = valor_cobrado + (valor_cobrado * (taxa/100) * tempo)
print(f"O valor da prestação de um bem em atraso é de {prestação}")

