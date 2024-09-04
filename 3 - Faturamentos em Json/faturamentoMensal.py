import json
caminho = 'dados.json'

# Função que lê o arquivo em JSON e retorna os dados em uma tupla.
def dados_faturamento(caminho):
    with open(caminho, 'r') as file:
        data = json.load(file)
    return tuple((item['dia'], item['valor']) for item in data)


# Função que encontra o menor valor de faturamento ocorrido em um dia no mês
def menor_valor_faturado(dados):
    menor = float('inf')
    for dia, valor in dados:
        if valor != 0 and valor < menor:
            menor = valor
    return menor

# Função que encontra o maior valor de faturamento ocorrido em um dia no mês 
def maior_valor_faturado(dados):
    maior = float('-inf')
    for dia, valor in dados:
        if valor > maior:
            maior = valor
    return maior

# Função que encontra a média mensal faturada ignorando todos os feriados e finais de semana
def media_mensal(dados):
    soma = 0
    cont = 0
    for dia, valor in dados:
        if valor != 0:
            soma += valor
            cont += 1
    media = soma / cont
    maior_que_media = 0
    for dia, valor in dados:
        if valor > media:
            maior_que_media += 1
    return maior_que_media


dados = dados_faturamento(caminho)
print()
print(f'O menor valor faturado em um único dia foi: {menor_valor_faturado(dados)}\n')
print(f'O maior valor faturado em um único dia foi: {maior_valor_faturado(dados)}\n')
print(f'O número de dias no mês em que o valor de faturamento diário foi superior à média mensal é: {media_mensal(dados)}')
