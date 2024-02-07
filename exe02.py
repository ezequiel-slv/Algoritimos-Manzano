#Ler uma temperatura em graus Fahrenheit e apresentá-la convertida em graus Celsius. A fórmula de conversão é C ← ((F – 32) * 5) / 9, sendo F a temperatura em Fahrenheit e C

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

fahrenheit_celsius = ((fahrenheit - 32) * 5) / 9

print(f"{fahrenheit} graus Fahrenheit em graus celsius é: {fahrenheit_celsius:.1f}")