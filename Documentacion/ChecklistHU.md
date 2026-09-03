# Checklist de Implementación de Historias de Usuario

Checklist local de seguimiento de las historias de usuario del proyecto PlanillasJVRT. Documento de trabajo individual: marca cada casilla a medida que implementas y verificas cada historia.

> **Cómo usar:**
> - `- [ ]` = pendiente por implementar/verificar.
> - `- [x]` = implementada y verificada.
> - Marca el checkbox general de la HU solo cuando **todos** sus criterios estén cumplidos.
> - Usa el campo **Notas** para anotar observaciones, pendientes puntuales o referencias a código.

**Fuente de los criterios:** `Documentacion/HU.md`.
---

- [ ] **Crear un .env para las contraseñas y conexion con la base de datos**
- [ ] **Crear la base de datos**
  - [ ] Crear el diagrama de la base de datos
  - [ ] Crear el script de la base de datos
  - [ ] Crear el contenedor docker para pruebas locales en la db
---

# Historias de usuario funcionales

## HU-001 — Visualización de un extracto al escanear el QR

**Rol:** General (visitante)
**Como** General, **quiero** escanear el QR de un extracto y ver toda su información en el navegador, **para** consultar los datos sin autenticarme.

- [ ] **HU-001 implementada**
  - [ ] Un visitante que escanea un QR válido ve la información completa del extracto al abrir la URL.
  - [ ] Un QR inválido, caducado o inexistente muestra un mensaje de error claro (extracto no encontrado).
  - [ ] La visualización es legible en computadores y dispositivos móviles.

**Notas:**
- [ ]

---

## HU-002 — Control de acceso y roles

**Rol:** Administrador
**Como** Administrador, **quiero** que el sistema restrinja el acceso según roles, **para** que actores externos o no registrados no accedan a funcionalidades internas.

- [ ] **HU-002 implementada**
  - [ ] Un visitante sin sesión que intenta cargar/gestionar extractos es redirigido a iniciar sesión.
  - [ ] Un usuario sin rol de administrador no puede registrar usuarios (acceso denegado).
  - [ ] Cada acción sensible valida el rol del actor antes de ejecutarse.

**Notas:**
- [ ]

---

## HU-003 — Usuario administrador (único inicial)

**Rol:** Administrador
**Como** Administrador, **quiero** contar con un único usuario y contraseña que funcionen como administrador, **para** dar acceso a los demás usuarios.

- [ ] **HU-003 implementada**
  - [ ] El sistema cuenta con un usuario administrador preconfigurado.
  - [ ] El administrador puede crear cuentas para otros usuarios.
  - [ ] El administrador puede cambiar su propia contraseña.

**Notas:**
- [ ]

---

## HU-004 — Carga de archivos PDF o Excel

**Rol:** Usuario/Administrador
**Como** Usuario/Administrador, **quiero** cargar archivos en formato PDF o Excel (.xlsx), **para** ingresar extractos de forma automática.

- [ ] **HU-004 implementada**
  - [ ] Se aceptan archivos `.pdf` y `.xlsx`/`.xls`.
  - [ ] Se rechazan formatos no soportados con un mensaje de error claro.
  - [ ] El tamaño máximo de archivo está controlado para evitar sobrecarga.
  - [ ] La carga funciona desde computadores y pantallas táctiles.

**Notas:**
- [ ]

---

## HU-005 — Procesamiento (extracción de datos) del archivo cargado

**Rol:** Usuario/Administrador
**Como** Usuario/Administrador, **quiero** que el sistema procese automáticamente el archivo cargado para extraer la información del extracto, **para** no capturar los datos manualmente.

- [ ] **HU-005 implementada**
  - [ ] Un archivo PDF o Excel válido extrae los datos del extracto correctamente.
  - [ ] Un archivo no interpretable notifica el error sin dejar datos parciales.
  - [ ] El mecanismo de extracción es genérico y configurable (sujeto a validación de formatos).

**Notas:**
- [ ]

---

## HU-006 — Retorno del archivo PDF con el QR insertado

**Rol:** Usuario/Administrador
**Como** Usuario/Administrador, **quiero** que al cargar un `.pdf` el sistema devuelva ese mismo `.pdf` con el QR insertado, **para** emitir el extracto ya verificable.

- [ ] **HU-006 implementada**
  - [ ] Un PDF cargado regresa con el QR incrustado tras procesarlo y generar el QR.
  - [ ] El PDF devuelto conserva la información original del extracto.
  - [ ] El QR insertado es escaneable y enlaza al extracto (compatible con HU-001).

**Notas:**
- [ ]

---

## HU-007 — Generación de códigos QR (automática o manual)

**Rol:** Usuario/Administrador
**Como** Usuario/Administrador, **quiero** que el sistema genere el QR del extracto automática o manualmente, **para** obtener siempre la referencia verificable.

