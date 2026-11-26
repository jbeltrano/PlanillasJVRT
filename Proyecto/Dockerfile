# syntax=docker/dockerfile:1

# ============================================================
# Etapa 1: instalación de dependencias
# ============================================================
FROM python:3.12-slim AS builder

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_INPUT=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /build

# Solo requirements.txt primero: si el archivo no cambia, Docker reutiliza
# esta capa (y el pip install) aunque el código del proyecto cambie.
COPY requirements.txt ./

# Cache mount de BuildKit: reutiliza los wheels ya descargados entre builds,
# incluso cuando requirements.txt sí cambia.
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# ============================================================
# Etapa 2: runtime
# ============================================================
FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

# curl se usa para el healthcheck del contenedor.
# psycopg[binary] ya incluye libpq, por eso no se instala libpq5.
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Usuario sin privilegios para ejecutar la aplicación.
RUN useradd --create-home --uid 1000 appuser

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv

# El código va al final: es la única capa que se invalida al editar archivos,
# por eso los rebuilds posteriores son de pocos segundos.
COPY --chown=appuser:appuser planillasJVRT/ ./planillasJVRT/
COPY --chown=appuser:appuser --chmod=755 entrypoint.sh ./entrypoint.sh

USER appuser

WORKDIR /app/planillasJVRT

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
    CMD curl -fsS http://127.0.0.1:8000/admin/login/ || exit 1

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "planillasJVRT.wsgi:application", \
     "--bind", "0.0.0.0:8000", \
     "--workers", "3", \
     "--timeout", "60", \
     "--access-logfile", "-", \
     "--error-logfile", "-"]
