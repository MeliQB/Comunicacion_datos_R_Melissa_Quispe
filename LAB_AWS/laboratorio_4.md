# SERVIDORES VIRTUALES

## 4.1: Lanzamiento de una instancia de EC2:

Se lanzó una instancia y la llamamos Web Server 3, al asignarle un nombre nos permite identificar rápidamete un recurso específico.

##### Tarea 1: comenzar a crear la intancia y asignarle un nombre
<p aling = "center" >
  <img src = "https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/f6d214362c17719c2369527b3b97fe2beaeac684/Im%C3%A1genes/Captura%20desde%202024-05-29%2005-57-24.png">
</p>

Para poder visualizar la instancia lanzada se habílitó la IP pública, además se actualizó el grupo de seguridad, porque no se podía acceder al servidor web, puesto que, el grupo de seguridad no permite el tráfico  entrante en el puerto 80,
que se utiliza para las solicitudes web HTTP. Por ello se cambiaron las reglas de entrada con:

TIPO: HTTP
FUENTE: Cualquier lugar IPv4

Actualizamos la dirección IP y la pagína nos muestra lo siguiente:
<p aling = "center" >
  <img src = "https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/1883e5e81bc00119b4e36140cb7555b99098e145/Im%C3%A1genes/Captura%20desde%202024-05-29%2005-56-36.png">
</p>

## 4.2: Creación de un bucket de S3

#### Crear un Bucket

<p aling = "center" >
  <img src = "https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/9b62c6ae85a7e7e4a80545256238137f64cb11c7/Im%C3%A1genes/namebucket.jpeg">
</p>

Se desactivó el bloqueo de todo acceso público, el bucket creado y los objetos se conviertn el público, porque queremos verificar si el sitio web funciona.

<p aling = "center" >
  <img src = "https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/9b62c6ae85a7e7e4a80545256238137f64cb11c7/Im%C3%A1genes/quitbloqueo.jpeg">
</p>

#### Añadir una política de bucket para que el contenido esté disponible públicamente

Concedemos el acceso de lectura pública la sitio web en la política del bucket.

<p aling = "center" >
  <img src = "https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/9b62c6ae85a7e7e4a80545256238137f64cb11c7/Im%C3%A1genes/politicabucketcode.jpeg">
</p>

####  Subir un documento HTML
Sesubión un documento HTML al nuevo bucket.

<p aling = "center" >
  <img src = "https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/9b62c6ae85a7e7e4a80545256238137f64cb11c7/Im%C3%A1genes/index.jpeg">
</p>

#### Probar el sitio web

Al abrir el URL del punto de enlace del sitio web del bucket nos muestra lo siguiente: 

<p aling = "center" >
  <img src = "https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/9b62c6ae85a7e7e4a80545256238137f64cb11c7/Im%C3%A1genes/hw.jpeg">
</p>
