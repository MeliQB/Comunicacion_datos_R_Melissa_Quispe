# Comunicaciones de TCP y UDP

## Paso 1: Genera tráfico de red en modo de simulación y vea multiplexación
### Genera tráfico para completar las tablas del protocolo de resolución de direcciones (ARP)
Realiza la siguiente tarea para reducir la cantidad de tráfico de red que se ve en la simulación.
1. Haz clic en MultiServer y luego haz click en **Desktop** tab > **Command Prompt**.
2. Ingresa el comando **ping -n 1 192.168.1.255**. Está haciendo ping a la dirección broadcast de la LAN del cliente. La opción de comando enviará sólo una solicitud de ping en lugar de las cuatro habituales. Esto tomará unos segundos ya que cada dispositivo en la red responde a la solicitud de ping de MultiServer.
3. Cierra la ventana **MultiServer**.
<p aling = "center" >
  <img src="https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/6a6dfc05ff92e2ff950ffcc0f75542823620a63a/Im%C3%A1genes/imagen_2024-05-20_235327605.png">
</p>
   
**Nota:** El comando "-n 1" envía solo una solicitud de ping, aunque en el terminal se muestren cuatro envíos. Esto se debe a cómo funciona el comando en un prompt de Windows real, donde obedece al comando y envía una sola solicitud.
**Nota 2:** La cantidad de solicitudes enviadas depende del número especificado en el comando. Por ejemplo, si se utiliza el comando "n -2", se enviarán dos solicitudes en lugar de una.

<p aling = "center" >
  <img src="https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/9c0d0e663485a9837cb0e65becf1e04007823a9f/Im%C3%A1genes/imagen_2024-05-20_235729597.png">
</p>

### Genera tráfico web (HTTP)
1. Cambia a modo de simulación.
2. Haz clic en **Cliente HTTP** y abre el **Explorador Web** desde el escritorio.
3. En el campo URL, introduce **192.168.1.254** y haz clic en **Go** (Ir). Los sobres (PDU) aparecerán en la ventana de topología.
4. Minimiza, pero no cierres, la ventana de configuración de **HTTP Client**.

### Genera tráfico FTP
1. Haz clic en **FTP Client** y abra el **Command Prompt** desde el escritorio
2. Introduce el comando **ftp 192.168.1.254**. Las PDU aparecerán en la ventana de simulación.
3. Minimiza, pero no cierres, la ventana de configuración de **FTP Client**.
<p alin = "center">
  <img src = "https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/9c0d0e663485a9837cb0e65becf1e04007823a9f/Im%C3%A1genes/imagen_2024-05-20_235729597.png">
</p>
    
### Genera tráfico DNS
1. Haz clic en DNS Client y abra el **Command Prompt**.
2. Introduce el comando **nslookup multiserver.pt.ptu**. Aparecerá una PDU en la ventana de simulación.
3. Minimiza, pero no cierre, la ventana de configuración de **DNS Client**.

<p alin = "center">
  <img src = "https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/f8add32ff0425c3d9d24c73fded5c817f98a08c7/Im%C3%A1genes/imagen_2024-05-21_000241457.png">
</p>

### Genera tráfico de correo electrónico
1. Haz clic en **E-Mail Client** y abre la herramienta **E Mail** desde el escritorio.
2. Haz clic en **Compose** (Redactar) y escribe la siguiente información:
```
To: user@multiserver.pt.ptu
Subject: Personalizar la línea de asunto
E-Mail Body: Personalizar el correo electrónico
```
3. Haz clic en **Send** (Enviar).
4. Minimiza, pero no cierres, la ventana de configuración de **E-Mail Client**.

### Verifica que se haya generado tráfico y que esté preparado para la simulación
Ahora debería haber entradas de PDU en el panel de simulación para cada uno de los equipos cliente.

### Examina la multiplexación a medida que el tráfico cruza la red
Ahora utilizarás el **botón Capturar/Reenviar** del Panel de Simulación para observar los diferentes protocolos que viajan por la red.

1. Haz clic una vez en **Capture/Forward**. Todas las PDU se transfieren al switch.
2. <p alin = "center">
  <img src = "https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/7cc0fb873def3d5afe779583ea7909fed8756afd/Im%C3%A1genes/imagen_2024-05-21_000412279.png">
</p>

3. Haz clic en **Capturar/Reenviar** seis veces y observe las PDU de los diferentes hosts mientras viajan por la red. Observe que solo una PDU puede cruzar un cable en cada dirección en un momento determinado.


#### ¿Cómo se llama esto?
Se llama multiplexacion, esto es transmitir varios datos por un mismo medio, uno por uno.<br>

#### Aparece una variedad de PDU en la lista de eventos en el Panel de simulación. ¿Cuál es el significado de los diferentes colores?
Los colores nos muestran los protocolos de cada PDU, sean HTTP, FTP, etc.

## Paso 2: Examinar la funcionalidad de los protocolos TCP y UDP
### Examinar el tráfico HTTP cuando los clientes se comunican con el servidor
1. Haz clic en **Reset Simulation (Restablecer simulación)**.
2. Filtrar el tráfico que se muestra actualmente sólo a las PDU **HTTP** y **TCP**. Para filtrar el
tráfico que se muestra actualmente:<br>- Haz clic en **Edit Filters** y alterna el botón **Show All/None**.<br>- Selecciona **HTTP** y **TCP**. Haz clic en la «x» roja en la esquina superior derecha del cuadro Editar filtros para cerrarla. Los eventos visibles ahora deberían mostrar solo las PDU **HTTP** y **TCP**.
3. Abre el navegador en HTTP Client e ingresa **192.168.1.254** en el campo URL. Haz clic en **Ir** para conectarse al servidor a través de HTTP. Minimiza HTTP Client window.
4. Haz clic en **Capturar/Reenviar** hasta que aparezca una PDU para HTTP. Tenga en cuenta que el color del envolvente de la ventana de topología coincide con el código de color de la PDU HTTP del Panel de simulación.


#### ¿Por qué tardó tanto en aparecer la PDU HTTP?
Porque primero se debe establecer una conexión TCP entre el multiserver y el cliente, para que así el trafico HTTP pueda comenzar.

5. Haz clic en el sobre de la PDU para mostrar los detalles de la PDU. Haz clic en **Outbound PDU Details** y desplácese hacia abajo hasta la segunda sección.
#### ¿Cómo se rotula la sección?
TCP
#### ¿Se consideran confiables estas comunicaciones?
SI
