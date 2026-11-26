import os
from io import StringIO
from unittest import mock

from django.contrib.auth import authenticate
from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase
from django.urls import reverse

from .models import Usuario

PASSWORD_ADMIN = 'Admin-Segura-2026'
PASSWORD_USUARIO = 'Usuario-Segura-2026'


def crear_usuario(username, password, tipo=Usuario.TipoUsuario.USUARIO):
    return Usuario.objects.create_user(username=username, password=password, tipo_usuario=tipo)


class ModeloUsuarioTests(TestCase):
    def test_no_tiene_campos_de_django_admin(self):
        nombres = {campo.name for campo in Usuario._meta.get_fields()}
        self.assertNotIn('is_staff', nombres)
        self.assertNotIn('is_superuser', nombres)

    def test_columnas_de_la_tabla_usuario(self):
        self.assertEqual(Usuario._meta.db_table, 'usuario')
        columnas = {campo.column for campo in Usuario._meta.concrete_fields}
        self.assertTrue({'nombre', 'contraseña', 'tipo_usuario'}.issubset(columnas))

    def test_guarda_contrasena_hasheada(self):
        usuario = crear_usuario('ana', PASSWORD_USUARIO)
        self.assertNotEqual(usuario.password, PASSWORD_USUARIO)
        self.assertTrue(usuario.check_password(PASSWORD_USUARIO))

    def test_es_administrador_segun_tipo(self):
        admin = crear_usuario('root', PASSWORD_ADMIN, Usuario.TipoUsuario.ADMINISTRADOR)
        usuario = crear_usuario('ana', PASSWORD_USUARIO)
        self.assertTrue(admin.es_administrador)
        self.assertFalse(usuario.es_administrador)


class CrearAdminInicialTests(TestCase):
    def ejecutar(self, **entorno):
        salida = StringIO()
        with mock.patch.dict(os.environ, entorno, clear=False):
            call_command('crear_admin_inicial', stdout=salida)
        return salida.getvalue()

    def test_crea_administrador_preconfigurado(self):
        self.ejecutar(
            DJANGO_ADMIN_USERNAME='admin',
            DJANGO_ADMIN_PASSWORD=PASSWORD_ADMIN,
        )
        admin = Usuario.objects.get(username='admin')
        self.assertEqual(admin.tipo_usuario, Usuario.TipoUsuario.ADMINISTRADOR)
        self.assertTrue(admin.check_password(PASSWORD_ADMIN))

    def test_es_idempotente_y_no_sobrescribe_la_contrasena(self):
        self.ejecutar(DJANGO_ADMIN_USERNAME='admin', DJANGO_ADMIN_PASSWORD=PASSWORD_ADMIN)
        admin = Usuario.objects.get(username='admin')
        admin.set_password('Nueva-Clave-2026')
        admin.save()

        salida = self.ejecutar(DJANGO_ADMIN_USERNAME='admin', DJANGO_ADMIN_PASSWORD=PASSWORD_ADMIN)

        self.assertIn('ya existe', salida)
        self.assertEqual(Usuario.objects.filter(username='admin').count(), 1)
        self.assertTrue(Usuario.objects.get(username='admin').check_password('Nueva-Clave-2026'))

    def test_falla_sin_contrasena(self):
        with mock.patch.dict(os.environ, {'DJANGO_ADMIN_PASSWORD': ''}, clear=False):
            with self.assertRaisesMessage(CommandError, 'DJANGO_ADMIN_PASSWORD'):
                call_command('crear_admin_inicial', stdout=StringIO())
        self.assertFalse(Usuario.objects.exists())

    def test_rechaza_contrasena_debil(self):
        with self.assertRaises(CommandError):
            self.ejecutar(DJANGO_ADMIN_USERNAME='admin', DJANGO_ADMIN_PASSWORD='123')
        self.assertFalse(Usuario.objects.exists())


