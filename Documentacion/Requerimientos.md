# Requerimientos generales
* El sistema debe funcionar en la web, para tener acceso desde cualquier parte de colombia
* Preferiblemente, debe ser ligero, sin muchas imagnes, ni contenido pesado, puesto que es primordial que responda rapidamente con datos moviles o redes no muy rapidas
* Debe mostrar toda la informacion del extracto realizado puede ser en un estilo muy similar al de otros software
* Solo pueden cargar informacion los propietarios del sistema
* Debe haber una preconfiguracion de usuario y contraseña, con el posible cambio de la contraseña en caso de ser necesario

## Requisitos funcionales especificos
* Debe poderce cargar un archivo, preferiblmeente pdf, para extraer la infromacin y generar el nuevo extracto
* Debe generar el QR del extracto, que haga referencia a la infromacin plasmada en el extracto
* La persona encargada de los extractos, puede subir un pdf, el cual se procesa internamente, genera el qr y devuelve el pdf con el qr
* Debe haber un endpoint, para subir informacion de manera automatica y posteriormente obtener el qr para que el usuario lo gestione como quiera
* Puede haber un usuario, donde su informacion se guarde automaticamente para que no tenga que iniciar secion posteriormente
* Debe haber una forma de recuperar la contraseña
* Un ligero panel de administracion para ver los extractos cargados y asi mismo cargar uno
* Cualquier usuario al escanear el qr, debe poder observar el extracto

## Requisitos no funcionales
* El programa deberia responder en menos de 2 segundos de manera normal
* La contraseña debe estar encriptada para evitar fraude
* La contraseña debe tener diferentes caracteres para garantizar la seguridad
* Un pequeño endpoind para conexion con otros sistemas
* Para los sitemas extenernos, deben tener premisos
* El programa debe funcionar, tanto para computadores como para pantallas tactiles
* Debe funcionar en google crome, firefox y safari (para dispositivos apple)