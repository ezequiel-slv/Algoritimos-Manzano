#a) Ler uma temperatura em graus Celsius e apresentá-laconvertida em graus Fahrenheit. A fórmula de conversão é F← C * 9 / 5 + 32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

celsius = float(input("Digite valor de graus celsius: "))

celsius_fahrenheit = (celsius * (9 / 5 + 32))

print(f"{celsius} graus Celsius em Fahrenheit é: {celsius_fahrenheit:.1f}")