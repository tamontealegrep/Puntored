# **Predicción de Default en Créditos Bancarios**

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

## **Estructura del Repositorio**  
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
│── README.md           <- Documentación del proyecto  


--------


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