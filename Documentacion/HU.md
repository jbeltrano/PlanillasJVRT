# Historias de Usuario

Documento de historias de usuario derivadas de los requisitos en `Requerimientos.md` y `Requisitos.md`. Cada historia sigue el formato **Como `<rol>`, quiero `<funcionalidad>`, para `<beneficio>`**, acompañada de criterios de aceptación en formato *Given/When/Then* y trazabilidad hacia los requisitos de origen.

> **Nota sobre decisiones pendientes:**
> - RF-5 deja abierto si el parser de archivos será específico para ciertos formatos o genérico. Se asume un **parser genérico** (configurable), sujeto a validación.
> - RF-8 vs RNF-3: la recuperación de contraseña la realiza el **administrador** (prevalece RNF-3).

## Roles (actores)

| Actor | Descripción |
|-------|-------------|
| General / Visitante | Cualquier persona que escanea un QR y visualiza un extracto sin registrarse |
| Usuario | Persona interna de la empresa, registrada y con sesión iniciada |
| Administrador | Usuario con permisos de gestión del sistema (registro de usuarios, gestión total de extractos) |
| Sistema externo | Sistema ajeno a la plataforma con permisos autorizados, conectado vía endpoint |

---

## Simbolismo de los criterios

- **Dado (Given):** condición previa.
- **Cuando (When):** acción del actor.
- **Entonces (Then):** resultado esperado.

---

# Historias de usuario funcionales

## HU-001 — Visualización de un extracto al escanear el QR

**Como** General (visitante), **quiero** poder escanear el código QR de un extracto y ver toda su información en el navegador, **para** consultar los datos del extracto sin necesidad de autenticarme.

**Criterios de aceptación:**
- Dado que un visitante escanea un QR válido, cuando abre la URL vinculada, entonces ve la información completa del extracto asociado.
- Dado un QR inválido, caducado o inexistente, cuando el visitante lo escanea, entonces se muestra un mensaje de error claro (extracto no encontrado).
- La visualización debe ser legible en computadores y dispositivos móviles.

**Trazabilidad:** RF-1, RNF-13

---

## HU-002 — Control de acceso y roles

**Como** Administrador, **quiero** que el sistema restrinja el acceso según roles (Administrador, Usuario, General), **para** que actores externos o no registrados no accedan a funcionalidades internas.

**Criterios de aceptación:**
- Dado un visitante sin sesión, cuando intenta cargar o gestionar extractos, entonces se le redirige a iniciar sesión.
- Dado un usuario sin el rol de administrador, cuando intenta registrar usuarios, entonces el sistema le deniega el acceso.
- Cada acción sensible valida el rol del actor antes de ejecutarse.

**Trazabilidad:** RF-2, RNF-2

---

## HU-003 — Usuario administrador (único inicial)

**Como** Administrador, **quiero** contar con un único usuario y contraseña que funcionen como administrador del sistema, **para** dar acceso a los demás usuarios.

**Criterios de aceptación:**
- El sistema cuenta con un usuario administrador preconfigurado.
- El administrador puede crear cuentas para otros usuarios.
- El administrador puede cambiar su propia contraseña.

**Trazabilidad:** RF-3

---

## HU-004 — Carga de archivos PDF o Excel

**Como** Usuario/Administrador, **quiero** cargar archivos en formato PDF o Excel (.xlsx), **para** ingresar extractos de forma automática.

**Criterios de aceptación:**
- Se aceptan archivos con extensión `.pdf` y `.xlsx`/`.xls`.
- Se rechazan formatos no soportados con un mensaje de error claro.
- El tamaño máximo de archivo está controlado para evitar sobrecarga.
- La carga es posible desde computadores y pantallas táctiles.

**Trazabilidad:** RF-4, RNF-12

---

## HU-005 — Procesamiento (extracción de datos) del archivo cargado

