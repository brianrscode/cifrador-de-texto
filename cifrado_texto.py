import hashlib
# cSpell:enable

def cifrar_texto(texto, funcion_hash) -> str:
    """
    Toma una cadena de texto y una función hash y devuelve el texto hasheado.

    Parámetros:
    texto (str): La cadena de texto a hashear.
    funcion_hash (función): La función hash a utilizar.

    Devuelve:
    str: El resumen hexadecimal del `texto` hasheado.
    """

    texto_cifrado = funcion_hash(texto.encode("utf-8"))
    return texto_cifrado.hexdigest()


def main():
    """
    Solicita al usuario seleccionar una función hash, luego solicita ingresar un texto para cifrar con la función hash seleccionada.
    Luego cifra el texto usando la función seleccionada e imprime el resultado cifrado.
    No hay parámetros de entrada y no devuelve nada.
    """

    print("Seleccione una opción:")
    print("1.MD5\n2.SHA1\n3.SHA256\n4.SHA512\n5.Salir")
    opcion = input(">> ")
    if opcion == "5":
        return

    try:
        opcion = int(opcion)
    except ValueError:
        print("valor inválido")
        return

    funciones_hash = {
        1: hashlib.md5,
        2: hashlib.sha1,
        3: hashlib.sha256,
        4: hashlib.sha512,
    }
    opcion = funciones_hash.get(opcion, 1)

    texto = input("Texto a cifrar:\n>> ")
    texto_cifrado = cifrar_texto(texto, funciones_hash[opcion])
    print(f"{funciones_hash[opcion].__name__} => {texto_cifrado}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
