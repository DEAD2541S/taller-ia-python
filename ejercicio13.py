while True:
    mensaje = input("Ingrese un mensaje ('salir' para terminar): ")
    if mensaje.strip().lower() == "salir":
        print("Programa finalizado correctamente.")
        break
    print(f"Mensaje recibido: {mensaje}")