**Como** Usuario/Administrador, **quiero** que el sistema procese automáticamente el archivo cargado para extraer la información del extracto, **para** no tener que capturar los datos manualmente.

**Criterios de aceptación:**
- Dado un archivo PDF o Excel válido, cuando se carga, entonces el sistema extrae los datos del extracto correctamente.
- Dado un archivo que no puede interpretarse, cuando se procesa, entonces se notifica el error sin dejar datos parciales.
- El mecanismo de extracción es genérico y configurable (sujeto a validación de formatos).

**Trazabilidad:** RF-5, RNF-11

---

## HU-006 — Retorno del archivo PDF con el QR insertado

**Como** Usuario/Administrador, **quiero** que al cargar un archivo `.pdf` el sistema me devuelva ese mismo `.pdf` con el código QR insertado, **para** entregar/emitir el extracto ya verificable.

**Criterios de aceptación:**
- Dado un PDF cargado, cuando el sistema lo procesa y genera el QR, entonces devuelve el PDF con el QR incrustado.
- El PDF devuelto conserva la información original del extracto.
- El QR insertado es escaneable y enlaza al extracto (funciona con HU-001).

**Trazabilidad:** RF-14

---

## HU-007 — Generación de códigos QR (automática o manual)

**Como** Usuario/Administrador, **quiero** que el sistema genere el código QR del extracto, ya sea automáticamente tras una acción o manualmente a petición, **para** obtener siempre la referencia verificable del extracto.

**Criterios de aceptación:**
- Dado un extracto creado o actualizado, cuando se confirma la acción, entonces se genera el QR de forma automática.
- El usuario puede solicitar la generación manual del QR de un extracto existente.
- El QR hace referencia a la información plasmada en el extracto.
- El sistema devuelve el QR tras el ingreso de un extracto.

**Trazabilidad:** RF-6, RF-13

---

## HU-008 — Inicio de sesión

**Como** Usuario/Administrador, **quiero** iniciar sesión con usuario y contraseña, **para** acceder a las funcionalidades internas del sistema.

**Criterios de aceptación:**
- Se puede iniciar sesión con credenciales válidas.
- Con credenciales incorrectas se muestra un mensaje de error y no se concede acceso.
- La contraseña se valida contra un almacenamiento cifrado (ver HU-NF-01).

**Trazabilidad:** RF-7, RNF-1

---

## HU-009 — Recuperación de contraseña por el administrador

**Como** Administrador, **quiero** poder restablecer la contraseña de un usuario registrado, **para** que el usuario recupere el acceso cuando la haya olvidado.

**Criterios de aceptación:**
- El administrador puede reasignar/restablecer la contraseña de cualquier usuario.
- Solo el administrador puede realizar esta acción.
- El usuario afectado debe volver a autenticarse con la nueva contraseña.

**Trazabilidad:** RF-8, RNF-3

---

## HU-010 — Consultas con filtros complejos

**Como** Usuario/Administrador, **quiero** realizar consultas sobre los extractos mediante filtros complejos (cadenas de texto, placas, personas y fechas), **para** localizar rápidamente información específica.

**Criterios de aceptación:**
- Se pueden filtrar por cadenas de texto libres.
- Se pueden filtrar por placa.
- Se pueden filtrar por persona.
- Se pueden filtrar por fechas (rango).
- Es posible combinar varios filtros a la vez.

**Trazabilidad:** RF-9

---

## HU-011 — Panel de administración para registro de usuarios

**Como** Administrador, **quiero** un panel de administración para registrar nuevos usuarios y gestionar, **para** administrar los accesos al sistema.

**Criterios de aceptación:**
- El panel permite registrar nuevos usuarios.
- El panel permite asignar el rol (Administrador/Usuario) a cada usuario.
- Solo accesible por el administrador.
- El panel también permite cargar y visualizar extractos (ver HU-013 y HU-014).

**Trazabilidad:** RF-10

---

## HU-012 — Ingreso de extractos por formulario (manual) o archivo (automático)

