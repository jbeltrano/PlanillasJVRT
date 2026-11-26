import os

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError

from usuarios.models import Usuario


class Command(BaseCommand):
    help = (
        'Crea el usuario administrador inicial a partir de DJANGO_ADMIN_USERNAME '
        'y DJANGO_ADMIN_PASSWORD. Si el usuario ya existe, no lo modifica.'
    )

    def handle(self, *args, **options):
        username = os.getenv('DJANGO_ADMIN_USERNAME', 'admin').strip()
        password = os.getenv('DJANGO_ADMIN_PASSWORD', '')

        if Usuario.objects.filter(username=username).exists():
            self.stdout.write(f'El administrador "{username}" ya existe; no se modifica.')
            return

        if not password:
            raise CommandError(
                'La variable DJANGO_ADMIN_PASSWORD es obligatoria para crear el administrador inicial.'
            )
        try:
            validate_password(password)
        except ValidationError as error:
            raise CommandError('La contraseña del administrador no cumple los requisitos: ' + ' '.join(error.messages))

        Usuario.objects.create_user(
            username=username,
            password=password,
            tipo_usuario=Usuario.TipoUsuario.ADMINISTRADOR,
        )
        self.stdout.write(self.style.SUCCESS(f'Administrador "{username}" creado correctamente.'))
