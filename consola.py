from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def imprimir_tabla(tabla_valor: dict):
    table = Table(title="Tabla de Símbolos", show_lines=True)
    table.add_column("Valor", justify="center", style="green")
    table.add_column("Símbolo", justify="center", style="green")

    for valor, simbolo in tabla_valor.items():
        table.add_row(str(valor), str(simbolo))
    
    console.print(table)

def imprimir_resultado(mensaje_encriptado: str, mensaje_desencriptado: str):
    table = Table(title="Resultado de Desencriptación", show_lines=True)
    table.add_column("Mensaje Encriptado", style="green")
    table.add_column("Mensaje Desencriptado", style="green")
    table.add_row(mensaje_encriptado, mensaje_desencriptado)
    console.print(table)

def imprimir_semilla_inverso(semilla: int, inverso: int):
    console.print(f"Semilla encontrada: [bold green]{semilla}[/]")
    console.print(f"Inverso multiplicativo: [bold green]{inverso}[/]\n")
