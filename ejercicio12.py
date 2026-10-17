texto = input("Ingrese un comentario u opinión: ").lower()

palabras_positivas = ["bueno", "excelente", "maravilloso", "recomiendo", "genial", "gracias"]
palabras_negativas = ["malo", "pesimo", "horrible", "lento", "deficiente", "caro"]

puntaje = 0

for palabra in palabras_positivas:
    if palabra in texto:
        puntaje += 1

for palabra in palabras_negativas:
    if palabra in texto:
        puntaje -= 1

if puntaje > 0:
    sentimiento = "Positivo"
elif puntaje < 0:
    sentimiento = "Negativo"
else:
    sentimiento = "Neutral"

print(f"Puntaje calculado: {puntaje} | Sentimiento: {sentimiento}")