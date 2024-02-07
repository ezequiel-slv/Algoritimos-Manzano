#Elaborar um programa que apresente o valor da conversão em dólar (US$) de um valor lido em real (R$). O programa deve solicitar o valor da cotação do dólar e também a quantidade de reais disponível com o usuário e armazenar em memória o valor da conversão antes da apresentação.

real = float(input("Digite o valor em Reais: "))

dolar = 0.21

conversao = real * dolar

print(f"O valor do Real recebido, em dólar é de: {conversao:.2f} ")