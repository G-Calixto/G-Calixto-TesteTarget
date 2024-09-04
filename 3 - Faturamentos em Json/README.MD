## QUESTÃO 3 ##
## Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
##  O menor valor de faturamento ocorrido em um dia do mês;
##  O maior valor de faturamento ocorrido em um dia do mês;
## Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

**IMPORTANTE:**
##    Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
##    Podem existir dias sem faturamento, como nos finais de semana e   feriados. Estes dias devem ser ignorados no cálculo da média;


<!--
Para a resolução desse problema a linguagem escolhida foi python.
Primeiro, foi criada uma função para ler os dados do arquivo JSON e salvar em uma tupla.
Em seguida foi criada uma função para cada solicitação: menor valor, maior valor e média de faturamento ignorando os dias que não houve faturamento.
Na função de menor valor, apesar de não especificado no problema, tomei a liberdade de ignorar também os valores zerados.
Após isso as funções foram chamadas dentro de um print para já imprimir seu resultado
 -->