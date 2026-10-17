mensaje = input("Ingrese el mensaje para analizar: ").lower()

palabras_sospechosas = ["gratis", "premio", "urgente", "ganaste", "clave", "banco", "clic"]
contador = 0

for palabra in palabras_sospechosas:
    if palabra in mensaje:
        contador += 1

print(f"Total de palabras sospechosas encontradas: {contador}")