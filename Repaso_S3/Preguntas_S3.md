# S3

### INTRODUCCIÓN A LAS OPCIONES DE ALMACENAMIENTO EN AWS

**Pregunta:** *Explica las diferentes opciones de almacenamiento disponibles en AWS y sus casos de uso  más comunes. ¿Cuáles son las diferencias clave entre el almacenamiento en bloque,  almacenamiento de archivos y almacenamiento de objetos?*


Almacenamiento en bloque (EBS): Acceso a nivel de bloque, orientado a cargas de trabajo con un alto rendimiento y baja latencia. Adecuado para bases de datos y aplicaciones empresariales.
Almacenamiento de archivos (EFS): Acceso a nivel de archivo, orientado a cargas de trabajo que requieren un sistema de archivos compartido y escalable. Adecuado para aplicaciones web y servicios empresariales.
Almacenamiento de objetos (S3): Acceso a nivel de objeto, orientado al almacenamiento y recuperación de datos no estructurados. Adecuado para una amplia gama de casos de uso, incluido el alojamiento de sitios web estáticos.


### ALMACENAMIENTO EN BLOQUE

**Pregunta:** *Describe el almacenamiento en bloque en AWS y sus ventajas. ¿Cómo se utiliza Amazon  EBS (Elastic Block Store) y cuáles son sus principales características?*

El almacenamiento en bloque con Amazon EBS proporciona un almacenamiento persistente, altamente disponible y ajustable para cargas de trabajo críticas que requieren un acceso rápido y eficiente a los datos.
EBS de utiliza para:
Creación de volúmenes
Adjuntar volúmenes a instancias de EC2
Gestión y monitoreo 
Principales características de Amazon EBS:
Rendimiento ajustable (IOPS, rendimiento y latencia)
Respaldo de datos mediante snapshots
Cifrado de volúmenes
Integración con otros servicios de AWS, como EC2, CloudWatch y AWS Backup

### ALMACENAMIENTO DE ARCHIVOS

**Pregunta:**  *Explica el almacenamiento de archivos en AWS. ¿Qué es Amazon EFS (Elastic File System)  y cómo se diferencia de Amazon FSx?*

Amazon EFS es un servicio de almacenamiento de archivos escalable y elástico en la nube, diseñado para satisfacer las necesidades de almacenamiento de archivos compartidos de las aplicaciones en la nube. Por otro lado, Amazon FSx se enfoca en proporcionar sistemas de archivos administrados de terceros para cargas de trabajo específicas.


### Almacenamiento de objetos 

**Pregunta:** *Define el almacenamiento de objetos y explica cómo Amazon S3 implementa este tipo de  almacenamiento. ¿Cuáles son las ventajas del almacenamiento de objetos sobre los otros tipos de  almacenamiento?*

El almacenamiento de objetos con Amazon S3 ofrece una solución de almacenamiento altamente escalable, durable y flexible, lo que lo convierte en una opción ideal para una amplia gama de casos de uso en comparación con otros tipos de almacenamiento.
Ventajas del almacenamiento de objetos con Amazon S3:
Escalabilidad ilimitada: S3 puede escalar fácilmente para manejar cualquier volumen de datos, sin necesidad de aprovisionar capacidad.
Durabilidad y disponibilidad: S3 ofrece una durabilidad y disponibilidad excepcionales, lo que lo convierte en una opción confiable para el almacenamiento a largo plazo.
Versatilidad: S3 se puede utilizar para una amplia gama de casos de uso, desde el almacenamiento de datos no estructurados hasta el alojamiento de sitios web estáticos.
Bajo costo: S3 ofrece una estructura de precios sencilla y competitiva, lo que lo hace una opción de almacenamiento rentable.
Facilidad de uso: S3 se puede administrar fácilmente a través de la consola de AWS, la CLI o APIs, lo que facilita su integración en aplicaciones y flujos de trabajo.
Introducción a Amazon S3 
Pregunta: Proporciona una visión general de Amazon S3, incluyendo su arquitectura y cómo se  organizan los datos en buckets y objetos.

