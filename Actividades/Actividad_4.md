</p>
  <h1 align="center">Configuración inicial de un Switch</h1>
</p>

## Paso 1: Verifica la configuración predeterminada del switch
### Ingresa al modo EXEC privilegiado.
Puedes acceder a todos los comandos del switch en el modo EXEC privilegiado. Sin embargo, debido a que muchos de los comandos privilegiados configuran parámetros operativos, el acceso privilegiado se debe proteger con una contraseña para evitar el uso no autorizado.

El conjunto de comandos EXEC privilegiado incluye los comandos disponibles en el modo EXEC del usuario, muchos comandos adicionales y el comando configure a través del cual se obtiene acceso a los modos de configuración.

1. Haz clic en S1 y luego en la pestaña CLI. Presione Enter.
2. Ingresa al modo EXEC privilegiado introduciendo el comando enable:
Switch> enable
Switch#
Observa que la solicitud cambió para reflejar el modo EXEC privilegiado.

### Examina la configuración actual del switch.
Ingresa el comando show running-config.
```
Switch# show running-config
```
Responde las siguientes preguntas:<br>

1. **¿Cuántas interfaces Fast Ethernet tiene el switch?** <br>24 interfaces Fast Ethernet<br><br>
2. **¿Cuántas interfaces Gigabit Ethernet tiene el switch?** <br>2 interfaces Gigabit Ethernet<br><br>
3. **¿Cuál es el rango de valores que se muestra para las líneas vty?** <br>De 0 a 15<br><br>
4. **¿Qué comando muestra el contenido actual de la memoria de acceso aleatorio no volátil (NVRAM)? show star** <br>show startup-config<br><br>
5. **¿Por qué el switch responde con "startup-config no está presente"?** <br>Aún no se almacenó ninguna información.

## Paso 2: Crea una configuración básica del switch
### Asigna un nombre a un switch.
Para configurar los parámetros de un switch, quizá deba pasar por diversos modos de configuración. Observa cómo cambia la petición de entrada mientras navega por el switch.
```
Switch# configure terminal
Switch(config)# hostname S1
S1(config)# exit
S1#
```
### Proporciona acceso seguro a la línea de consola.
Para proporcionar un acceso seguro a la línea de la consola, acceda al modo config-line y establezca la contraseña de consola en cesar.
```
S1# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
S1(config)# line console 0
S1(config-line)# password cesar
S1(config-line)# login
S1(config-line)# exit
S1(config)# exit
%SYS-5-CONFIG_I: Configured from console by console
S1#
```
**¿Por qué se requiere el comando login?** <br> Sin el login la contraseña no funciona.

### Verifica que el acceso a la consola sea seguro.
Salimos del modo privilegiado para verificar que la contraseña del puerto de consola esté vigente.
```
S1# exit
Switch con0 is now available
Press RETURN to get started.
User Access Verification
Password:
S1>
```
### Proporciona un acceso seguro al modo privilegiado.
Establece la contraseña de enable en jeka. Esta contraseña protege el acceso al modo privilegiado.
```
S1> enable
S1# configure terminal
S1(config)# enable password jeka
S1(config)# exit
%SYS-5-CONFIG_I: Configured from console by console
S1#
```
### Verifica que el acceso al modo privilegiado sea seguro.
1. Introduce el comando exit nuevamente para cerrar la sesión del switch.
2. Presiona Enter; a continuación, se le pedirá que introduzca una contraseña:
```
User Access Verification
Password:
```
3. La primera contraseña es la contraseña de consola que configuró para line con 0. Introduzca esta contraseña para volver al modo EXEC del usuario.
4. Introduce el comando para acceder al modo privilegiado.
5. Introduce la segunda contraseña que configuró para proteger el modo EXEC privilegiado.
6. Verifica su configuración examinando el contenido del archivo de configuración en ejecución:
```
S1# show running-config
```
Ten en cuenta que la consola y las contraseñas de activación están en texto plano. Esto podría suponer un riesgo para la seguridad si alguien está mirando por encima de su hombro u obtiene acceso a los archivos de configuración almacenados en una ubicación de copia de seguridad. 

### Configura una contraseña encriptada para proporcionar un acceso seguro al modo privilegiado.
La contraseña de enable se debe reemplazar por una nueva contraseña secreta encriptada mediante el comando enable secret. Configura la contraseña de enable secret como itsasecret.
```
S1# config t
S1(config)# enable secret itsasecret
S1(config)# exit
S1#
```
**Nota:** La contraseña de enable secret sobrescribe la contraseña de enable password. Si ambos están configurados en el switch, debes ingresar la contraseña enable secret para ingresar al modo EXEC privilegiado. 

### Verifica si la contraseña de enable secret se agregó al archivo de configuración.
Introduce el comando show running-config nuevamente para verificar si la nueva contraseña de enable secret está configurada.<br>
Nota: Puedes abreviar show running-config como:
```
S1# show run
```
**¿Qué se muestra como contraseña de enable secret?** <br>$1$mERr$ILwq/b7kc.7X/ejA4Aosn0<br><br>
**¿Por qué la contraseña de enable secret se ve diferente de lo que se configuró?** <br>Porque la contraseña está encriptada.
### Encripta las contraseñas de consola y de enable
La contraseña enable secret estaba encriptada, pero las contraseñas enable y console todavía estaban en texto plano.
Encriptamos estas contraseñas de texto no cifrado con el comando service password-encryption.
```
S1# config t
S1(config)# service password-encryption
S1(config)# exit
```

**Si configuras más contraseñas en el switch, ¿se mostrarán como texto no cifrado o en forma cifrada en el archivo de configuración? Explica.**
Las contraseñas se mostrarán en forma cifrada, porque, el comando de configuración se ejecuta solo una vez y las contrasenas posteriores se autoencriptan.

## Configura S2:
![](https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/e7ba2777a716b65c1bfcee2bc8f0d2ea2694e2f0/Im%C3%A1genes/WhatsApp%20Image%202024-05-15%20at%204.38.38%20PM.jpeg)

![](https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/e7ba2777a716b65c1bfcee2bc8f0d2ea2694e2f0/Im%C3%A1genes/WhatsApp%20Image%202024-05-15%20at%204.38.54%20PM.jpeg)
