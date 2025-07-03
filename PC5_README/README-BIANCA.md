
## Cambios a `doc_extractor.py`
- Sección de **Cobertura de documentación**:
  - Cuántas variables y outputs están correctamente documentados.
  - Porcentaje de cobertura de cada uno.
  - Verificación de existencia de un README con descripción válida.
- Tabla detallada de **variables** (nombre, tipo, descripción, valor por defecto).
- Tabla detallada de **outputs** (nombre, descripción, valor).
- Lista de **recursos** definidos en `main.tf`.
 
## ¿Para qué sirve?
### **Auditoria rapida**
Permite identificar de un vistazo qué tanto has documentado tus variables y outputs, evitando que queden elementos sin explicar en tu infraestructura.

### **Medición objetiva**
Al mostrar los porcentajes de cobertura, puedes establecer umbrales mínimos (por ejemplo, 80 %) y enseguida ver si tu módulo los alcanza.

### **Control de calidad de IAC**
Verificar que existe un README con descripción válida garantiza que cada módulo viene acompañado de contexto (qué hace, para qué sirve), esencial para mantenimiento y colaboración en equipo.

## Ejecución

```
Dentro de scripts
python3 doc_extractor.py
```
## Archivos generados

Dentro de la carpeta `docs/` se generan archivos markdown con su nombre,resumen, cobertura, variables documentadas vs total, outputs documentadas vs total, verificacion de existencia de README, tabla de variables, tabla de outputs y lista de recursos.