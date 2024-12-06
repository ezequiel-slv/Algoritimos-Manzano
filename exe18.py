#pag 149 r) Em  uma  eleição  sindical  concorreram  ao  cargo  de presidente três candidatos (representados pelas variáveis A, B  e  C).  Durante  a  apuração  dos  votos  foram  computados votos nulos e em branco, além dos votos válidos para cada candidato. Deve ser criado um programa de computador que faça  a  leitura  da  quantidade  de  votos  válidos  para  cada candidato, além de ler também a quantidade de votos nulos e  em  branco.  Ao  final,  o  programa  deve  apresentar  o número total de eleitores, considerando votos válidos, nulos e em branco; o percentual correspondente de votos válidos em  relação  à  quantidade  de  eleitores;  o  percentual correspondente de votos válidos do candidato A em relação à quantidade de eleitores; o percentual correspondente de votos  válidos  do  candidato  B  em  relação  à  quantidade  de eleitores; o percentual correspondente de votos válidos do candidato  C  em  relação  à  quantidade  de  eleitores;  o percentual  correspondente  de  votos  nulos  em  relação  à quantidade  de  eleitores;  e,  por  último,  o  percentual correspondente  de  votos  em  branco  em  relação  à quantidade  de  eleitores.  Todos  os  cálculos  devem efetivamente ser armazenados em memoria


def calculo_percentul(parte, total):
    if total == 0:
        return 0
    return (parte / 100) * 100

candidato_A = int(input("Digite a quantidde de votos do candidato A: "))
candidato_B = int(input("Digite a quantidde de votos do candidato B: "))
candidato_C = int(input("Digite a quantidde de votos do candidato C: "))
votos_nulos = int(input("Digite a quantidde de votos de nulos: "))
votos_brancos = int(input("Digite a quantidde de votos brancos: "))

total = candidato_A + candidato_B + candidato_C + votos_nulos + votos_brancos

percentual_valido = calculo_percentul(candidato_A + candidato_B + candidato_C, total)
percentual_A = calculo_percentul(candidato_A, total)
percentual_B = calculo_percentul(candidato_B, total)
percentual_C = calculo_percentul(candidato_C, total)
percentual_nulos = calculo_percentul(votos_nulos, total)
votos_brancos = calculo_percentul(votos_brancos, total)

print(f"percentual total de  eleitores: {total}")
print(f"percentual de votos validos: {percentual_valido}")
print(f"percentual de votos validos para o candidato A: {percentual_A}")
print(f"percentual de votos validos para o candidato B: {percentual_B}")
print(f"percentual de votos validos para o candidato C: {percentual_C}")
print(f"percentual de votos nulos: {percentual_nulos}")
print(f"percentual de votos brancos: {votos_brancos}")

