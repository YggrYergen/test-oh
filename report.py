import os
import sys
import json
import subprocess
from datetime import datetime

CONFIG_FILE = 'report_config.json'

def es_binario(file_path):
    """
    Determina si un archivo es binario.
    """
    try:
        with open(file_path, 'rb') as file:
            chunk = file.read(1024)
            if b'\0' in chunk:
                return True
        return False
    except Exception:
        return False

def obtener_detalles_archivo(file_path):
    """
    Obtiene detalles como tamaño y fecha de última modificación.
    """
    try:
        tamaño = os.path.getsize(file_path)
        ultima_mod = os.path.getmtime(file_path)
        ultima_mod = datetime.fromtimestamp(ultima_mod).strftime('%Y-%m-%d %H:%M:%S')
        return tamaño, ultima_mod
    except Exception:
        return 'Desconocido', 'Desconocido'

def preguntar_inclusion(tipo, nombre):
    while True:
        respuesta = input(f"¿Deseas incluir {tipo} '{nombre}'? (Y/N): ").strip().lower()
        if respuesta in ('y', 'n'):
            return respuesta == 'y'
        else:
            print("Por favor, responde 'Y' o 'N'.")

def recorrer_directorio(directorio_actual, estructura, contenidos, configuracion, nivel=0):
    contenido = []
    try:
        contenido = os.listdir(directorio_actual)
    except Exception as e:
        print(f"Error al listar el directorio {directorio_actual}: {e}")
        return

    for item in sorted(contenido):
        item_path = os.path.join(directorio_actual, item)
        indent = '  ' * nivel

        if os.path.isdir(item_path):
            clave = f"dir::{os.path.relpath(item_path)}"
            if clave in configuracion:
                incluir_carpeta = configuracion[clave]
            else:
                incluir_carpeta = preguntar_inclusion('la carpeta', item_path)
                configuracion[clave] = incluir_carpeta

            if incluir_carpeta:
                estructura.append(f"{indent}- {item}/\n")
                contenidos.append(f"{indent}## {item}\n\n")
                contenidos.append(f"{indent}**Ruta:** `{item_path}/`\n\n")
                recorrer_directorio(item_path, estructura, contenidos, configuracion, nivel + 1)
        elif os.path.isfile(item_path):
            clave = f"file::{os.path.relpath(item_path)}"
            if clave in configuracion:
                incluir_archivo = configuracion[clave]
            else:
                incluir_archivo = preguntar_inclusion('el archivo', item_path)
                configuracion[clave] = incluir_archivo

            if incluir_archivo:
                estructura.append(f"{indent}- {item}\n")
                tamaño, ultima_mod = obtener_detalles_archivo(item_path)
                contenidos.append(f"{indent}### {item}\n\n")
                contenidos.append(f"{indent}**Tamaño:** {tamaño} bytes, **Última Modificación:** {ultima_mod}\n\n")
                if not es_binario(item_path):
                    try:
                        with open(item_path, 'r', encoding='utf-8', errors='replace') as file:
                            contenido_archivo = file.read()
                            # Detectar el lenguaje según la extensión
                            _, ext = os.path.splitext(item)
                            lenguaje = ext.lstrip('.').lower() if ext else ''
                            contenidos.append(f"{indent}```{lenguaje}\n{contenido_archivo}\n{indent}```\n\n")
                    except Exception as e:
                        contenidos.append(f"{indent}(Error leyendo el archivo: {e})\n\n")
                else:
                    contenidos.append(f"{indent}(Archivo binario, no se muestra el contenido)\n\n")

def main():
    directorio_actual = os.getcwd()
    estructura = []
    contenidos = []
    encabezado = []
    encabezado.append(f"# Reporte de Directorio `{directorio_actual}`\n\n")
    encabezado.append(f"**Generado el:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

    configuracion = {}

    # Cargar configuración previa si existe
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            configuracion = json.load(f)
        while True:
            respuesta = input("Se encontró una configuración previa. ¿Deseas usarla? (Y/N): ").strip().lower()
            if respuesta == 'y':
                print("Usando configuración previa...")
                break
            elif respuesta == 'n':
                print("Se usará una nueva configuración.")
                configuracion = {}
                break
            else:
                print("Por favor, responde 'Y' o 'N'.")

    recorrer_directorio(directorio_actual, estructura, contenidos, configuracion)

    # Guardar la configuración actual
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(configuracion, f, ensure_ascii=False, indent=2)

    # Unir la estructura y los contenidos
    output = encabezado
    output.append("## Estructura de Archivos Incluidos\n\n")
    output.extend(estructura)
    output.append("\n---\n\n")
    output.extend(contenidos)

    # Guardar la salida en un archivo .md
    try:
        with open("report_complete.md", "w", encoding='utf-8') as file:
            file.write(''.join(output))
        print("\nProceso completado exitosamente. El reporte se ha guardado en 'report_complete.md'.")
        
        # ── Nueva sección: abrir en VS Code ──
        try:
            # Ponemos shell=True para que Python use la misma resolución de comandos
            subprocess.run(f'code "{os.path.abspath("report_complete.md")}"', 
                        shell=True, check=True)
            print("Abriendo report_complete.md en VS Code…")
        except Exception:
            print(
                "No se pudo abrir en VS Code. "
                "Comprueba que el comando 'code' esté disponible en tu shell."
            )

    except Exception as e:
        print(f"\nError al escribir el archivo de reporte: {e}")

if __name__ == "__main__":
    main()