- [ ] **HU-007 implementada**
  - [ ] Al crear o actualizar un extracto se genera el QR de forma automática.
  - [ ] El usuario puede solicitar la generación manual del QR de un extracto existente.
  - [ ] El QR hace referencia a la información plasmada en el extracto.
  - [ ] El sistema devuelve el QR tras el ingreso de un extracto.

**Notas:**
- [ ]

---

## HU-008 — Inicio de sesión

**Rol:** Usuario/Administrador
**Como** Usuario/Administrador, **quiero** iniciar sesión con usuario y contraseña, **para** acceder a las funcionalidades internas.

- [ ] **HU-008 implementada**
  - [ ] Se puede iniciar sesión con credenciales válidas.
  - [ ] Con credenciales incorrectas se muestra un mensaje de error y no se concede acceso.
  - [ ] La contraseña se valida contra un almacenamiento cifrado (ver HU-NF-01).

**Notas:**
- [ ]

---

## HU-009 — Recuperación de contraseña por el administrador

**Rol:** Administrador
**Como** Administrador, **quiero** poder restablecer la contraseña de un usuario registrado, **para** que recupere el acceso cuando la haya olvidado.

- [ ] **HU-009 implementada**
  - [ ] El administrador puede reasignar/restablecer la contraseña de cualquier usuario.
  - [ ] Solo el administrador puede realizar esta acción.
  - [ ] El usuario afectado debe volver a autenticarse con la nueva contraseña.

**Notas:**
- [ ]

---

## HU-010 — Consultas con filtros complejos

**Rol:** Usuario/Administrador
**Como** Usuario/Administrador, **quiero** realizar consultas mediante filtros complejos, **para** localizar rápidamente información específica.

- [ ] **HU-010 implementada**
  - [ ] Se pueden filtrar por cadenas de texto libres.
  - [ ] Se pueden filtrar por placa.
  - [ ] Se pueden filtrar por persona.
  - [ ] Se pueden filtrar por fechas (rango).
  - [ ] Es posible combinar varios filtros a la vez.

**Notas:**
- [ ]

---

## HU-011 — Panel de administración para registro de usuarios

**Rol:** Administrador
**Como** Administrador, **quiero** un panel de administración para registrar nuevos usuarios y gestionar, **para** administrar los accesos al sistema.

- [ ] **HU-011 implementada**
  - [ ] El panel permite registrar nuevos usuarios.
  - [ ] El panel permite asignar el rol (Administrador/Usuario) a cada usuario.
  - [ ] Solo accesible por el administrador.
  - [ ] El panel también permite cargar y visualizar extractos (ver HU-013 y HU-014).

**Notas:**
- [ ]

---

## HU-012 — Ingreso de extractos por formulario (manual) o archivo (automático)

**Rol:** Usuario/Administrador
**Como** Usuario/Administrador, **quiero** ingresar extractos de forma manual o automática, **para** registrarlos según lo más cómodo para cada caso.

- [ ] **HU-012 implementada**
  - [ ] Es posible crear un extracto completando un formulario manualmente.
  - [ ] Es posible crear un extracto cargando un archivo.
  - [ ] Ambos caminos generan el QR correspondiente (ver HU-007).
  - [ ] Solo los propietarios/usuarios autorizados pueden cargar información.

**Notas:**
- [ ]

---

## HU-013 — Visualización de extractos en el panel de administración

**Rol:** Usuario/Administrador
**Como** Usuario/Administrador, **quiero** ver en el panel los extractos ya cargados, **para** tener una vista consolidada y operar sobre ellos.

- [ ] **HU-013 implementada**
  - [ ] El panel lista los extractos cargados.
  - [ ] Desde el panel se puede cargar un nuevo extracto.

**Notas:**
- [ ]

---

## HU-014 — Modificación y eliminación de extractos

**Rol:** Usuario/Administrador
**Como** Usuario/Administrador, **quiero** modificar y eliminar extractos existentes, **para** mantener la información actualizada y correcta.

- [ ] **HU-014 implementada**
  - [ ] Se puede editar la información de un extracto existente.
  - [ ] Se puede eliminar un extracto.
  - [ ] Toda modificación regenera/actualiza el QR correspondiente (ver HU-007).
  - [ ] Solo usuarios autorizados pueden modificar o eliminar.

**Notas:**
- [ ]

---

## HU-015 — Endpoint para sistemas externos (ingestión y QR)

**Rol:** Sistema externo
**Como** Sistema externo autorizado, **quiero** un endpoint que permita subir información automáticamente y obtener el QR, **para** integrar la generación de extractos verificables en mis procesos.

- [ ] **HU-015 implementada**
  - [ ] Existe un endpoint accesible por sistemas externos autorizados.
  - [ ] Se requiere permiso/autenticación para utilizarlo.
  - [ ] Al enviar la información, el endpoint devuelve el QR para que el sistema externo lo gestione.
  - [ ] El extracto queda registrado y visible en el panel.

**Notas:**
- [ ]

---

# Historias de usuario no funcionales

