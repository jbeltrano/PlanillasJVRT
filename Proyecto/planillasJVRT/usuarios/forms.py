from django.contrib.auth.forms import UserCreationForm

from .models import Usuario


class UsuarioCreationForm(UserCreationForm):
    """Alta de cuentas desde el panel. Valida la contraseña con AUTH_PASSWORD_VALIDATORS."""

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username', 'tipo_usuario')
