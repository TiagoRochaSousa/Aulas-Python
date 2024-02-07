km_percorridos = float(input("Digite os km percorridos: "))
dias_alogado = int(input("Digite os dias alugados: "))

#calculos
custo_dia = 60
custo_km = 0.456
valor_km = km_percorridos * custo_km
valor_dia = dias_alogado * custo_dia
valor_total = valor_km + valor_dia

#resultado no ecra
print("O valor total pelo aluguer é de:", valor_total, "euros")