**Arquitectura de Amazon S3:**

S3 es un servicio de almacenamiento de objetos en la nube ofrecido por Amazon Web Services (AWS).
Está diseñado para ofrecer una escala, durabilidad y disponibilidad casi ilimitadas para el almacenamiento de datos.
S3 está construido sobre una infraestructura altamente redundante y distribuida, lo que le permite ofrecer una durabilidad y una disponibilidad del 99,9%.


**Organización de datos en S3:**

- *Buckets (Contenedores):*
    	Los datos en S3 se organizan en "buckets", que son contenedores de nivel superior donde se almacenan los objetos.
    	Cada bucket tiene un nombre único a nivel global dentro de AWS.
    	Los buckets se pueden configurar con políticas de acceso, reglas de ciclo de vida, versioning, entre otras opciones.

- *Objetos:*
    	Dentro de cada bucket, los datos se almacenan como "objetos".
    	Un objeto consta de los datos en sí, los metadatos asociados y una clave única que identifica al objeto.
    	Los objetos pueden tener un tamaño de hasta 5 TB.
    	Cada objeto tiene una URL única que se puede utilizar para acceder a los datos.

- *Jerarquía de directorios:*
    	Aunque S3 no tiene un sistema de archivos tradicional, los objetos se pueden organizar de manera jerárquica utilizando "prefijos" (similares a directorios).
    	Esto permite una estructura de carpetas y subcarpetas lógica para organizar y acceder a los datos.
Buckets y Objetos 
Pregunta: Describe cómo crear y gestionar buckets y objetos en Amazon S3. ¿Cuáles son las mejores  prácticas para nombrar y organizar buckets y objetos? 
Mejores prácticas para nombrar y organizar buckets y objetos:
Nombrado de buckets:
Usar nombres de buckets que sean descriptivos, significativos y únicos.
Seguir las convenciones de nomenclatura de DNS para que los buckets puedan ser utilizados como parte de URLs.
Organización de objetivos:
Utilizar una estructura de directorios lógica y jerárquica para organizar tus objetos dentro de los buckets
Asignar claves
Usar prefijos
Habilitar el versionamiento de objetos para mantener un historial de cambios y facilitar la recuperación de versiones anteriores.


### Gestión de objetos en un Bucket 
**Pregunta:**  *Explica las diferentes maneras de gestionar objetos en un bucket de Amazon S3,  incluyendo la carga, descarga y eliminación de objetos. ¿Qué herramientas y métodos se pueden  utilizar para estas operaciones?*

Herramientas y métodos:
Consola de AWS:  La interfaz web de la consola de AWS proporciona una forma sencilla y visual de gestionar objetos en S3.
AWS CLI: La línea de comando de AWS (AWS CLI) permite realizar operaciones de gestión de objetos de manera eficiente y automatizada.
AWS SDK: como Python, js, Node, etc. permiten integrar la gestión de objetos en S3 de forma programática en tus aplicaciones.
API S3: P uedes interactuar directamente con la API de S3 a través de solicitudes HTTP para realizar operaciones avanzadas de gestión de objetos.
Amazon S3 ofrece múltiples métodos y herramientas para cargar, descargar, eliminar y gestionar objetos de manera eficiente, lo que te permite integrar estas funcionalidades en tus aplicaciones y flujos de trabajo.


### Alojamiento regional – disponibilidad Global 

**Pregunta:**  *Discute la importancia del alojamiento regional en Amazon S3 y cómo asegura la alta  disponibilidad y durabilidad de los datos.*

El alojamiento regional en Amazon S3 es fundamental para garantizar la alta disponibilidad y durabilidad de tus datos. Al aprovechar la redundancia entre Zonas de Disponibilidad dentro de una región, S3 ofrece un almacenamiento altamente confiable y resiliente, lo que lo convierte en una opción ideal para una amplia gama de cargas de trabajo en la nube.
