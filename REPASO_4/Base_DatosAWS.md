# Temas: BASE DE DATOS EN AWS

#### Preguntas:

*1: Bases de datos administradas vs. no Administrativas*

*2: Servicios de bases de datos para requisitos especilizados*

*3: Conceptos y modelos de bases de datos*

**Modelos de bases de datos:**
- Modelo relacional: Organiza los datos en tablas (relaciones) con columnas y filas. Cada fila contiene información sobre una instancia específica de la entidad (por ejemplo, un cliente). Ejemplo de base de datos AWS: Amazon RDS para MySQL.
- Modelo no relacionales: Los datos se almacenan utilizando diferentes modelos según el tipo de datos que se almacenen.

Al igual que las bases de datos relacionales, las bases de datos no relacionales requieren
que tengas al menos un campo de clave principal (atributo) y este es el único atributo requerido. Más allá
de esto, las tablas de tu base de datos no tienen ningún esquema. La clave principal se utiliza para
garantizar que cada registro de la base de datos sea único.

*4: Introducción a Amazon RDS*

**Amazon RDS (Relational Database Service)** es un servicio administrado que facilita la implementación y gestión de bases de datos relacionales.

*Beneficios:*

- Automatización: Amazon RDS se encarga de tareas como aprovisionamiento, copias de seguridad, parches y actualizaciones.
- Escalabilidad: Puedes ajustar la capacidad de la base de datos según la demanda.
- Alta disponibilidad: Ofrece opciones de replicación y failover.
- Seguridad: Proporciona medidas de seguridad integradas.
- Monitoreo y métricas: Acceso a métricas y registros para supervisar el rendimiento.
