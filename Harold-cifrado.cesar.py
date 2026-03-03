
# CIFRADO CESAR BY VALERIA
def cifrar_letra(letra, desplazamiento): # deficibión de la función para cifrar una letra
    if desplazamiento < 1 or desplazamiento > 25: # Validación del desplazamiento para que sea entre 1 y 25
        return "Error: desplazamiento imposible"

    letra = letra.upper() # Converción en mayúscula

    codigo = ord(letra)  # Converción al código ASCII

    if codigo >= 65 and codigo <= 90: # Aplicamos el cifrado solo si es letra está entre (A-Z)

        nuevo_codigo = ((codigo - 65 + desplazamiento) % 26) + 65  # Calcul de la nueva letra con desplazamiento
        return chr(nuevo_codigo)
    else:

        return letra  # Si no es una letra, nos devolverá el mismo carácter

def cifrar_mensaje(mensaje, desplazamiento):  # deficibión de la función para cifrar un mensaje
    mensaje_cifrado = ""
    for letra in mensaje:
        mensaje_cifrado += cifrar_letra(letra, desplazamiento)
    return mensaje_cifrado

# Código principal
mensaje = input("Introduce un mensaje a cifrar: ")  # Pedimos al usuario el mensaje

desplazamiento = int(input("Introduce el desplazamiento (1-25): ")) # Pedimos el desplazamiento al usuario y lo convertimos a entero

mensaje_cifrado = cifrar_mensaje(mensaje, desplazamiento) # Aqui mostramos el mensaje cifrado
print("Mensaje cifrado:", mensaje_cifrado)

# Para verificar, ciframos de nuevo con desplazamiento inverso
mensaje_original = cifrar_mensaje(mensaje_cifrado, 26 - desplazamiento)
print("Mensaje original:", mensaje_original)