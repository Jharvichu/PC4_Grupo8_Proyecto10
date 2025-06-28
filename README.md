# PC4_Grupo8_Proyecto10

## Archivo `setup.sh`

**Archivo importante, ejecutar al inicio.**

Este archivo automatiza la creación del setup adecuado para trabajar en este proyecto. Realiza las siguientes operaciones:

- Crea el entorno virtual `venv`. (si es que aún no está creado)
- Activa dicho entorno.
- Instalar las dependencias dentro de `requirements.txt` (si es que existe).
- Mueve los hooks de `hooks/` (`pre-commit`, `commit-msg` y `pre-push`) al directorio `.git/hooks/` y les de permisos de ejecución.

Dicho script bash se puede ejecutar de la siguiente manera

```
source setup.sh
```

Cabe mencionar que algunos comandos dentro de `setup.sh` (como `source venv/bin/activate`) solamente funcionan en sistemas tipo Unix, por lo cual, si se usa otro sistema operativo simplemente dichos comandos no tendrán efecto.

## Hooks

### pre-commit

- Impide commits directamente en ramas protegidas: `main`, `develop`, `release`.
- Realiza validaciones rápidas solamente para los archivos staged para commit.
- Ejecuta linter Python (`flake8`) solo en archivos `.py` staged, reportando errores críticos.
- Ejecuta `terraform fmt -check` solo en archivos `.tf` staged, verificando que estén bien formateados.
- Ejemplo:
  ```bash
  flake8 --select=E9,F63,F7,F82 --show-source archivo.py
  terraform fmt -check archivo.tf
  ```
- Si algún archivo Python tiene un error crítico o algún archivo terraform no está bien formateado, el commit se cancela.

### commit-msg

- Valida que el mensaje de commit siga la estructura definida.
- No permite mensajes que no sigan la estructura.
- Formato requerido:
  ```
  <tipo>([alcance]): (Issue #n) descripción corta
  ```
  Ejemplo:
  ```
  feat(hook): (Issue #12) validar mensajes de commit
  ```

### pre-push

- Ejecuta validaciones automáticas antes de subir cambios al repositorio remoto.
- Corre linters python (`flake8`) sobre todo el proyecto.
- Valida formato de archivos terraform (`terraform fmt -check`).
- Ejecuta pruebas automáticas (`pytest`) y se exige un porcentaje mínimo de cobertura (≥80%).
- Permite el push si no hay tests, mostrando solo una advertencia.
- Secuencia:
  ```bash
  flake8 .
  terraform fmt -check
  pytest
  ```

## carpeta Modules
### root_dir/
Función:
Crea un directorio raíz en el sistema de archivos local. Este directorio actúa como la base de la infraestructura sobre la cual se construyen los demás componentes.

### config_files/
Función:
Genera archivos de configuración (main.conf, app.conf) dentro del directorio raíz.
Dependencia: Requiere que root_dir haya creado correctamente su estructura.

### service_dir/
Función:
Crea un subdirectorio (secondary_service/) dentro del directorio raíz y un archivo representativo de un servicio secundario (service_data.txt).
Dependencia: Depende tanto de root_dir como de los archivos generados en `config_files`.

### summary_creator/
Función:
Ejecuta un script mediante null_resource y local-exec que genera un archivo `summary.txt` dentro del directorio raíz. Este archivo resume las rutas de los archivos y directorios creados por los módulos anteriores.
Dependencia: Depende explícitamente de todos los módulos previos.

### Archivos importantes en la raíz
main.tf
Este archivo orquesta la integración de los módulos, pasando variables y conectando las salidas entre sí, garantizando que las dependencias estén explícitamente modeladas.

### Instrucciones de Ejecución

```
Desde la raiz:

terraform init

terraform apply
```

### Resultado Esperado
Al ejecutar correctamente terraform apply, se debe crear una estructura como esta:


### Estructura generada por Terraform
#### infra_local/
Este es el directorio raíz de la infraestructura local. Fue creado por el módulo root_dir. Todo lo demás se construye dentro de él.

#### main.conf y app.conf
Estos son archivos de configuración básicos.
Fueron generados por el módulo config_files dentro del directorio raíz infra_local/. Simulan archivos que una aplicación o servicio podría necesitar para funcionar.

#### secondary_service/
 Ubicación: infra_local/secondary_service/

Este es un subdirectorio que representa un servicio secundario dentro de la infraestructura. Fue creado por el módulo service_dir.

#### service_data.txt
Este archivo está dentro del subdirectorio secondary_service/.
Contiene información ficticia o simulada, como si fuera la configuración o datos de ese servicio.

#### summary.txt
Este archivo fue generado por el módulo summary_creator, usando un script que corre localmente con `null_resource` y `local-exec`.
Contiene un resumen de todos los recursos creados por los otros módulos: rutas, nombres de archivo, etc. Sirve como una forma de validar que todo fue creado y que las dependencias se resolvieron correctamente.

El archivo summary.txt contendrá información sobre los directorios y archivos creados por cada módulo, verificando que las dependencias funcionaron correctamente.


#### diagram_generator.py

## Responsabilidad de `generate_dependencies()`:

- Busca todos los subdirectorios en `infra/modules/`.
- Lee los archivos `main.tf` dentro de cada módulo.
- Extrae dependencias como:
- Módulos usados (`module "..."`)
- Recursos referenciados con `depends_on = [...]`
- Variables (`var.algo`)
- Recursos `data` (`data.tipo.nombre`)
- Fuentes de otros módulos (`source = "../modulo"`)

## Ejecucion:

Dentro de scripts/

```
python3 diagram_generator.py
```


## Resultados:
Un archivo con un grafo en lenguaje DOT que describe las dependencias entre nodos; representa como los módulos y variables estan relacionados y tienen dependencias entre si. Se puede usar para generar diagramas .png con `Graphivz`.

