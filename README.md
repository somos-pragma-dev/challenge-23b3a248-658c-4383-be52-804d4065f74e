# Desarrollo de una aplicación web con panel de administración

El equipo de desarrollo necesita crear una aplicación web que incluya un panel de administración para gestionar usuarios y productos. La aplicación debe permitir la creación, lectura, actualización y eliminación de usuarios y productos. El panel de administración debe ser accesible solo para usuarios con rol de administrador. La aplicación debe manejar la autenticación y autorización de usuarios.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Aplicación web con Django y panel de administración |
| **Nivel** | junior-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 10 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Configuración inicial y autenticación

**Objetivo:** Configurar el proyecto Django y establecer la autenticación básica de usuarios.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Configurar el proyecto Django.
- Crear modelos para Usuario y Producto.
- Implementar la autenticación básica utilizando el sistema de autenticación de Django.

**Entregable:** Proyecto Django configurado con modelos de Usuario y Producto, y autenticación básica implementada.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo manejar diferentes roles de usuario.
- Piensa en la seguridad de las contraseñas.

</details>

### Fase 2: Creación del panel de administración

**Objetivo:** Crear un panel de administración para gestionar usuarios y productos.

**Tiempo estimado:** 4 horas

**Instrucciones:**

- Crear vistas y plantillas para el panel de administración.
- Implementar funcionalidades CRUD para usuarios y productos.
- Asegurar que solo usuarios con rol de administrador puedan acceder al panel de administración.

**Entregable:** Panel de administración funcional para gestionar usuarios y productos, accesible solo para usuarios con rol de administrador.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo organizar las vistas y plantillas para una navegación intuitiva.
- Piensa en la validación de datos al crear y actualizar usuarios y productos.

</details>

### Fase 3: Pruebas y mejoras

**Objetivo:** Realizar pruebas y realizar mejoras en la aplicación.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Realizar pruebas unitarias y de integración para asegurar la funcionalidad de la aplicación.
- Identificar y corregir errores o inconsistencias.
- Realizar mejoras en la aplicación basadas en las pruebas y retroalimentación.

**Entregable:** Aplicación web con panel de administración funcional, probado y mejorado.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo escribir pruebas efectivas para asegurar la calidad del código.
- Piensa en posibles mejoras para la usabilidad y rendimiento de la aplicación.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una aplicación web con Django y cómo se estructura?
- **paraQueSirve**: ¿Para qué sirve un panel de administración en una aplicación web?
- **comoSeUsa**: ¿Cómo se usa Django para crear una aplicación web con autenticación y autorización?
- **erroresComunes**: ¿Cuáles son los errores comunes al implementar un panel de administración y cómo se pueden evitar?
- **queDecisionesImplica**: ¿Qué decisiones implica el diseño y desarrollo de una aplicación web con Django y panel de administración?

## Criterios de Evaluacion

- Configurar correctamente el proyecto Django y establecer la autenticación básica de usuarios.
- Crear un panel de administración funcional para gestionar usuarios y productos, accesible solo para usuarios con rol de administrador.
- Realizar pruebas unitarias y de integración para asegurar la funcionalidad de la aplicación y realizar mejoras basadas en las pruebas y retroalimentación.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
