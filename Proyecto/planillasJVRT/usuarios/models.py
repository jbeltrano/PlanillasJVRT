from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('El nombre de usuario es obligatorio.')
        usuario = self.model(username=username, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, username, password=None, **extra_fields):
        # Permite que `createsuperuser` cree un administrador (tipo_usuario).
        extra_fields.setdefault('tipo_usuario', Usuario.TipoUsuario.ADMINISTRADOR)
        return self.create_user(username, password, **extra_fields)


class Usuario(AbstractBaseUser):
    class TipoUsuario(models.TextChoices):
        ADMINISTRADOR = 'administrador', 'Administrador'
        USUARIO = 'usuario', 'Usuario'

    username = models.CharField(
        'nombre',
        max_length=150,
        unique=True,
        validators=[UnicodeUsernameValidator()],
        error_messages={'unique': 'Ya existe un usuario con este nombre.'},
        db_column='nombre',
    )

    password = models.CharField('contraseña', max_length=128, db_column='contraseña')
    tipo_usuario = models.CharField(
        'tipo de usuario',
        max_length=20,
        choices=TipoUsuario.choices,
        default=TipoUsuario.USUARIO,
    )

    is_active = models.BooleanField('activo', default=True)
    date_joined = models.DateTimeField('fecha de alta', default=timezone.now)

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'usuario'
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        constraints = [
            models.CheckConstraint(
                condition=models.Q(tipo_usuario__in=['administrador', 'usuario']),
                name='usuario_tipo_usuario_valido',
            ),
        ]

    @property
    def es_administrador(self):
        return self.tipo_usuario == self.TipoUsuario.ADMINISTRADOR