**Como** Usuario/Administrador, **quiero** ingresar extractos de forma manual (rellenando un formulario) o automática (cargando un archivo `.xlsx` o `.pdf`), **para** registrar extractos de la manera que resulte más cómoda según el caso.

**Criterios de aceptación:**
- Es posible crear un extracto completando un formulario manualmente.
- Es posible crear un extracto cargando un archivo.
- Ambos caminos generan el QR correspondiente (ver HU-007).
- Solo los propietarios/usuarios autorizados pueden cargar información.

**Trazabilidad:** RF-11, Requerimientos generales (solo propietarios cargan información)

---

## HU-013 — Visualización de extractos en el panel de administración

**Como** Usuario/Administrador, **quiero** ver en el panel de administración los extractos ya cargados, **para** tener una vista consolidada y poder operar sobre ellos.

**Criterios de aceptación:**
- El panel lista los extractos cargados.
- Desde el panel se puede cargar un nuevo extracto.

**Trazabilidad:** Requerimiento general (panel ligero), RF-13

---

## HU-014 — Modificación y eliminación de extractos

**Como** Usuario/Administrador, **quiero** poder modificar y eliminar extractos existentes, **para** mantener la información del sistema actualizada y correcta.

**Criterios de aceptación:**
- Se puede editar la información de un extracto existente.
- Se puede eliminar un extracto.
- Toda modificación regenera/actualiza el QR correspondiente (ver HU-007).
- Solo usuarios autorizados pueden modificar o eliminar.

**Trazabilidad:** RF-12

---

## HU-015 — Endpoint para sistemas externos (ingestión y QR)

**Como** Sistema externo autorizado, **quiero** un endpoint que permita subir información de manera automática y obtener el QR, **para** integrar la generación de extractos verificables en mis propios procesos.

**Criterios de aceptación:**
- Existe un endpoint accesible por sistemas externos autorizados.
- Se requiere permiso/autenticación para utilizarlo.
- Al enviar la información, el endpoint devuelve el QR para que el sistema externo lo gestione.
- El extracto queda registrado y visible en el panel.

**Trazabilidad:** RF-13 (endpoint), RNF-14, Requerimientos generales (endpoint automático)

---

# Historias de usuario no funcionales

## HU-NF-01 — Cifrado de contraseñas

**Como** Administrador/Usuario, **quiero** que las contraseñas se almacenen con un método de cifrado seguro, **para** prevenir fraudes y proteger los accesos.

**Criterios de aceptación:**
- Las contraseñas nunca se almacenan en texto plano.
- Se usa un algoritmo de cifrado/hashing seguro irreverssible.

**Trazabilidad:** RNF-1, Requerimientos generales

---

## HU-NF-02 — Contraseñas con requisitos de seguridad

**Como** Usuario/Administrador, **quiero** usar contraseñas que incluyan diferentes tipos de caracteres, **para** garantizar la seguridad de la cuenta.

**Criterios de aceptación:**
- La contraseña debe combinar caracteres de distintas categorías (mayúsculas, minúsculas, números y/o símbolos).
- El sistema valida la fortaleza de la contraseña al crearla o cambiarla.

**Trazabilidad:** Requerimientos generales (contraseña con diferentes caracteres)

---

## HU-NF-03 — Rendimiento: tiempos de respuesta

**Como** Usuario/Administrador/Visitante, **quiero** que el sistema responda rápidamente, **para** una experiencia fluida incluso con redes móviles o lentas.

**Criterios de aceptación:**
- Las solicitudes de visitantes responden en máximo 1 segundo.
- Las solicitudes de usuarios y administradores responden en máximo 2 segundos.
- La interfaz es ligera, sin imágenes ni contenido pesado, para responder bien con datos móviles.

**Trazabilidad:** RNF-4, RNF-5, Requerimientos generales

---

## HU-NF-04 — Soporte de usuarios simultáneos

