import sys
import argparse
import json
from decrypt import cargar_config, calcular_semilla, desencriptar

sys.stdout.reconfigure(encoding='utf-8')

def main():
    parser = argparse.ArgumentParser(description="Desencriptador modular")
    parser.add_argument("-c", "--config", type=str, required=True, help="Archivo JSON de configuración")
    args = parser.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        config = json.load(f)

    tabla_valor, tabla_simbolo, modulo, b, datos_descubiertos, mensaje_encriptado, semilla = cargar_config(config)

    semilla = calcular_semilla(tabla_simbolo, datos_descubiertos, b, modulo, semilla)
    if semilla is None:
        print("Error: No se pudo calcular la semilla. Asegure al menos dos datos descubiertos válidos.")
        return

    desencriptar(tabla_valor, tabla_simbolo, mensaje_encriptado, b, semilla)

if __name__ == "__main__":
    main()
