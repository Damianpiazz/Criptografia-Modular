from collections import OrderedDict
from consola import imprimir_tabla, imprimir_semilla_inverso, imprimir_resultado

def cargar_config(config: dict):
    tabla_valor = OrderedDict(sorted({int(k): v for k, v in config.get("tabla", {}).items()}.items()))
    tabla_simbolo = {v: k for k, v in tabla_valor.items()}
    
    modulo = len(tabla_valor)
    b = int(config.get("b", 0)) % modulo
    datos_descubiertos = config.get("datos_descubiertos", {})
    mensaje_encriptado = config.get("mensaje_encriptado", "")
    semilla = config.get("semilla")

    return tabla_valor, tabla_simbolo, modulo, b, datos_descubiertos, mensaje_encriptado, semilla

def inverso_multiplicativo(a: int, modulo: int) -> int:
    for i in range(1, modulo):
        if (a * i) % modulo == 1:
            return i
    raise ValueError(f"No existe inverso para {a} módulo {modulo}")

def calcular_semilla(tabla_simbolo: dict, datos_descubiertos: dict, b: int, modulo: int, semilla_existente=None):
    if semilla_existente is not None:
        return semilla_existente

    if len(datos_descubiertos) < 2:
        return None

    pares = [
        (tabla_simbolo[orig], tabla_simbolo[enc])
        for orig, enc in datos_descubiertos.items()
        if orig in tabla_simbolo and enc in tabla_simbolo
    ]

    for a in range(1, modulo):
        if all((a * X + b) % modulo == Y for X, Y in pares):
            return a

    return None

def desencriptar(tabla_valor: dict, tabla_simbolo: dict, mensaje_encriptado: str, b: int, semilla: int):
    inverso = inverso_multiplicativo(semilla, len(tabla_valor))
    imprimir_semilla_inverso(semilla, inverso)

    resultado = []
    for c in mensaje_encriptado:
        if c in tabla_simbolo:
            Y = tabla_simbolo[c]
            X = ((Y - b) * inverso) % len(tabla_valor)
            resultado.append(tabla_valor.get(X, '?'))
        else:
            resultado.append(c)

    mensaje = ''.join(resultado)
    imprimir_tabla(tabla_valor)
    imprimir_resultado(mensaje_encriptado, mensaje)
    return mensaje
