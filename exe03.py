#Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula VOLUME ← 3.14159 * R ↑ 2 * ALTURA.

raio = float(input("Digite o raio da lata: "))
altura = float(input("Digite a altura da lata: "))

volume_lata = (3.14159 * raio ** 2 * altura)

print(f"O valor do volume da lata de óleo é: {volume_lata:.2f}")