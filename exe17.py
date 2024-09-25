#pag 149 q) Elaborar um programa que calcule e apresente o valor do resultado da área de uma circunferência (variável A). O programa deve solicitar a entrada do valor do raio da circunferência (variável R). Para a execução deste problema, utilize a fórmula A ← 3.14159265* R ↑ 2.

raio = float(input("Digite o valor do raio da circunferência: "))

formula = 3.14159265 * (raio ** 2 )

print(f"O valor do resultado da área de uma circunferência é: {formula}")