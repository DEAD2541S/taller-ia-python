mensaje = input("Ingrese el detalle del ticket: ").lower()

palabras_soporte = ["error", "fallo", "problema", "ayuda", "sistema"]
palabras_ventas = ["precio", "comprar", "cotizacion", "pago", "factura"]

es_soporte = any(palabra in mensaje for palabra in palabras_soporte)
es_ventas = any(palabra in mensaje for palabra in palabras_ventas)

if es_soporte:
    print("Categoría: Soporte")
elif es_ventas:
    print("Categoría: Ventas")
else:
    print("Categoría: Otro")