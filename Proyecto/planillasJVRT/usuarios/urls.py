from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path(
        'cuentas/login/',
        auth_views.LoginView.as_view(template_name='usuarios/login.html', redirect_authenticated_user=True),
        name='login',
    ),
    path('cuentas/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cuentas/password/', views.CambiarPasswordView.as_view(), name='password_cambiar'),
    path('cuentas/password/hecho/', views.CambiarPasswordHechoView.as_view(), name='password_hecho'),
    path('panel/', views.DashboardView.as_view(), name='dashboard'),
    path('panel/usuarios/', views.UsuarioListView.as_view(), name='usuario_list'),
    path('panel/usuarios/nuevo/', views.UsuarioCreateView.as_view(), name='usuario_crear'),
]
