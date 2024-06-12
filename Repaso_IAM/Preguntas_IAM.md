# IAM

### Introducción al Servicio AWS IAM 

**Pregunta:**  *Explica la funcionalidad principal del servicio AWS IAM y su importancia en la  administración de accesos en la nube de AWS.* 

IAM permite proteger el acceso a tu cuenta de aws, además es un servicio de autenticación y autorización, que te permite decidir, quién o  qué puede acceder a los servicios de aws de tu cuenta, y qué pueden hacer estas entidades en tu cuenta.
Permite a las organizaciones mantener un control centralizado y detallar sobre los accesos y permisos en la nube de AWS. Esto contribuye a mejorar la seguridad, la gestión de identidades y el cumplimiento normativo.


### La consola de AWS IAM 

**Pregunta:** *Describe las diferentes secciones de la consola de AWS IAM y cómo se utilizan para  gestionar identidades y permisos.*

se puede utilizar la consola de administración basada en la web, la interfaz de comandos(CLI)  o los SDK DE AWS
La consola de AWS IAM proporciona a los administradores una interfaz unificada para crear, gestionar y asignar identidades, roles y permisos a los recursos de AWS.
AWS IAM pertenece a la categoría Seguridad, Identidad y Cumplimiento (Security, Identity, &Compliance)


### Servicios de AWS IAM 

**Pregunta:** *Enumera y describe brevemente los servicios principales que ofrece AWS IAM y cómo se  integran con otros servicios de AWS.*

Usuarios de  IAM: Del usuario raiz, se puede crear un usuarios adicionales como usuario de IAM, representan a las personas físicas
Grupos  de IAM: conjunto de usuarios de IAM, asignar  un solo permiso
Roles de IAM : define qué acciones pueden realizar las entidades autorizadas en los recursos de la nube. Estos roles son útiles en diversas situaciones, como la delegación de acceso a recursos a través de aplicaciones, la federación de identidades para permitir a usuarios externos acceder a recursos dentro de tu cuenta de nube y la automatización de tareas administrativas.
Políticas de IAM: as políticas de IAM son objetos adjuntos a una identidad de IAM dada, como un usuario de IAM, grupos de usuarios de IAM o un rol de IAM. Estas políticas definen lo que la identidad puede o no puede hacer dentro de la cuenta de AWS y se escriben como documentos JSON.
Credenciales de seguridad: son información utilizada para autenticar y autorizar solicitudes de acceso a recursos en la nube. Estas credenciales son esenciales para permitir que usuarios, aplicaciones o servicios accedan de manera segura a los recursos dentro de un entorno en la nube como Amazon Web Services (AWS)
Diferencias clave entre usuarios IAM y Grupos IAM 
Pregunta: Compara y contrasta las diferencias clave entre usuarios IAM y grupos IAM, incluyendo  sus usos y mejores prácticas. 
Los usuarios IAM permiten un control granular de permisos, mientras que los grupos IAM facilitan la gestión y simplificación de la asignación de permisos. Una combinación adecuada de usuarios y grupos, siguiendo las mejores prácticas, es clave para mantener la seguridad y la gobernanza en la nube de AWS.


### Usuarios IAM 

**Pregunta:**  *Explica el proceso de creación y gestión de un usuario IAM, incluyendo la asignación de  permisos y políticas.*

**Creación del usuario:**
- Accede a la consola de AWS IAM.
- En la sección "Usuarios", haz clic en "Añadir usuario".
- Proporciona un nombre único para el usuario y selecciona el tipo de acceso (consola de AWS, programático o ambos).
- Opcionalmente, puedes agregar etiquetas para organizar y filtrar usuarios.
- Revisa y confirma la creación del usuario.


**Asignación de permisos:**
Una vez creado el usuario, puedes asignar permisos para acceder a los recursos de AWS.
Puedes hacerlo de dos formas: a. Asignando políticas de permisos directamente al usuario. b. Agregando el usuario a uno o más grupos IAM que tengan políticas de permisos asignadas.

- Gestión de políticas de permisos:
Las políticas de permisos definen las acciones que el usuario puede realizar en los recursos de AWS.
Puedes crear políticas personalizadas en formato JSON o utilizar las políticas administradas por AWS.
Asigna las políticas de permisos al usuario o al grupo al que pertenece.

- Gestión de credenciales:
Puedes generar y administrar las credenciales de acceso del usuario, como contraseñas y claves de acceso.
Establece una política de contraseñas seguras y rota las credenciales periódicamente.
Habilita la autenticación multifactor (MFA) para mejorar la seguridad.

- Monitoreo y registro:
Utiliza el servicio AWS CloudTrail para registrar y auditar las actividades del usuario.
Revisa regularmente los registros de actividad para detectar cualquier actividad sospechosa.

-Revisión y actualización:
Revisa periódicamente los permisos asignados a los usuarios y ajusta según sea necesario.
Elimina o desactiva usuarios que ya no necesiten acceder a la plataforma AWS.


### Grupos IAM 

**Pregunta:** *Describe cómo crear y gestionar grupos IAM, y cómo se pueden utilizar para simplificar la  administración de permisos.*


Creación de un grupo:

**Accede a la consola de AWS IAM.**

En la sección "Grupos", haz clic en "Crear grupo".
Asigna un nombre único al grupo y, opcionalmente, agrega etiquetas.
Asignación de políticas de permisos:
Una vez creado el grupo, debes asignarle las políticas de permisos que definirán las acciones   que los usuarios del grupo podrán realizar.
Puedes utilizar políticas administradas por AWS o crear políticas personalizadas.
Selecciona las políticas que deseas asignar al grupo y confirma la asignación.

**Adición de usuarios al grupo:**

Después de crear el grupo y asignarle las políticas de permisos, puedes agregar usuarios a este grupo.
En la sección "Usuarios", selecciona los usuarios que deseas agregar al grupo y haz clic en "Agregar a grupo".
Los usuarios heredarán automáticamente los permisos definidos en las políticas asignadas al grupo.

**Gestión de grupos:**

Puedes editar el nombre del grupo, agregar o eliminar políticas de permisos, y agregar o eliminar usuarios del grupo según sea necesario.
Los cambios realizados en el grupo se reflejarán de manera automática en los usuarios que pertenecen a él.

. La creación y gestión de grupos IAM, junto con la asignación de políticas de permisos a estos grupos, es una práctica fundamental para simplificar y escalar la administración de accesos y permisos en la nube de AWS.
Definición de permisos con políticas IAM 
Pregunta: Explica qué son las políticas IAM y cómo se utilizan para definir permisos. Proporciona un  ejemplo de una política simple. 
Las políticas IAM (Identity and Access Management) son documentos en formato JSON que definen de manera declarativa los permisos que se otorgan a usuarios, grupos y roles dentro de la plataforma de AWS.

<p aling = "center">
   <img src = "">
</p> 
