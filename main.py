#Mini prjeto parte 1
print("Mini projeto parte 1")
nome_completo = "Antonieta da Silva"

dia_nascimento = 16
mes_nascimento = 5
ano_nascimento = 1998
data_nascimento = f"{dia_nascimento}/{mes_nascimento}/{ano_nascimento}" 

dia_atual = 14
mes_atual = 5
ano_atual = 2025
idade = 2024 - ano_nascimento

dias_em_um_ano = 365
dias_em_um_mes = 30

dias_de_anos_vividos = (ano_atual - ano_nascimento) * dias_em_um_ano
dias_de_mes_vividos = (mes_atual - mes_nascimento) * dias_em_um_mes
dias_vividos_no_mes = dia_atual - dia_nascimento

total_de_dias_vividos = dias_de_anos_vividos + dias_de_mes_vividos + dias_vividos_no_mes

print (f"{nome_completo}, nascida em {data_nascimento}")
print (f"{nome_completo} tem {total_de_dias_vividos} dias de vida")
print (f"{nome_completo} tem {idade} anos de vida")
