@echo off
setlocal

echo ========================================
echo   Configurando proyecto Django
echo ========================================

REM Crear entorno virtual si no existe
if not exist "venv" (
    echo Creando entorno virtual...
    python -m venv venv
) else (
    echo El entorno virtual ya existe.
)

REM Activar entorno virtual
call venv\Scripts\activate.bat

REM Actualizar pip
echo Actualizando pip...
python -m pip install --upgrade pip

REM Instalar dependencias
if exist "requirements.txt" (
    echo Instalando dependencias...
    python -m pip install -r requirements.txt
) else (
    echo ADVERTENCIA: No se encontro requirements.txt
)

REM Crear proyecto Django
if not exist "planillasJVRT" (
    echo Creando proyecto Django...
    django-admin startproject planillasJVRT
) else (
    echo El proyecto planillasJVRT ya existe.
)

echo.
echo ========================================
echo   Configuracion terminada
echo ========================================
pause