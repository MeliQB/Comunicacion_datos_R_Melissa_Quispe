# Uso de CLoudFront como CDN para un sitio web 

#### Crear un bucket de S3  mediante WS CLI

Creamos un bucket S3 mediante una herramienta de comando libre (AWS CLI).
<p aling = "center">
  <img src = "https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/b851e0507fd46e7f7ca56e6fad25e40008eb8aab/Im%C3%A1genes/Captura%20desde%202024-05-29%2008-37-35.png">
</p>

#### Añadir una política de bucket

Desactivamos la casilla de bloquear acceso público, ya que, estaba activado predeterminadamente.

<p aling = "center">
  <img src = "https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/b851e0507fd46e7f7ca56e6fad25e40008eb8aab/Im%C3%A1genes/Captura%20desde%202024-05-29%2008-40-11.png">
</p>

Después, editamos la sección de Política del bucket para conceder acceso de lectura pública al sitio web creado.

<p aling = "center">
  <img src = "https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/b851e0507fd46e7f7ca56e6fad25e40008eb8aab/Im%C3%A1genes/Captura%20desde%202024-05-29%2008-43-36.png">
</p>

#### Subir un documento HTML

Cargamos un archivo index.html en el bucket.

<p aling = "center">
  <img src = "https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/b851e0507fd46e7f7ca56e6fad25e40008eb8aab/Im%C3%A1genes/Captura%20desde%202024-05-29%2008-48-12.png">
</p>

#### Probar el sitio web

Podemos visualizar el contenido del documento subido anteriormente index.html

<p aling = "center">
  <img src = "https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/b851e0507fd46e7f7ca56e6fad25e40008eb8aab/Im%C3%A1genes/hw.jpeg">
</p>

#### Crear una distribución de CloudFront para servir al sitio web

Creamos uan distribución de Amazon CloudFront para servir al sitio web
Luego creamos un nuevo archivo HTML para probar la distribución subiendo una imagen al bucket.
<p aling = "center">
  <img src = "https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/b851e0507fd46e7f7ca56e6fad25e40008eb8aab/Im%C3%A1genes/Captura%20desde%202024-05-29%2009-30-23.png">
</p>

Se muestra la imagen que se subió al bucket

<p aling = "center">
  <img src = "https://github.com/MeliQB/Comunicacion_datos_R_Melissa_Quispe/blob/b851e0507fd46e7f7ca56e6fad25e40008eb8aab/Im%C3%A1genes/Captura%20desde%202024-05-29%2009-30-52.png">
</p>



