import os
import re


def generate_dependencies():
    """
    Analiza los módulos para extraer sus dependencias, genera un diccionario dependencies con la información obtenida.
    """
    dependencies = {}
    root = os.path.join(os.path.dirname(__file__), "../infra/modules")
    modules = os.listdir(root)

    for module in modules:
        content = parce_dependencies(f'{root}/{module}')
        dependencies[f'{module}'] = content

    return dependencies


def parce_dependencies(module) -> list:
    """
    Analiza los archivos 'main.tf' dentro del 'módulo' especificado para extraer dependencias.
    """
    dependencias = []

    patrones = [
        r'module\s*"([^"]+)"',              # module "nombre"
        r'depends_on\s*=\s*\[([^\]]+)\]',   # depends_on = [x, y, z]
        r'var\.([a-zA-Z0-9_-]+)',           # var.nombre_variable
        r'data\.([a-zA-Z0-9_-]+)',          # data.tipo_recurso
        r'source\s*=\s*"../([a-zA-Z0-9_-]+)"',  # source = "../modulo"
    ]

    for archivo in os.listdir(module):
        if archivo.endswith("main.tf"):
            with open(os.path.join(module, archivo), 'r') as f:
                contenido = f.read()
                for patron in patrones[:-1]:
                    coincidencias = re.findall(patron, contenido)
                    dependencias.extend(coincidencias)
                coincidencias_remote = re.findall(patrones[-1], contenido, re.DOTALL)
                for coincidencia in coincidencias_remote:
                    dependencias.append(coincidencia[1])

    return dependencias


def main():
    content = generate_dependencies()
    print(content)


if __name__ == "__main__":
    main()
