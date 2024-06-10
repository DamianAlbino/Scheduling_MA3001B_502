# Scheduling Project

### Damián Jacob Albino Mejía A01246716

## Descripción del proyecto

El proyecto actual busca establecer una metodología para crear una solución a un programa de producción o scheduling, que consta en la asignación y secuenciación de tareas o trabajos que unos recursos, limitados, tienen que realizar, estableciendo el tiempo en el que inician y terminan las tareas. Específicamente se buscará trabajar en la industria de alimentos y construir una solución para el proceso de producción del pan de molde.

Para iniciar con la producción del pan se necesita de ingredientes, los cuales son harina, azúcar, levadura, sal, manteca, conservadores y otros (depende del tipo de pan, por ejemplo semillas o frutos secos), los ingredientes que se requieren en menor cantidad se añaden a mano. Al contar con los ingredientes estos se insertan a una máquina que los mezcla hasta obtener la masa. 

La masa resultante se pasa a una línea donde esta se divide en bolas de masa de tamaños iguales, en esta misma línea las bolas de masa se cubren de harina, se moldean y se enrollan. Después de enrollarse la masa pasa a unos moldes donde se deja fermentar por unas horas.

Finalmente, tras haberse elevado la masa tras la fermentación esta se coce en los hornos, al terminar de hornearse las barras del pan resultantes se sacan de los moldes y se dejan enfriar por un tiempo antes de cortarlas y empaquetarlas.

### Archivos y directorios

- **src/main.py**: Archivo principal que ejecuta el proyecto.
- **src/Classes**: Contiene los archivos con las clases principales del proyecto.
  - `src/Classes/Demanda.py`: Clase que gestiona la demanda de producción.
  - `src/Classes/Maquina.py`: Clase que representa las máquinas en el proceso de producción.
  - `src/Classes/SecuenciaProduccion.py`: Clase que maneja la secuencia de producción.
  - `src/Classes/Setup.py`: Clase para los setups necesarios en el proceso.
- **src/Methods**: Contiene los archivos con los métodos de programación.
  - `src/Methods/desprogramar_manual.py`: Método para desprogramar manualmente tareas.
  - `src/Methods/programacion_automatica.py`: Método para la programación automática de tareas.
  - `src/Methods/programar_manual.py`: Método para programar manualmente tareas.

 ### Tablas de entrada

 #### Lista de Máquinas

| Campo              | Tipo     | Descripción                                    |
|--------------------|----------|------------------------------------------------|
| ID_Máquina         | Entero   | Identificador único para cada máquina.         |
| Tipo_Máquina       | Texto    | Tipo o categoría de la máquina.                |
| Capacidad          | Entero   | Capacidad de producción máxima por ciclo.      |
| Capacidad_Ocupada  | Entero   | Capacidad de producción asignada a la máquina. |
| Disponibilidad     | Texto    | Estado actual de la máquina.                   |
| Rate               | Decimal  | Tasa de producción específica de la máquina.   |

#### Lista de Demanda

| Campo           | Tipo         | Descripción                                  |
|-----------------|--------------|----------------------------------------------|
| ID_Demanda      | Entero       | Identificador único para cada demanda.       |
| Producto        | Texto        | Tipo de producto requerido.                  |
| Cantidad        | Decimal      | Cantidad requerida del producto.             |
| Fecha_Solicitud | Fecha y Hora | Fecha y hora de solicitud de producción.     |
| Estado          | Texto        | Estado de la demanda.                        |

#### Lista de Setups

| Campo       | Tipo   | Descripción                                   |
|-------------|--------|-----------------------------------------------|
| ID_Setup    | Entero | Identificador único para cada configuración.  |
| Descripción | Texto  | Breve descripción del setup.                  |
| Tiempo      | Horas  | Duración estimada del setup.                  |


### Tabla de salida

#### Tabla de Secuencia de Producción

| Campo             | Tipo         | Descripción                                   |
|-------------------|--------------|-----------------------------------------------|
| Producto          | Texto        | Tipo de producto.                             |
| ID_Máquina        | Entero       | Máquina utilizada.                            |
| FechaHoraInicio   | Fecha y Hora | Fecha y hora de inicio de producción.         |
| FechaHoraFin      | Fecha y Hora | Fecha y hora de finalización de producción.   |
| CantidadProgramada| Decimal      | Cantidad de producto programada.              |
| UnidadVentas      | Texto        | Unidades en las que se mide el volumen de ventas.|


## Instalación

1. Clona este repositorio en tu máquina local.
2. Navega al directorio del proyecto.
3. Instala las dependencias necesarias usando el siguiente comando:
   ```bash
   pip install -r requirements.txt
## Uso
Ejecuta el archivo principal para iniciar el programa:
`python src/main.py`
