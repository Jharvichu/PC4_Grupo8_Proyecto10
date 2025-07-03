# Módulo <null>

<null>

### Variables

| Nombre | Tipo | Descripción | Default |
|--------|------|-------------|---------|
| root_path | string
 | Ruta absoluta del directorio raíz de la infraestructura. | <null> |
| config_files | list(string)
 | Lista de rutas de archivos de configuración generados. | <null> |
| service_name | string
 | Nombre lógico del servicio secundario. | <null> |
| service_path | string
 | Ruta absoluta del subdirectorio del servicio secundario. | <null> |
| service_file | string
 | Ruta del archivo de datos del servicio secundario. | <null> |
| service_data_id | string
 | ID del archivo de datos del servicio secundario (para dependencias explícitas). | <null> |
| depends_on_resources | list(any)
  default     = []
 | Lista de recursos de los que depende este módulo para generar el resumen. | [] |

### Outputs

| Nombre | Descripción | Valor |
|--------|-------------|-------|
| summary_file | Ruta del archivo resumen generado por este módulo. | ${var.root_path |

### Recursos

- null_resource create_summary