**Como** Administrador, **quiero** que el sistema soporte al menos 100 usuarios simultáneos sin degradación significativa, **para** dar servicio confiable a toda la organización.

**Criterios de aceptación:**
- El sistema soporta 100 usuarios concurrentes sin degradación notable en el rendimiento.

**Trazabilidad:** RNF-6

---

## HU-NF-05 — Escalabilidad

**Como** Administrador, **quiero** que el sistema escale verticalmente y que la base de datos soporte crecimiento continuo, **para** crecer sin afectar el rendimiento.

**Criterios de aceptación:**
- El sistema puede escalar verticalmente (más recursos en el mismo servidor).
- La base de datos soporta crecimiento progresivo de datos sin perjudicar el rendimiento.

**Trazabilidad:** RNF-7, RNF-8

---

## HU-NF-06 — Disponibilidad

**Como** Administrador, **quiero** que el sistema esté disponible al menos el 99.96% del tiempo, **para** garantizar acceso permanente a los extractos y al QR.

**Criterios de aceptación:**
- El sistema mantiene una disponibilidad mínima del 99.96%.

**Trazabilidad:** RNF-9

---

## HU-NF-07 — Portabilidad entre navegadores

**Como** Usuario/Visitante, **quiero** que el sistema funcione en los navegadores modernos Chrome, Firefox, Opera y Safari (incluidos dispositivos Apple), **para** poder usarlo desde cualquier navegador o dispositivo.

**Criterios de aceptación:**
- El sistema funciona correctamente en Chrome, Firefox, Opera y Safari.
- Es funcional en computadores y pantallas táctiles (dispositivos móviles/tabletas).

**Trazabilidad:** RNF-12, Requerimientos generales

---

## HU-NF-08 — Mantenibilidad y estándares

**Como** Desarrollador, **quiero** que el código tenga documentación y cumpla estándares de desarrollo, **para** mantener y evolucionar el sistema fácilmente.

**Criterios de aceptación:**
- El código cuenta con documentación adecuada.
- Se siguen estándares de desarrollo.
- La arquitectura permite agregar nuevas funcionalidades sin afectar las existentes.

**Trazabilidad:** RNF-10, RNF-11

---

## HU-NF-09 — Pruebas unitarias e integración

**Como** Desarrollador/Administrador, **quiero** que el sistema cuente con pruebas unitarias y de integración que se ejecuten antes de cada despliegue, **para** garantizar la calidad y evitar regresiones.

**Criterios de aceptación:**
- Existen pruebas unitarias.
- Existen pruebas de integración.
- Las pruebas se ejecutan antes de cualquier despliegue y deben pasar.

**Trazabilidad:** RNF-15, RNF-16, RNF-17

---

## Resumen de trazabilidad

| HU | Requisitos de origen |
|----|----------------------|
| HU-001 | RF-1, RNF-13 |
| HU-002 | RF-2, RNF-2 |
| HU-003 | RF-3 |
| HU-004 | RF-4, RNF-12 |
| HU-005 | RF-5, RNF-11 |
| HU-006 | RF-14 |
| HU-007 | RF-6, RF-13 |
| HU-008 | RF-7, RNF-1 |
| HU-009 | RF-8, RNF-3 |
| HU-010 | RF-9 |
| HU-011 | RF-10 |
| HU-012 | RF-11 |
| HU-013 | Const. generales, RF-13 |
| HU-014 | RF-12 |
| HU-015 | RNF-14, const. generales |
| HU-NF-01 | RNF-1 |
| HU-NF-02 | Const. generales |
| HU-NF-03 | RNF-4, RNF-5 |
| HU-NF-04 | RNF-6 |
| HU-NF-05 | RNF-7, RNF-8 |
| HU-NF-06 | RNF-9 |
| HU-NF-07 | RNF-12, const. generales |
| HU-NF-08 | RNF-10, RNF-11 |
| HU-NF-09 | RNF-15, RNF-16, RNF-17 |
