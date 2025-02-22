# **Estructura del Repositorio**  
El repositorio está organizado en diferentes carpetas y archivos para mantener una estructura clara y modular:  

------------

📂 Puntored  
│── 📂 data  
│   └── clientes.csv    <- Dataset con la información de los clientes  
│  
│── 📂 src  
│   ├── analisis.py     <- Código para análisis estadístico del dataset  
│   ├── outliers.py     <- Código para detección y tratamiento de valores atípicos  
│   ├── plots.py        <- Código para generar visualizaciones y gráficos  
│  
│── main.ipynb          <- Notebook con el desarrollo completo del proyecto  
│── requirements.txt    <- Archivo con las dependencias necesarias  
│── consultas.sql       <- Archivo con las consultas en SQL  
│── README.md           <- Documentación del proyecto  

--------

# **Prueba práctica python y machine learning: Predicción de Default en Créditos Bancarios**

## **Descripción del Proyecto**  
Este proyecto tiene como objetivo desarrollar un modelo de **Machine Learning** para predecir si un cliente de un banco **incumplirá en el pago de su crédito (default)**, utilizando datos históricos de clientes.  

El dataset contiene información clave sobre los clientes, como su **edad, ingreso mensual y historial crediticio**, lo que permite construir un modelo que ayude a identificar clientes con mayor riesgo de incumplimiento.  

## **Estructura del Dataset** (`clientes.csv`)  
| **Columna**              | **Tipo de dato** | **Descripción** |
|-------------------------|----------------|----------------|
| `edad`                 | `int`          | Edad del cliente en años. |
| `ingreso_mensual`      | `float`        | Ingreso mensual del cliente. |
| `historial_crediticio` | `int (0-5)`    | Evaluación del historial crediticio (0 = peor, 5 = mejor). |
| `default`              | `int (0 o 1)`  | Indica si el cliente incumplió en el pago del crédito (1 = Sí, 0 = No). |

## **Desarrollo del Proyecto**  
El desarrollo completo del proyecto, desde la limpieza de los datos hasta la creación y evaluación del modelo de Machine Learning, se encuentra en el **notebook `main.ipynb`**.  

En este notebook se abordan los siguientes pasos:  
1. **Carga y exploración de los datos**.  
2. **Limpieza y preprocesamiento**, incluyendo el tratamiento de valores nulos y outliers.  
3. **Análisis exploratorio de datos (EDA)** con visualizaciones.  
4. **Ingeniería de características** para mejorar el modelo.  
5. **Entrenamiento de modelos de clasificación**.  
6. **Evaluación del desempeño del modelo utilizando métrica AUC-ROC**.  

## **Instalación**  
Para instalar las dependencias del proyecto, ejecuta el siguiente comando en la terminal:  

```bash
pip install -r requirements.txt
```

# **Prueba Práctica de SQL**

En esta sección, se incluyen las consultas SQL para obtener información relevante de un conjunto de datos simulado, con base en la estructura de las tablas `clientes` y `ventas`. Las consultas están diseñadas para demostrar la capacidad de extracción de información útil y de análisis sobre los datos de ventas y clientes.

## **Estructura de las Tablas de la Prueba**

### Tabla: `clientes`
| **Columna**   | **Tipo de dato** | **Descripción** |
|---------------|------------------|-----------------|
| `id`          | `INT`            | Identificador único del cliente. |
| `nombre`      | `VARCHAR`        | Nombre del cliente. |
| `apellido`    | `VARCHAR`        | Apellido del cliente. |

### Tabla: `ventas`
| **Columna**   | **Tipo de dato** | **Descripción** |
|---------------|------------------|-----------------|
| `id`          | `INT`            | Identificador único de la venta. |
| `cliente_id`  | `INT`            | Identificador del cliente (relación con la tabla `clientes`). |
| `monto`       | `DECIMAL`        | Monto de la venta realizada. |
| `fecha`       | `DATE`           | Fecha en que se realizó la venta. |

---

Este repositorio contiene el archivo `consultas.sql`, que incluye las siguientes consultas para extraer información de las tablas `clientes` y `ventas`:

1. **Consulta para obtener los 5 clientes con mayor monto total de ventas en los últimos 6 meses.**
2. **Consulta para calcular el ticket promedio de ventas por cliente en el último año.**
3. **Consulta para obtener el nombre completo de los clientes y su monto total de ventas.**
4. **Consulta para obtener el ingreso promedio de ventas por mes.**
5. **Consulta para calcular el ranking de clientes por ventas en el último año.**
6. **Consulta para calcular el total de ventas por cliente y seleccionar solo aquellos cuyo total de ventas sea superior al promedio general.**

Cada una de estas consultas está diseñada para extraer información específica sobre las ventas de los clientes y ayudar en el análisis de datos para tomar decisiones informadas.
