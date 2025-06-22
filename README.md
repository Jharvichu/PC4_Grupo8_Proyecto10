# PC4_Grupo8_Proyecto10

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