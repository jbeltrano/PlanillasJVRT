# Requisitos Funcionales
| ID | REQUISITO | ACTOR |
|----|-----------|-------|
| RF-1 | El sistema, debe permitir visualizar toda la informacion referente a un extracto de contrato, luego de escanear el codigo QR | General |
| RF-2 | El sistema debe restringir el acceso a actores externos o diferentes a los usuarios registrados por los propietarios del sisstema | Administradores |
| RF-3 | Hay un unico usuario con su respectiva contraseña que funciona de admin, para dar acceso a los demas usuarios | Admin |
| RF-4 | El sistema debe permitir la cargue de archivos tanto en formato pdf, como en formato excel | Usuarios/Adimin |
| RF-5 | Cuando se carguen archivos, el sistema debe ser capaz de procesarlos para extrear la informacion correspondiente a los extractos (Por determinar si va a ser especifico para ciertos formatos o si se va a implementar un parser) | Usuarios/Admin |
| RF-6 | El sistema debe generar los codigos QR, ya sea de manera automatica despues de una accion o manual, solicitado por el usuario | Usuario/Admin |
| RF-7 | El sistema debe proveer inicio de sesion para los usuarios internos de la empresa | Usuario/Admin |
| RF-8 | El sistema permite la recuperacion de contraseñas para los diferentes usuarios | Usuario/Admin |
| RF-9 | El sistema debe permitir a los usuarios registrados y logueados la realizacion de consultas por filtros complejos (Cadenas de texto, Placas, Personas y fechas) | Usuario/Administrador |
| RF-10 | El sistema muestra un panel de administracion, para el registro de nuevos usuarios | Admin |
| RF-11 | El sistema debe permitir a los usuarios ingresar extractos, ya sea de manera manual (Rellenando un formulario) o automatica (Cargando un archivo en formato .xlsx o .pdf) | Usuario/Admin |
| RF-12 | El sistema debe permitir la modificacion, y eliminacion de extractos | Usuario/Admin |
| RF-13 | El sistema debe retornar el codigo QR luego de hacer un ingreso de un extracto | Usuario/Admin |
| RF-14 | Cuando se carge un archivo de extencion .pdf, el sistema debe retornar este .pdf, con el codigo qr insertado en el pdf | Usuario/Admin |

# Requisitos No Funcionales
## Seguridad
| ID | REQUISITO |
|----|-----------|
| RNF-1 | Las contraseñas deben estar con algun metodo de cifrado seguro para tal fin |
| RNF-2 | Deben existir control por roles (Usuario, Administrador, General o visitante) |
| RNF-3 | La recuperacion de contraseñas, debe realizarce por el administrador del sistema |

## Rendimiento
| ID | REQUISITO |
|----|-----------|
| RNF-4 | El sistema debe responder a las solicitudes de los visitantes en un tiempo maximo de 1 segundo |
| RNF-5 | El sistema debe responder a solicitudes realizadas por los usuarios y administradores en un maximo de 2 segundos |
| RNF-6 |El sistema debe soportar almenos 100 usuarios simultaneos sin degradacion significativa en las respuestas |

## Escalabilidad
| ID | REQUISITO |
|----|-----------|
| RNF-7 | El sistema debe poder escalar verticalmente sin inconvenientes |
| RNF-8 | La base de datos debe soportar el crecimiento continuo y progresivo sin afectar el rendimiento |

## Disponibilidad
| ID | REQUISITO |
|----|-----------|
| RNF-9 | El sistema debe estar al menos un 99.96% disponible para cualquiera de los usuarios del sistema |

## Mantenibilidad
| ID | REQUISITO |
|----|-----------|
| RNF-10 | El codigo debe tener algun tipo de documentacion y cumplir con estandares de desarrollo |
| RNF-11 | La arquitectura a utilizar debe permitir agregar de manera facil nuevas funcionalidades sin afectar las existentes |

## Portabilidad
| ID | REQUISITO |
|----|-----------|
| RNF-12 | El sistema debe funcionar en los navegadores modernos: Chrome, Firefox, Opera y Safari |

## Usabilidad
| ID | REQUISITO |
|----|-----------|
| RNF-13 | La visualizacion de los extractos, debe ser clara y con informacion completa y con una estructura que permita buena legibilidad en dispositivos moviles |

## Interoperabilidad
| RNF-14 | El sistema debe exponer un pequeño endpoint para que otros sistemas autorizados puedan ingresar extractos y obtener su respectivo codigo QR |

## Calidad
| ID | REQUISITO | ACTOR |
|----|-----------|-------|
| RNF-15 | El sistema debe tener test unitarios |
| RNF-16 | El sistema debe tener test de integracion |
| RNF-17 | los test deben ejecutarce antes de cualquier despliegue |