# Investigación de los modelos TCP/IP y OSI

</p>

## Paso 1: Examinar el tráfico web HTTP
### Cambia del modo de tiempo real al modo de simulación.
1. Haz clic en el ícono del modo de Simulación para cambiar del modo de Tiempo real al modo de Simulación.
2. Selecciona HTTP en Filtros de lista de eventos.
2.1. Es posible que HTTP ya sea el único evento visible. Si es necesario, haz clic en el botón Editar filtros en la parte inferior del panel de simulación para mostrar los eventos visibles disponibles. Alterna la casilla de verificación Mostrar todo/ninguno y observa cómo las casillas de verificación se desactivan y se activan, o viceversa, según el estado actual.
2.2. Haz clic en la casilla de verificación Mostrar todo/ninguno hasta que se desactiven todas las casillas y luego selecciona HTTP. Haz clic en la X situada en la esquina superior derecha de la ventana para cerrar la ventana Editar filtros. Los eventos visibles ahora deben mostrar sólo HTTP.
   <p aling = "center">
     <img src = "https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/3eb22f5a9db2c3fc6707745f8e6c78bcd99997e0/Im%C3%A1genes/imagen_2024-05-20_233615609.png" width="600">
     </p>
</p>


### Genera tráfico web (HTTP).

<p align="justify">
Actualmente, el panel de simulación está vacío. En la parte superior de Lista de eventos dentro del panel de simulación, se indican cinco columnas. A medida que se genera y se revisa el tráfico, aparecen los eventos en la lista.

a. Haz clic en Cliente web en el panel del extremo izquierdo.

b. Haz clic en la ficha Escritorio y luego en el ícono Navegador web para abrirlo.

c. En el campo de dirección URL, introduce www.osi.local y haga clic en Ir.

Debido a que el tiempo en el modo de simulación se desencadena por eventos, debes usar el botón Capturar/avanzar para mostrar los eventos de red. El botón de captura hacia adelante se encuentra en el lado izquierdo de la banda azul que está debajo de la ventana de topología. De los tres botones, es el de la derecha.

d. Haz clic en Capturar/Avanzar cuatro veces. Deberías haber cuatro eventos en la Lista de eventos.

**Observa la página del navegador web del cliente web. ¿Cambió algo?**

<p aling="center">
   <img src = "https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/6ddb1fd2c7fe24486ef83ab6974b22cb25a6c593/Im%C3%A1genes/imagen_2024-05-20_234207557.png" whidth=600>
</p>

### Explora el contenido del paquete HTTP

<p align="justify">
a. Haz clic en el primer cuadro coloreado debajo de la columna Lista de eventos > Información. Quizá sea necesario expandir el panel de simulación o usar la barra de desplazamiento que se encuentra directamente debajo de la lista de eventos.

Se muestra la ventana Información de PDU en dispositivo: cliente web. En esta ventana, solo hay dos fichas, (Modelo OSI y Detalles de PDU saliente), debido a que este es el inicio de la transmisión. A medida que se analizan más eventos, se muestran tres fichas, ya que se agrega la ficha Detalles de PDU entrante. Cuando un evento es el último evento de la transmisión de tráfico, solo se muestran las fichas Modelo OSI y Detalles de PDU entrante.

b. Asegúrate de que esté seleccionada la ficha Modelo OSI.
En la columna Capas de salida , haga clic en Capa 7 .

</p>

- **¿Qué información se indica en los pasos numerados directamente debajo de los cuadros Capas de entrada y Capas de salida?** <br>"El cliente HTTP envía una solicitud HTTP al servidor."

- **¿Cuál es el valor del puerto Dst para la capa 4 en la columna Capas de salida?** <br>Dst Port: 80

- **¿Cuál es el destino? ¿Valor IP para la Capa 3 en la columna Capas de salida?** <br> En la Capa 3 el destino es 192.168.1.254

- **¿Qué información se muestra en la Capa 2 en la columna Capas de salida?** <br> Nos muestra el encabezado Ethernet II de capa 2, la **MAC de origen: 0060.47CA.4DEE** y la **MAC de destino: 0001.96A9.401D**.

c. Haz clic en la ficha de Detalles de la PDU saliente.
La información que se indica debajo de Detalles de PDU refleja las capas dentro del modelo
TCP/IP.
</p>
<p align="justify">
  
**Nota:** La información que se indica en la sección Ethernet II proporciona información aún más detallada que la que se indica en capa 2 en la ficha Modelo OSI. Los detalles de la PDU saliente proporcionan información más descriptiva y detallada. Los valores de MAC DE DEST. y de MAC DE ORIGEN en la sección Ethernet II de Detalles de PDU aparecen en la ficha Modelo OSI, en capa 2, pero no se los identifica como tales.

