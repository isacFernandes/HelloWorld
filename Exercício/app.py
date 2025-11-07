peso = int(input("Qual o seu peso?"))
unidade = input("(K)g ou (L)bs: ")

if unidade.upper() == "K":
    convertido = peso / 0.45
    print(f"Peso em libras: {str(convertido)}")
else:
    convertido = peso * 0.45
    print(f"Peso em quilos: {str(convertido)}")
