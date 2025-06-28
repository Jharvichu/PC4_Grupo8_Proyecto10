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


def generate_diagram_dot():
    """
    Crea el archivo docs/dependencies.dot con todos los módulos y recursos conectados.
    Muestra las relaciones como flechas. Compatible con Graphviz.
    """
    docs_path = os.path.join(os.path.dirname(__file__), "../docs")

    if not os.path.isdir(docs_path):
        print("Creando directorio docs")
        try:
            os.mkdir(docs_path)
        except PermissionError:
            print("Permisos denegados")

    dependencies = generate_dependencies()

    with open(f'{docs_path}/dependencies.dot', 'w') as f:
        f.write('digraph Dependencies {\n')
        for modulo, deps in dependencies.items():
            for dep in deps:
                f.write(f'    "{modulo}" -> "{dep}";\n')
        f.write('}\n')


if __name__ == "__main__":
    generate_diagram_dot()