class LoginTests(TestCase):
    def setUp(self):
        crear_usuario('ana', PASSWORD_USUARIO)

    def test_login_valido_redirige_al_inicio(self):
        respuesta = self.client.post(
            reverse('usuarios:login'), {'username': 'ana', 'password': PASSWORD_USUARIO}
        )
        self.assertRedirects(respuesta, reverse('usuarios:inicio'))

    def test_login_invalido_muestra_error_y_no_autentica(self):
        respuesta = self.client.post(
            reverse('usuarios:login'), {'username': 'ana', 'password': 'incorrecta'}
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_pagina_de_login_responde_sin_sesion(self):
        self.assertEqual(self.client.get(reverse('usuarios:login')).status_code, 200)

    def test_autenticacion_con_backend_de_django(self):
        self.assertIsNotNone(authenticate(username='ana', password=PASSWORD_USUARIO))


class ControlDeAccesoTests(TestCase):
    def setUp(self):
        self.admin = crear_usuario('root', PASSWORD_ADMIN, Usuario.TipoUsuario.ADMINISTRADOR)
        self.usuario = crear_usuario('ana', PASSWORD_USUARIO)

    def test_anonimo_es_redirigido_al_login(self):
        respuesta = self.client.get(reverse('usuarios:dashboard'))
        self.assertRedirects(
            respuesta, f"{reverse('usuarios:login')}?next={reverse('usuarios:dashboard')}"
        )

    def test_usuario_normal_recibe_403_en_panel(self):
        self.client.force_login(self.usuario)
        self.assertEqual(self.client.get(reverse('usuarios:dashboard')).status_code, 403)
        self.assertEqual(self.client.get(reverse('usuarios:usuario_list')).status_code, 403)
        self.assertEqual(self.client.get(reverse('usuarios:usuario_crear')).status_code, 403)

    def test_usuario_normal_no_puede_crear_cuentas(self):
        self.client.force_login(self.usuario)
        respuesta = self.client.post(reverse('usuarios:usuario_crear'), {
            'username': 'intruso',
            'password1': PASSWORD_USUARIO,
            'password2': PASSWORD_USUARIO,
            'tipo_usuario': 'administrador',
        })
        self.assertEqual(respuesta.status_code, 403)
        self.assertFalse(Usuario.objects.filter(username='intruso').exists())

    def test_administrador_accede_al_panel(self):
        self.client.force_login(self.admin)
        self.assertEqual(self.client.get(reverse('usuarios:dashboard')).status_code, 200)
        self.assertEqual(self.client.get(reverse('usuarios:usuario_list')).status_code, 200)

    def test_inicio_redirige_al_panel_si_es_administrador(self):
        self.client.force_login(self.admin)
        self.assertRedirects(self.client.get(reverse('usuarios:inicio')), reverse('usuarios:dashboard'))


class CrearCuentasTests(TestCase):
    def setUp(self):
        self.admin = crear_usuario('root', PASSWORD_ADMIN, Usuario.TipoUsuario.ADMINISTRADOR)
        self.client.force_login(self.admin)

    def test_administrador_crea_usuario_con_tipo(self):
        respuesta = self.client.post(reverse('usuarios:usuario_crear'), {
            'username': 'ana',
            'password1': PASSWORD_USUARIO,
            'password2': PASSWORD_USUARIO,
            'tipo_usuario': 'usuario',
        })
        self.assertRedirects(respuesta, reverse('usuarios:usuario_list'))
        nuevo = Usuario.objects.get(username='ana')
        self.assertEqual(nuevo.tipo_usuario, Usuario.TipoUsuario.USUARIO)
        self.assertTrue(nuevo.check_password(PASSWORD_USUARIO))

    def test_rechaza_contrasena_debil(self):
        respuesta = self.client.post(reverse('usuarios:usuario_crear'), {
            'username': 'ana',
            'password1': '123',
            'password2': '123',
            'tipo_usuario': 'usuario',
        })
        self.assertEqual(respuesta.status_code, 200)
        self.assertFalse(Usuario.objects.filter(username='ana').exists())

    def test_rechaza_nombre_duplicado(self):
        crear_usuario('ana', PASSWORD_USUARIO)
        respuesta = self.client.post(reverse('usuarios:usuario_crear'), {
            'username': 'ana',
            'password1': PASSWORD_USUARIO,
            'password2': PASSWORD_USUARIO,
            'tipo_usuario': 'usuario',
        })
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(Usuario.objects.filter(username='ana').count(), 1)

    def test_listado_muestra_usuarios(self):
        crear_usuario('ana', PASSWORD_USUARIO)
        respuesta = self.client.get(reverse('usuarios:usuario_list'))
        self.assertContains(respuesta, 'ana')


class CambiarPasswordTests(TestCase):
    def test_administrador_cambia_su_contrasena(self):
        admin = crear_usuario('root', PASSWORD_ADMIN, Usuario.TipoUsuario.ADMINISTRADOR)
        self.client.force_login(admin)

        respuesta = self.client.post(reverse('usuarios:password_cambiar'), {
            'old_password': PASSWORD_ADMIN,
            'new_password1': 'Nueva-Clave-2026',
            'new_password2': 'Nueva-Clave-2026',
        })

        self.assertRedirects(respuesta, reverse('usuarios:password_hecho'))
        admin.refresh_from_db()
        self.assertTrue(admin.check_password('Nueva-Clave-2026'))
        self.assertFalse(admin.check_password(PASSWORD_ADMIN))

    def test_contrasena_actual_incorrecta_no_cambia_nada(self):
        admin = crear_usuario('root', PASSWORD_ADMIN, Usuario.TipoUsuario.ADMINISTRADOR)
        self.client.force_login(admin)

        respuesta = self.client.post(reverse('usuarios:password_cambiar'), {
            'old_password': 'mal',
            'new_password1': 'Nueva-Clave-2026',
            'new_password2': 'Nueva-Clave-2026',
        })

        self.assertEqual(respuesta.status_code, 200)
        admin.refresh_from_db()
        self.assertTrue(admin.check_password(PASSWORD_ADMIN))