- **¿Cuál es la información frecuente que se indica en la sección IP de detalles de PDU comparada con la información que se indica en la ficha Modelo OSI? ¿Con qué capa se relaciona?**

- **¿Cuál es la información frecuente que se indica en la sección IP de Detalles de PDU comparada con la información que se indica en la ficha Modelo OSI?**

- **¿Cuál es el host que se indica en la sección HTTP de Detalles de PDU? ¿Con qué capa se relacionaría esta información en la ficha Modelo OSI?**

d. Haz clic en el primer cuadro coloreado debajo de la columna Lista de eventos >Tipo. Solo la capa 1 está activa (sin atenuar). El dispositivo mueve el frame desde el búfer y la coloca en la red.

e. Avanza al siguiente cuadro Tipo de HTTP dentro de la lista de eventos y haz clic en el
cuadro coloreado. Esta ventana contiene las columnas Capas de entrada y Capas de
salida. Observa la dirección de la flecha que está directamente debajo de la columna Capas
de entrada; esta apunta hacia arriba, lo que indica la dirección en la que se transfiere la
información. Desplázate por estas capas y toma nota de los elementos vistos anteriormente.
En la parte superior de la columna, la flecha apunta hacia la derecha. Esto indica que el
servidor ahora envía la información de regreso al cliente. Compara la información que se
muestra en la columna Capas de entrada con la de la columna Capas de salida: ¿cuáles
son las diferencias principales?

f. Haz clic en la ficha Inbound PDU Details (Detalles de PDU entrante). Revisa los detalles de
la PDU.

g. Haz clic en el último cuadro coloreado de la columna Información.Explica los resultados.
</p>
## Paso 2: Mostrar elementos de la suite de protocolos TCP/IP
### Ver eventos adicionales

<p align="justify">
a. Cierra todas las ventanas de información de PDU abiertas.

b. En la sección Filtros de lista de eventos > Eventos visibles, haga clic en Mostrar todo.

- **¿Qué tipos de eventos adicionales se muestran?**

Estas entradas adicionales cumplen diversas funciones dentro de la suite TCP/IP. El Protocolo de resolución de direcciones (ARP) solicita direcciones MAC para los hosts de destino. El protocolo DNS es responsable de convertir un nombre (por ejemplo, www.osi.local) a una dirección IP. Los eventos de TCP adicionales son responsables de la conexión, del acuerdo de los parámetros de comunicación y de la desconexión de las sesiones de comunicación entre los dispositivos.

c. Haz clic en el primer evento de DNS en la columna Información. Examina las fichas Modelo OSI y Detalles de PDU, y observa el proceso de encapsulamiento. Al observar la ficha Modelo OSI con el cuadro capa 7 resaltado, se incluye una descripción de lo que ocurre, inmediatamente debajo de las Capas de entrada y las Capas de salida: (“1. The DNS client sends a DNS query to the DNS server.” [“El cliente DNS envía una consulta DNS al servidor DNS”]). Esta información es muy útil para ayudarte a comprender qué ocurre durante el proceso de comunicación.

d. Haz clic en la ficha de Detalles de la PDU saliente.

- **¿Qué información se indica en NOMBRE: en la sección CONSULTA DNS?**

e. Haz clic en el último cuadro coloreado Información de DNS en la lista de eventos.

- **¿En qué dispositivo se capturó la PDU?**
  
- **¿Cuál es el valor que se indica junto a DIRECCIÓN: en la sección RESPUESTA DE DNS de Detalles de la PDU entrante?**

f. Busca el primer evento de HTTP en la lista y haga clic en el cuadro coloreado del evento de
TCP que le sigue inmediatamente a este evento. Resalte capa 4 en la ficha Modelo OSI.

- En la lista numerada que está directamente debajo de Capas de entrada y Capas de salida, **¿cuál es la información que se muestra en los elementos 4 y 5?**. El protocolo TCP administra la conexión y la desconexión del canal de comunicaciones, además de tener otras responsabilidades. Este evento específico muestra que SE ESTABLECIÓ el canal de comunicaciones.

g. Haz clic en el último evento de TCP. Resalte capa 4 en la ficha Modelo OSI. Examine los
pasos que se indican directamente a continuación de Capas de entrada y Capas de salida.

- **¿Cuál es el propósito de este evento, según la información proporcionada en el último
elemento de la lista (debe ser el elemento 4)?**
</p>
