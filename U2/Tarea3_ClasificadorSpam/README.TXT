*ADVERTENCIA*: El rar contiene el proyecto para poder ejecutar el programa, ya que se cuenta con algunas carpetas, el codigo en el repositorio es para ver el codigo sin embargo no ejecutará por si solo.

--- Explicación del Código: Sistema Detector de SPAM con Naive Bayes ---

Este código implementa un sistema de detección de SPAM utilizando un modelo de Naive Bayes. 
Se encarga de cargar un conjunto de datos, preprocesar los textos, 
entrenar el modelo y hacer predicciones sobre nuevos correos electronicos.

El código comienza importando las librerias necesarias, a continuación se da una breve descripción:

-pandas: Para el manejo de datos

-numpy: Nos da acceso a funciones matematicas mas complejas y a una representación
de los datos mas eficiente

-sklearn.feature_extraction.text.TfidfVectorizer: Para convertir el texto en vectores numéricos.

-sklearn.model_selection.train_test_split: Para dividir los datos en entrenamiento y prueba.

-sklearn.metrics.precision_score, recall_score: Para evaluar el modelo.

-nltk: Para el procesamiento de texto, como la tokenización y 
eliminación de palabras vacías (stopwords).

-datetime: Para manejar fechas en los correos electrónicos.
------------------------------------------------------------------
1. Carga y Limpieza de Datos

Función: cargar_datos_y_limpiarlos(archivo)

- Carga los datos desde un archivo CSV.
- Elimina filas duplicadas basadas en la columna text.
- Convierte el texto a minúsculas y elimina caracteres especiales.
- Tokeniza las palabras y elimina las "stopwords" en inglés.
- Asegura que la columna target contenga valores numéricos, eliminando filas con valores no válidos.
------------------------------------------------------------------
2. Entrenamiento del Modelo

Función: entrenar_naive_bayes(matriz_caracteristicas, etiquetas)

- Calcula la probabilidad de que un correo sea SPAM o no (basado en la columna target).
- Separa las características de los correos en dos clases: SPAM y no SPAM.
- Calcula la probabilidad de que cada palabra en ambos casos, utilizando 
(α = 1e-10) para evitar probabilidades de cero.
------------------------------------------------------------------
3. Predicción con el Modelo

Función: predecir_naive_bayes(matriz_caracteristicas, prob_spam, prob_no_spam, 
prob_palabras_spam, prob_palabras_no_spam)

- Calcula la probabilidad logarítmica de que un correo pertenezca a cada clase (SPAM o no SPAM).
- Devuelve 1 si la probabilidad de SPAM es mayor, de lo contrario, devuelve 0.
------------------------------------------------------------------
4. Evaluación del Modelo

- Se entrena un vectorizador TF-IDF (TfidfVectorizer) para transformar el texto a representaciones numéricas.
- Se entrena el modelo Naive Bayes con los datos procesados.
- Se generan predicciones y se evalúa el modelo calculando la precisión y la recuperación.
------------------------------------------------------------------
5. Predicción de Correos Nuevos por Consola

Función: predecir_texto(vectorizador, modelo, texto)

- Procesa un correo ingresado por el usuario, eliminando las stopwords.
- Convierte el texto en su representación TF-IDF.
- Utiliza el modelo para predecir si el correo es SPAM o no.
------------------------------------------------------------------
6. Interacción con el Usuario

- El usuario ingresa: Su correo electrónico, Nombre, Asunto y Mensaje.
- El sistema procesa el mensaje, lo clasifica como spam o no spam y muestra el resultado. 
  Permite decidir si enviar otro correo o salir.