## HU-NF-01 — Cifrado de contraseñas

**Rol:** Administrador/Usuario
**Como** Administrador/Usuario, **quiero** que las contraseñas se almacenen con un método de cifrado seguro, **para** prevenir fraudes y proteger los accesos.

- [ ] **HU-NF-01 implementada**
  - [ ] Las contraseñas nunca se almacenan en texto plano.
  - [ ] Se usa un algoritmo de cifrado/hashing seguro irreverssible.

**Notas:**
- [ ]

---

## HU-NF-02 — Contraseñas con requisitos de seguridad

**Rol:** Usuario/Administrador
**Como** Usuario/Administrador, **quiero** usar contraseñas con diferentes tipos de caracteres, **para** garantizar la seguridad de la cuenta.

- [ ] **HU-NF-02 implementada**
  - [ ] La contraseña combina caracteres de distintas categorías (mayúsculas, minúsculas, números y/o símbolos).
  - [ ] El sistema valida la fortaleza de la contraseña al crearla o cambiarla.

**Notas:**
- [ ]

---

## HU-NF-03 — Rendimiento: tiempos de respuesta

**Rol:** Usuario/Administrador/Visitante
**Como** Usuario/Administrador/Visitante, **quiero** que el sistema responda rápidamente, **para** una experiencia fluida incluso con redes móviles o lentas.

- [ ] **HU-NF-03 implementada**
  - [ ] Las solicitudes de visitantes responden en máximo 1 segundo.
  - [ ] Las solicitudes de usuarios y administradores responden en máximo 2 segundos.
  - [ ] La interfaz es ligera, sin imágenes ni contenido pesado, para responder bien con datos móviles.

**Notas:**
- [ ]

---

## HU-NF-04 — Soporte de usuarios simultáneos

**Rol:** Administrador
**Como** Administrador, **quiero** que el sistema soporte al menos 100 usuarios simultáneos sin degradación significativa, **para** dar servicio confiable a toda la organización.

- [ ] **HU-NF-04 implementada**
  - [ ] El sistema soporta 100 usuarios concurrentes sin degradación notable en el rendimiento.

**Notas:**
- [ ]

---

## HU-NF-05 — Escalabilidad

**Rol:** Administrador
**Como** Administrador, **quiero** que el sistema escale verticalmente y que la base de datos soporte crecimiento continuo, **para** crecer sin afectar el rendimiento.

- [ ] **HU-NF-05 implementada**
  - [ ] El sistema puede escalar verticalmente (más recursos en el mismo servidor).
  - [ ] La base de datos soporta crecimiento progresivo de datos sin perjudicar el rendimiento.

**Notas:**
- [ ]

---

## HU-NF-06 — Disponibilidad

**Rol:** Administrador
**Como** Administrador, **quiero** que el sistema esté disponible al menos el 99.96% del tiempo, **para** garantizar acceso permanente a los extractos y al QR.

- [ ] **HU-NF-06 implementada**
  - [ ] El sistema mantiene una disponibilidad mínima del 99.96%.

**Notas:**
- [ ]

---

## HU-NF-07 — Portabilidad entre navegadores

**Rol:** Usuario/Visitante
**Como** Usuario/Visitante, **quiero** que el sistema funcione en los navegadores modernos Chrome, Firefox, Opera y Safari, **para** usarlo desde cualquier navegador o dispositivo.

- [ ] **HU-NF-07 implementada**
  - [ ] El sistema funciona correctamente en Chrome, Firefox, Opera y Safari.
  - [ ] Es funcional en computadores y pantallas táctiles (dispositivos móviles/tabletas).

**Notas:**
- [ ]

---

## HU-NF-08 — Mantenibilidad y estándares

**Rol:** Desarrollador
**Como** Desarrollador, **quiero** que el código tenga documentación y cumpla estándares de desarrollo, **para** mantener y evolucionar el sistema fácilmente.

- [ ] **HU-NF-08 implementada**
  - [ ] El código cuenta con documentación adecuada.
  - [ ] Se siguen estándares de desarrollo.
  - [ ] La arquitectura permite agregar nuevas funcionalidades sin afectar las existentes.

**Notas:**
- [ ]

---

## HU-NF-09 — Pruebas unitarias e integración

**Rol:** Desarrollador/Administrador
**Como** Desarrollador/Administrador, **quiero** que el sistema cuente con pruebas unitarias y de integración que se ejecuten antes de cada despliegue, **para** garantizar la calidad y evitar regresiones.

- [ ] **HU-NF-09 implementada**
  - [ ] Existen pruebas unitarias.
  - [ ] Existen pruebas de integración.
  - [ ] Las pruebas se ejecutan antes de cualquier despliegue y deben pasar.

**Notas:**
- [ ]

---

# Notas generales de seguimiento

- **Bloqueos / deudas técnicas:**
  - [ ]
- **Decisiones pendientes:**
  - [ ]
- **Próximos pasos:**
  - [ ]
