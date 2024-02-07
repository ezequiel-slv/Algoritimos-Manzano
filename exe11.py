#Elaborar um programa que apresente o valor da conversão em real (R$) de um valor lido em dólar (US$). O programa deve solicitar o valor da cotação do dólar e também a quantidade de dólares disponível com o usuário e armazenar em memória o valor da conversão antes da apresentação.

dolar = float(input("Digite o valor em dólar: "))

real = 4.87

conversao = dolar * real

print(f"O valor do dólar recebido, em reais é de: {conversao:.2f} ")