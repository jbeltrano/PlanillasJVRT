# PlanillasJVRT
Este es un proyecto donde las empresas de transporte pueden adicionar el método de validación por QR a los extractos o planillas.
Este es un proyecto enfocado en la generacion de qr para los extractos o planillas, realizadas por las empresas de transporte, para que estos sean verificables.

## Desarrolladores
| Nombre | Contacto |
|--------|----------|
| Juan David Beltran Orjuela | juanpdnejoh@gmail.com |


# Despliegue

## Despliegue local
Para desplegar el sistema localmente, es necesario tener python instalado, se recomienda tener la imagen de la base de datos en un contenedor de docker


## Despliegue docker

El proyecto incluye un `docker-compose.yml` con dos servicios: `db` (PostgreSQL 16) y
`web` (Django servido con gunicorn). Antes de levantar el stack, copia `.env.example`
a `.env` y ajusta las credenciales y el `DJANGO_SECRET_KEY`.

```bash
docker compose up -d --build      # construye y levanta todo
docker compose ps                 # estado de los contenedores
docker compose logs -f web        # logs de Django/gunicorn
docker compose down               # detiene los contenedores (conserva la base de datos)
docker compose down -v            # detiene y borra también el volumen de PostgreSQL
```

La aplicación queda disponible en <http://localhost:8000/cuentas/login/> (o el puerto indicado
en `WEB_PORT`). Al arrancar, el contenedor `web` aplica las migraciones, crea el administrador
inicial si no existe y recolecta los archivos estáticos automáticamente.

### Rebuilds rápidos

El `Dockerfile` está pensado para que los cambios de código no reinstalen dependencias:

- `requirements.txt` se copia en una capa aparte, así que editar archivos `.py` solo
  invalida la última capa (`COPY` del código): el rebuild tarda unos segundos.
- Las dependencias se instalan con cache de pip de BuildKit, por lo que cambiar
  `requirements.txt` tampoco vuelve a descargar los paquetes ya cacheados.
- `.dockerignore` excluye `venv/`, `__pycache__/` y `.git/` para que el contexto de
  build sea pequeño.

Si se modifica el código, basta con:

```bash
docker compose up -d --build
```

Gunicorn no recarga código en caliente; el contenedor se recrea con la nueva imagen.
Para desarrollo con recarga automática se puede ejecutar `runserver` con el código
montado como volumen.

## Probar desde internet (Cloudflare Tunnel)

El compose incluye dos servicios de túnel desactivados por defecto mediante
`profiles`, así que `docker compose up -d --build` no expone nada a internet.

### Túnel rápido (pruebas puntuales, sin cuenta)

```bash
docker compose --profile tunnel-quick up -d
docker compose logs -f tunnel-quick   # la URL https://<algo>.trycloudflare.com aparece aquí
```

La URL es aleatoria y cambia cada vez que se reinicia el contenedor. Para cerrarlo:

```bash
docker compose stop tunnel-quick
```

`.env` ya incluye `.trycloudflare.com` en `DJANGO_ALLOWED_HOSTS` y
`https://*.trycloudflare.com` en `DJANGO_CSRF_TRUSTED_ORIGINS`, por lo que el túnel
rápido funciona sin tocar configuración. (En `ALLOWED_HOSTS` el comodín de subdominios
se escribe con punto inicial: `.trycloudflare.com`.)

> El túnel rápido expone la página de inicio de sesión a internet. Úsalo en sesiones
> cortas y no lo dejes corriendo de forma permanente. Usa una contraseña de administrador fuerte.

> **Si el túnel no conecta** y en los logs aparecen errores como
> `Failed to dial a quic connection`, `HTTP/2 connection is blocked` o
> `TLS handshake with edge error`, la red está bloqueando la salida hacia el edge de
> Cloudflare (TCP y UDP **7844**). Hay que permitir ese puerto en firewall/router, usar
> otra red (por ejemplo, un hotspot móvil) o recurrir a un túnel que salga por 443.

### Túnel con nombre (cuando exista dominio propio)

1. Añade el dominio a Cloudflare y crea un túnel en
   **Zero Trust → Networks → Tunnels**.
2. Configura el hostname público, por ejemplo `dev.tudominio.com` → `http://web:8000`.
3. Copia el token en `.env`:

   ```env
   CLOUDFLARE_TUNNEL_TOKEN=eyJ...
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,web,dev.tudominio.com
   DJANGO_CSRF_TRUSTED_ORIGINS=https://dev.tudominio.com
   ```

4. Aplica los cambios y arranca el túnel:

   ```bash
   docker compose up -d --build
   docker compose --profile tunnel up -d
   ```

Opcionalmente se puede añadir una política de **Cloudflare Access** (por ejemplo,
OTP por correo) para que solo los invitados puedan entrar al entorno de pruebas.

## Usuarios y administrador

El módulo `usuarios` reemplaza la autenticación por defecto de Django. La tabla `usuario`
sigue el diseño de `db/init_script.sql`: `nombre`, `contraseña` y `tipo_usuario`
(`administrador` o `usuario`). No hay panel de Django; la gestión se hace en la aplicación.

### Administrador inicial

Al arrancar, `entrypoint.sh` ejecuta `python manage.py crear_admin_inicial`, que toma estas
variables del `.env`:

```env
DJANGO_ADMIN_USERNAME=admin
DJANGO_ADMIN_PASSWORD=cambia_esta_clave_por_una_segura
```

- Si el usuario ya existe, el comando **no lo modifica**; así no se revierte una contraseña
  cambiada desde la aplicación.
- `DJANGO_ADMIN_PASSWORD` es obligatoria la primera vez. Sin ella (o si no cumple los
  validadores de contraseña) el contenedor no arranca.

### Rutas

| Ruta | Descripción | Acceso |
|------|-------------|--------|
| `/cuentas/login/` | Inicio de sesión | Público |
| `/cuentas/logout/` | Cerrar sesión | Autenticado |
| `/cuentas/password/` | Cambiar la contraseña propia | Autenticado |
| `/panel/` | Panel de administración | Administrador |
| `/panel/usuarios/` | Listado de usuarios | Administrador |
| `/panel/usuarios/nuevo/` | Crear cuenta de usuario | Administrador |

Los usuarios sin rol de administrador que intenten entrar al panel reciben `403`.

### Pruebas

```bash
docker compose exec web python manage.py test usuarios
```