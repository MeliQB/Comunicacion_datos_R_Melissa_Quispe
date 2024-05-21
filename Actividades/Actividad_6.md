<p align="left">
  <h1 align="center"> Crear una red con un switch y un router - Modo Físico</h1>
</p>

## Topología

<p align="center">
  <img src="https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/576b24a4c499238cc79f853c5f5405a1689ae3de/Im%C3%A1genes/Captura%20de%20pantalla%202024-05-15%20165102.png">
</p>

## Tabla de asignación de direcciones

<p align="center">
  <img src="https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/576b24a4c499238cc79f853c5f5405a1689ae3de/Im%C3%A1genes/imagen_2024-05-15_165229219.png">
</p>

## Paso 1: Configura la topología de red
1. Mueva el router y el switch requeridos del Estante al Rack.
2. Mueva los PCs requeridos del Estante a la Mesa.
3. Conecta los dispositivos como se muestra en la Topologia y en la Tabla de asignación de
direcciones.
4. Encienda todos los dispositivos.

## Paso 2: Configurar los dispositivos y verificar la conectividad
### Asignar información de IP estática a las interfaces de la PC
1. Configura la dirección IP, la máscara de subred y los parámetros del gateway predeterminado en la PC-A.
2. Configura la dirección IP, la máscara de subred y los parámetros del gateway predeterminado en la PC-B.
3. En una ventana con el símbolo del sistema en la PC-A, haga ping a la PC-B.
<p align= "center">
  <img src="" width="600">
</p>

### Configura el router
1. Acceda al router mediante el puerto de consola y habilite el modo EXEC con privilegios.
2. Ingresa al modo de configuración.
3. Asigna el nombre de dispositivo al router.
4. Asigna class como la contraseña cifrada del modo EXEC privilegiado.
5. Asigna cisco como la contraseña de la consola y habilite el inicio de sesión.
6. Asigne cisco como la contraseña de vty y habilite el inicio de sesión.
7. Encripta las contraseñas de texto sin formato.
8. Crea un aviso que advierta a todo el que acceda al dispositivo que el acceso no autorizado está prohibido.
9. Configura y activa las dos interfaces en el router.
<p align= "center">
  <img src="https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/a9490a3d9ddee138438b10b1b1514e4c7bead04a/Im%C3%A1genes/imagen_2024-05-20_231956645.png">
</p>

10. Configura una descripción de interfaz para cada interfaz e indique qué dispositivo está conectado.
11. Para habilitar el enrutamiento IPv6, ingrese el comando ipv6 unicast-routing.
12. Guardar la configuración en ejecución en el archivo de configuración de inicio
13. Configura el reloj en el router.<br>
**Nota:** Utiliza el signo de interrogación (?) para poder determinar la secuencia correcta de
parámetros necesarios para ejecutar este comando.
