# LABORAPP
**DISEÑO Y DESARROLLO DE UNA APLICACIÓN WEB PARA LA VINCULACIÓN LABORAL**

<img src="https://user-images.githubusercontent.com/17323717/165867245-4334e621-dec9-4f0d-b74d-dfd6e9dc9443.png" width="400">

Juan Camilo Fandiño Orjuela \
Universidad EAN \
Facultad de Ingeniería \
Bases de Datos 

<<<<<<<<< [VISITA LA APP](http://137.184.153.34) >>>>>>>>>>

### INTRODUCCIÓN

El presente trabajo tiene como objetivo abordar el diseño y desarrollo de una aplicación web para la búsqueda de empleo la cual está centrada en los aspirantes en lugar de las organizaciones. Este aplicativo web será implementado en Python, mediante el framework de desarrollo web &quot;Flask&quot; y contará con MySQL como RDBMS. Así mismo, se trabajarán los conceptos adquiridos durante el desarrollo de la unidad de estudio &quot;Bases de Datos&quot;, por lo que se incluirán las entidades creadas, tablas, restricciones, llaves primarias y llaves foráneas.

Por otro lado, el DDL y DML utilizado para el desarrollo de la solución será incorporado igualmente, no obstante, es importante resaltar que para realizar la comunicación entre la base de datos y la aplicación se hará uso de un ORM (Mapeo objeto-relacional) el cual permite interactuar de manera más sencilla con las entidades de la base de datos al vincularlas con objetos dentro del lenguaje de programación.

Finalmente, también se incluirá el diseño de la interfaz y las demás herramientas utilizadas para la elaboración de la solución.

### NECESIDAD/JUSTIFICACIÓN

Conseguir empleo tanto a nivel nacional como internacional se ha convertido en una problemática para muchos profesionales en la actualidad, lograr que los egresados sean tenidos en cuenta por las grandes empresas no es tarea fácil, pues para lograr si quiera ser considerado por alguna organización muchas veces es necesario enviar múltiples hojas de vida a diferentes personas y compañías. Una encuesta realizada recientemente por la firma Adecco Colombia, especialista en talento humano, reveló que para gran parte de las personas que adelantan una búsqueda activa de trabajo es muy difícil encontrar un empleo. De hecho, el 84% de los consultados considera que dar con un puesto de trabajo acorde con sus expectativas es algo particularmente complicado.

Ahora bien, aunque en el mercado actualmente existen distintos instrumentos tecnológicos y no-tecnológicos que buscan facilitar ese proceso, ninguno se ha consolidado como una solución definitiva para esta problemática, esto debido a que en la mayoría de los casos los diseñadores de las plataformas y servicios para la búsqueda de empleo se han centrado en favorecer a las empresas en lugar de los aspirantes y candidatos. Por otro lado, también es importante mencionar que en muchas de estas soluciones el usuario no tiene si quiera la posibilidad de ingresar a que puesto está aspirando, sino que son los reclutadores los que se encargan de realizar dicho filtro.

Teniendo en cuenta lo anteriormente expuesto surge la necesidad de implementar una herramienta que permita que aspirantes de diversas profesiones sean capaces de buscar empleo de manera sencilla y que con tan solo ingresar su información básica, estudios académicos y experiencial laboral puedan ser tenidos en cuenta por múltiples empleadores al mismo tiempo. Así mismo, esta herramienta permitirá que el personal de recursos humanos pueda revisar múltiples candidatos de manera sencilla y que sea capaz obtener los datos para contactarse con cualquiera de ellos de ser necesario.

### REQUISITOS FUNCIONALES

| Número de requerimiento | RF001 |
| --- | --- |
| Nombre de requerimiento | Autenticación de usuarios |
| Tipo | Requisito                                  |
| Fuente del requerimiento | Usuario |
| Proceso | La aplicación permite validar las credenciales del usuario a través de una pantalla de inicio de sesión. |
| Prioridad del requerimiento | Esencial |

| Número de requerimiento | RF002 |
| --- | --- |
| Nombre de requerimiento | CRUD Usuarios |
| Tipo | Requisito                                  |
| Fuente del requerimiento | Administrador |
| Proceso | La aplicación permite crear, consultar, editar y eliminar usuarios.|
| Prioridad del requerimiento | Esencial |

| Número de requerimiento | RF003 |
| --- | --- |
| Nombre de requerimiento | Ingreso de información académica.                              |
| Tipo | Requisito      |
| Fuente del requerimiento | Usuario |
| Proceso | La aplicación permite a los usuarios (aspirantes) ingresar su formación académica (Nombre de la institución académica, titulo obtenido, fecha)|
| Prioridad del requerimiento | Esencial |

| Número de requerimiento | RF004 |
| --- | --- |
| Nombre de requerimiento | Ingreso de experiencia laboral.                              |
| Tipo | Requisito                                  |
| Fuente del requerimiento | Usuario |
| Proceso | La aplicación permite a los usuarios (aspirantes) ingresar su experiencia laboral (Empresa, Descripción del cargo, Duración) |
| Prioridad del requerimiento | Esencial |

| Número de requerimiento | RF005 |
| --- | --- |
| Nombre de requerimiento | Ingreso de lenguajes                              |
| Tipo | Requisito                                  |
| Fuente del requerimiento | Usuario |
| Proceso | La aplicación permite a los usuarios (aspirantes) ingresar los idiomas que dominan (Nombre del lenguaje, calificación internacional) |
| Prioridad del requerimiento | Esencial |

| Número de requerimiento | RF006 |
| --- | --- |
| Nombre de requerimiento | Consulta de Aspirantes |
| Tipo | Requisito                                  |
| Fuente del requerimiento | Usuario |
| Proceso | La aplicación permite a los usuarios (empresas) consultar a los posibles aspirantes, con su información correspondiente.|
| Prioridad del requerimiento | Esencial |

| Número de requerimiento | RF007 |
| --- | --- |
| Nombre de requerimiento | Prohibir duplicados |
| Tipo | Restricción                                  |
| Fuente del requerimiento | Administrador |
| Proceso | La aplicación impide la creación de usuarios con el mismo con el mismo correo |
| Prioridad del requerimiento | Esencial |
| Número de requerimiento | RF008 |
| Nombre de requerimiento | Garantizar Integridad |
| Tipo | Restricción                                  |
| Fuente del requerimiento | Administrador |
| Proceso | La aplicación impide la modificación de la información de los aspirantes por parte de terceros sin autorización. |
| Prioridad del requerimiento | Esencial |

### REQUISITOS NO FUNCIONALES

| Número de requerimiento | RNF001 |
| --- | --- |
| Nombre de requerimiento | Encripción de claves |
| Tipo | Requisito                                  |
| Fuente del requerimiento | Administrador |
| Proceso | La contraseña se almacena cifrada en la base de datos, esto con el fin de que ninguna persona a parte del usuario la conozca. |
| Prioridad del requerimiento | Esencial |

| Número de requerimiento | RNF002 |
| --- | --- |
| Nombre de requerimiento | UI/UX |
| Tipo | Requisito                       |
| Fuente del requerimiento | Administrador |
| Proceso | La aplicación cuenta con una interfaz de usuario intuitiva y fácil de usar. |
| Prioridad del requerimiento | Deseada |

| Número de requerimiento | RNF003 |
| --- | --- |
| Nombre de requerimiento | Almacenamiento de información |
| Tipo | Requisito                                  |
| Fuente del requerimiento | Administrador |
| Proceso | Los datos de la aplicación serán administrados mediante un sistema de gestión de bases de datos relacionales. |
| Prioridad del requerimiento | Esencial |

| Número de requerimiento | RNF004 |
| --- | --- |
| Nombre de requerimiento | Alojamiento de la aplicación |
| Tipo | Requisito                                  |
| Fuente del requerimiento | Administrador |
| Proceso | La aplicación esta alojada en un servicio de hosting online, estando disponible para los usuarios a través de la web. |
| Prioridad del requerimiento | Esencial |

### HERRAMIENTAS UTILIZADAS

  1. **Python**

Python es un lenguaje de programación de alto nivel y su filosofía de diseño central tiene que ver con la legibilidad del código y una sintaxis que permite a los programadores expresar conceptos en unas pocas líneas de código.

Python es un lenguaje interpretado y a diferencia de los lenguajes compilados en los que el código debe traducirse a lenguaje de máquina para que el procesador lo ejecute, el código de Python se pasa directamente a un intérprete y se ejecuta directamente.

 <img src="https://user-images.githubusercontent.com/17323717/165866320-cf21e8dd-8f1a-4c8b-99ac-4f2677fe68b5.png" width="300">
 
  2. **Flask**

Flask es un pequeño y ligero framework de desarrollo web para Python que proporciona herramientas y funciones útiles que permiten que crear aplicaciones web en Python sea más fácil. Ofrece a los desarrolladores flexibilidad y una curva de aprendizaje corta permitiendo crear una aplicación web usando únicamente un archivo Python. Flask también es extensible y no fuerza una estructura de directorio concreta.

 <img src="https://user-images.githubusercontent.com/17323717/165866326-bc09c4f3-f2a2-4860-a50a-0f05c3a5e768.png" width="300">
 
  3. **Jinja2**

Flask utiliza el motor de plantillas Jinja2 para crear dinámicamente páginas HTML usando conceptos Python familiares como variables, bucles, listas, etcétera.

![índice](https://user-images.githubusercontent.com/17323717/165866340-2a9d05ec-fa0f-4e8d-8b51-8f4c480203e0.png)


  4. **MySQL**

MySQL es un sistema de gestión de bases de datos relacionaleS (RDBMS) de código abierto basado en el lenguaje de consulta estructurado (SQL). Aunque se puede utilizar para muchos propósitos, el desarrollo web es el ámbito en donde más se utiliza.

 <img src="https://user-images.githubusercontent.com/17323717/165866348-6cc14729-781b-438b-956d-9f7736034b6e.png" width="300">

  5. **SQLAlchemy**

SQLAlchemy es un Object-Relational Mapper (Mapeador objeto-relacional), es decir que es una librería que permite simplificar el uso de las bases de datos, esto la vinculación de entidades con objetos, lo que evita tener que escribir múltiples veces las mismas consultas de SQL.

También es importante mencionar que otros lenguajes también tienen sus propios ORMs como Eloquent en PHP o Hibernate en Java.

### ARQUITECTURA DE SOFTWARE

La arquitectura utilizada para el presente trabajo será el &quot;Modelo–vista–controlador&quot; (MVC) ya que se separaran los datos, la lógica y la interfaz de usuario. A continuación, se presenta de manera más detallada el contenido/concepto de cada capa:

- Modelos/Entidades: Son la representación de la información registrada en la aplicación web, gestiona los accesos a dicha información y la definición de los tipos de datos. En la presente aplicación algunas de los modelos definidos serán: Usuario, Empleador, Candidato, Experiencia Laboral y Experiencia Académica.
- Controladores: Responden a eventos provocados por el usuario e invoca peticiones al &#39;modelo&#39; cuando se hace alguna solicitud sobre la información (por ejemplo, editar un documento o un registro en una base de datos). También envía comandos a la &#39;vista&#39; asociada.
- Vistas: Presenta la información en un formato adecuado para el usuario (interfaz de usuario).

### MODELO ENTIDAD-RELACIÓN

A continuación, se muestra el modelo entidad-relación planteado:

**Figura 1**

Modelo entidad-relación


![Imagen 1](https://user-images.githubusercontent.com/17323717/165865971-b21570ec-16f6-4ecc-92e0-5f89443c92ba.png)


_Nota:_ El diagrama fue generado mediante la herramienta provista por DataGrip, las llaves primarias están indicadas de color dorado, mientras que las llaves foráneas están denotadas en color azul.

### METODOLOGÍA

La metodología ágil que será utilizada en el presente proyecto será **Kanban.** Esta es una metodología de desarrollo de software incremental a diferencia de otras iterativas como Scrum. Kanban pretende que el software sea creado en un gran ciclo, no obstante, buscar dividir el desarrollo en diferentes tareas para posteriormente elaborar un cuadro o diagrama en el que se reflejará su estado, las columnas normalmente son: tareas pendientes, en proceso y terminadas. Para el desarrollo del presente proyecto Trello será la herramienta en donde se consignará el tablero.

La elección de esta metodología se hizo teniendo en cuenta la fecha de entrega del proyecto, el tamaño del equipo (en este caso unipersonal), y las ventajas que presenta frente a una ejecución relativamente pequeña.

### UI


![Captura de Pantalla 2022-04-28 a la(s) 7 42 28 p  m](https://user-images.githubusercontent.com/17323717/165871915-d6342b39-fe94-4f34-b24a-cd006462cd34.png)


![Captura de Pantalla 2022-04-28 a la(s) 8 07 15 p  m](https://user-images.githubusercontent.com/17323717/165871919-97505a7f-3832-4536-92a3-5e933c5d2e30.png)

![Captura de Pantalla 2022-04-28 a la(s) 8 19 23 p  m](https://user-images.githubusercontent.com/17323717/165871922-dc526499-e1b7-451f-ad35-e558ba133ddc.png)

### RESULTADOS
Se logró el desarrollo de la aplicación web para la búsqueda de empleo cumpliendo los requerimientos funcionales y no funcionales propuestos. Posteriormente esta aplicación se alojó en DigitalOcean, el cual es un servicio de hosting online, lo que permitió su disponibilidad a través de internet. A continuación, se encuentran las distintas secciones de la aplicación que reflejan algunos de los requerimientos:

**Figura 4**
Validación de credenciales - RF001
![imagen](https://user-images.githubusercontent.com/17323717/171063073-08869223-2e04-4048-8ecc-150fcecba2da.png)
 
**Figura 5**
Consulta de usuarios - RF002
![imagen](https://user-images.githubusercontent.com/17323717/171063082-7a60fefc-0121-4d92-b2c8-3cb7eadabe04.png)


**Figura 6**
Ingreso de experiencia académica - RF003
![imagen](https://user-images.githubusercontent.com/17323717/171063097-dcda0a69-11ea-4bc7-a185-349b48c19d22.png)


**Figura 7**
Ingreso de experiencia laboral (CRUD) - RF004               
![imagen](https://user-images.githubusercontent.com/17323717/171063111-0c6bc412-1071-4574-9924-089b38cd7409.png)


**Figura 8**
Ingreso de lenguajes - RF005

![imagen](https://user-images.githubusercontent.com/17323717/171063118-74226ebd-eeaa-48dc-8d35-98309cc496ce.png)
 
**Figura 9**
Almacenamiento de contraseña cifrada - RNF001
![imagen](https://user-images.githubusercontent.com/17323717/171063129-39abd7be-0c74-4e2a-8329-f10cddb863fc.png)

 
### CONCLUSIONES
El desarrollo de la aplicación web utilizando Flask (Python) y MySQL (RDBMS) permitió un prototipado veloz y una fácil implementación, esto según la necesidad identificada y los requerimientos funcionales detallados. De igual manera el MER propuesto inicialmente para la creación de la base de datos fue suficiente y adecuado para almacenar la información necesaria de los candidatos.

Por otro lado, la arquitectura utilizada (modelo-vista-controlador) mostro ser un paradigma óptimo para este tipo de desarrollo dado que se encontraron ventajas como: la separación de los datos de su representación visual, fácil manejo de errores y la capacidad de agregar múltiples representaciones de los datos.

De igual manera, la metodología de desarrollo de software utilizada (Kanban) comprobó ser de bastante utilidad para la ejecución de proyectos de envergadura pequeña-mediana y especialmente útil para la continuación del proyecto en equipos unipersonales.

Finalmente, es importante mencionar que el desarrollo del presente proyecto permitió aplicar el conocimiento adquirido durante el transcurso de la asignatura “Base de datos”, específicamente los conceptos relacionados a manejo de bases de datos relacionales y creación de modelos entidad-relación.
