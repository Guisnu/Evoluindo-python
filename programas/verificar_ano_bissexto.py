def verificar_ano_bissexto(ano):
    if (ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0):
        print("O ano é bissexto")
    else:
        print("O ano não é bissexto")

#Chamado da função
ano = int(input("Digite algum ano: "))
verificar_ano_bissexto(ano)