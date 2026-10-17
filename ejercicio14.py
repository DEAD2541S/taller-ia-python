texto = input("Ingrese una palabra o frase: ")


limpio = texto.replace(" ", "").lower()


if limpio == limpio[::-1]:
    print(f"'{texto}' es un palíndromo.")
else:
    print(f"'{texto}' no es un palíndromo.")