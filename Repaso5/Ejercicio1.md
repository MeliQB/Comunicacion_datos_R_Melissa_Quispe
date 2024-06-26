## Simulación de escalabilidad vertical y horizontal

**Escalabilidad Horizontal:**  se refiere a agregar más recursos (como instancias de EC2 o bases de datos) para distribuir la carga de trabajo. Esto permite aumentar la capacidad de manera casi ilimitada, agregando más unidades de cómputo o almacenamiento según sea necesario.

En AWS, la escalabilidad horizontal se puede lograr mediante el uso de servicios como Auto Scaling Groups, Amazon Elastic Kubernetes Service (EKS). Estos servicios permiten agregar o quitar recursos de manera automatizada en función de la demanda.

La escalabilidad horizontal tiene la ventaja de ser más escalable a largo plazo, pero puede requerir una mayor complejidad en la arquitectura de la aplicación para manejar la distribución de carga de trabajo.


**Escalabillidad Vertical:**  se refiere a aumentar la capacidad de un recurso individual aumentando sus recursos internos, como la CPU, la memoria RAM o el almacenamiento. En AWS, esto se puede lograr, por ejemplo, cambiando a una instancia de EC2 de mayor tamaño o actualizando el plan de servicio de una base de datos RDS.

La escalabilidad vertical tiene la ventaja de ser relativamente simple de implementar y no requiere cambios en la arquitectura de la aplicación. Sin embargo, tiene un límite en la capacidad máxima que puede alcanzar un único recurso.

*Diferencias:*


1. Enfoque:
   - Vertical: Aumentar la capacidad de un único recurso (por ejemplo, una        instancia de EC2 o una base de datos RDS).
   - Horizontal: Agregar más recursos (por ejemplo, más instancias de EC2 o       bases de datos RDS).

2. Límite de escalabilidad:
   - Vertical: Hay un límite en la capacidad máxima que puede alcanzar un         único recurso.
   - Horizontal: Prácticamente ilimitada, ya que se puede agregar más             recursos según sea necesario.

3. Complejidad:
   - Vertical: Relativamente simple de implementar, no requiere cambios           significativos en la arquitectura.
   - Horizontal: Puede requerir una mayor complejidad en la arquitectura de       la aplicación para manejar la distribución de carga de trabajo.

4. Disponibilidad:
   - Vertical: Al escalar verticalmente, hay un riesgo de que el recurso          individual se convierta en un punto único de fallo.
   - Horizontal: Al escalar horizontalmente, se distribuye la carga de            trabajo entre múltiples recursos, lo que mejora la disponibilidad y la       tolerancia a fallos.

5. Flexibilidad:
   - Vertical: Menos flexible, ya que las opciones de escalado vertical           están limitadas por el hardware o plan de servicio del recurso.
   - Horizontal: Más flexible, ya que se pueden agregar o eliminar recursos       según sea necesario.


La escalabilidad vertical es más sencilla de implementar, pero tiene un límite en la capacidad máxima. La escalabilidad horizontal es más compleja, pero ofrece una escalabilidad prácticamente ilimitada y una mayor disponibilidad y flexibilidad.



