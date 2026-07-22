#entrada = input("Qual cidade voce nacseu? ").strip().upper()
#cidade = entrada[:6].startswith("SANTO")
#print(cidade)

entrada = input("Qual cidade voce nacseu? ").strip().upper()

cidade = entrada.split()

cidade_valida = cidade[0] == "SANTO"

print(cidade_valida)