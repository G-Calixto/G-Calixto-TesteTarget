estados = ['SP','RJ','MG','ES','OUTROS']
valores = [67836.43,36678.66,29229.88,27165.48,19849.53]

valortotal = sum(valores)

for estado,valor in zip(estados,valores):
    porcentagem = (valor/valortotal) * 100
    print(f"O percentual de vendas de {estado} foi {porcentagem:.2f}%")

