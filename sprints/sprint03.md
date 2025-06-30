[Video del Sprint 03](https://unipe-my.sharepoint.com/:f:/g/personal/luis_alanya_c_uni_pe/EhtGzayR_yxImugh8lIdsyEBnHnMLsvhf50CpsYyiFJBcg?e=xpwUTF)

## Archivo `test_terraform_docs_validation.py`

Tests para validar la relación entre archivos Terraform y su documentación en formato Markdown que se genera.

### Funciones probadas:
- `obtener_modulos()`: Obtiene la lista de módulos disponibles en el directorio.
- `parsear_doc_variables()`: Extrae variables documentadas de archivos Markdown.
- `parsear_doc_outputs()`: Extrae outputs documentados de archivos Markdown.
- `verificar_variables()`: Compara variables Terraform con documentación.
- `verificar_outputs()`: Compara outputs Terraform con documentación.

### Tests implementados:

**Tests de variables por módulo:**
- **`test_variables_root_dir`**: Verifica que variables del módulo `root_dir` estén correctamente documentadas.
- **`test_variables_config_files`**: Confirma documentación completa de variables en módulo `config_files`.

**Tests de outputs por módulo:**
- **`test_outputs_root_dir`**: Valida que outputs del módulo `root_dir` coincidan con documentación.
- **`test_outputs_config_files`**: Verifica outputs del módulo `config_files` estén documentados.

**Tests globales:**
- **`test_todos_modulos_variables`**: Valida variables de todos los módulos detectados automáticamente.
- **`test_todos_modulos_outputs`**: Verifica outputs de todos los módulos del proyecto.

### Técnicas usadas:
- Fixtures pytest para configuración reutilizable del validador.
- Expresiones regulares para parsear tablas Markdown de variables y outputs.
- Operaciones de conjuntos para detectar elementos faltantes o extra.
- Validación automática de consistencia entre código Terraform y documentación.