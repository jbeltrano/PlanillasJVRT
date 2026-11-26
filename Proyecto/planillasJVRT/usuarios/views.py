from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView

from .forms import UsuarioCreationForm
from .models import Usuario


class SoloAdministradorMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Anónimos van al login; usuarios sin rol de administrador reciben 403."""

    def test_func(self):
        return self.request.user.es_administrador

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            raise PermissionDenied
        return super().handle_no_permission()


class InicioView(LoginRequiredMixin, TemplateView):
    template_name = 'usuarios/inicio.html'

    def get(self, request, *args, **kwargs):
        if request.user.es_administrador:
            return redirect('usuarios:dashboard')
        return super().get(request, *args, **kwargs)


class DashboardView(SoloAdministradorMixin, TemplateView):
    template_name = 'usuarios/panel/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_usuarios'] = Usuario.objects.count()
        return context


class UsuarioListView(SoloAdministradorMixin, ListView):
    model = Usuario
    template_name = 'usuarios/panel/usuario_list.html'
    context_object_name = 'usuarios'
    ordering = ('username',)


class UsuarioCreateView(SoloAdministradorMixin, CreateView):
    model = Usuario
    form_class = UsuarioCreationForm
    template_name = 'usuarios/panel/usuario_form.html'
    success_url = reverse_lazy('usuarios:usuario_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Usuario "{self.object.username}" creado correctamente.')
        return response


class CambiarPasswordView(PasswordChangeView):
    template_name = 'usuarios/password_change.html'
    success_url = reverse_lazy('usuarios:password_hecho')


class CambiarPasswordHechoView(PasswordChangeDoneView):
    template_name = 'usuarios/password_change_done.html'
