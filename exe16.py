#Elaborar um programa que leia o valor numérico correspondente ao salário mensal (variável SM) de um trabalhador e também fazer a leitura do valor do percentual de reajuste (variável PR) a ser atribuído. Apresentar o valor do novo salário (variável NS) após o armazenamento do cálculo em memória.

salario = float(input("Digite o salário: "))

reajuste = float(input("Digite o valor percentual de reajuste: "))

novo_salario = (salario * (1 + reajuste / 100))

print(f"O valor do salário com reajuste é: {novo_salario:.2f}")