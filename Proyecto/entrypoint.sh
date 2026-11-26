#!/bin/sh
set -e

echo "==> Aplicando migraciones"
python manage.py migrate --noinput

echo "==> Creando administrador inicial (si no existe)"
python manage.py crear_admin_inicial

echo "==> Recolectando archivos estáticos"
python manage.py collectstatic --noinput

echo "==> Iniciando aplicación"
exec "$@"
