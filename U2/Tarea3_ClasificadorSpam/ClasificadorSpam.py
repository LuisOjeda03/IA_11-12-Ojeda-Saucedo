import datetime
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from datetime import date

def cargar_datos_y_limpiarlos(archivo):
    # Carga un archivo CSV, limpia los datos y los prepara para el modelo.
    datos = pd.read_csv(archivo, low_memory=False)
    
    # Eliminar filas duplicadas
    datos = datos.drop_duplicates(subset=['text'])
    
    # Convertir texto a minusculas y eliminar caracteres especiales
    datos['text'] = datos['text'].str.lower().str.replace('[^a-zA-Z0-9]', ' ', regex=True)
    
    # Cargar stopwords en inglés y eliminar palabras vacias
    stop_words = set(stopwords.words('english'))
    datos['text'] = datos['text'].apply(lambda texto: ' '.join(
        [palabra for palabra in word_tokenize(texto) if palabra not in stop_words]))
    
    # Asegurar que la columna 'target' contenga valores numéricos
    datos['target'] = pd.to_numeric(datos['target'], errors='coerce')
    datos = datos.dropna(subset=['target'])
    
    return datos

def entrenar_naive_bayes(matriz_caracteristicas, etiquetas):
    # Entrena un modelo de Naive Bayes desde cero.
    probabilidad_spam = etiquetas.mean()
    probabilidad_no_spam = 1 - probabilidad_spam
    
    # Separar características por clase
    caracteristicas_spam = matriz_caracteristicas[etiquetas == 1]
    caracteristicas_no_spam = matriz_caracteristicas[etiquetas == 0]
    
    # Evitar ceros en probabilidades
    alpha = 1e-10
    
    probabilidad_palabras_dado_spam = (caracteristicas_spam.sum(axis=0) + alpha) / (caracteristicas_spam.sum() + alpha * matriz_caracteristicas.shape[1])
    probabilidad_palabras_dado_no_spam = (caracteristicas_no_spam.sum(axis=0) + alpha) / (caracteristicas_no_spam.sum() + alpha * matriz_caracteristicas.shape[1])
    
    return probabilidad_spam, probabilidad_no_spam, probabilidad_palabras_dado_spam, probabilidad_palabras_dado_no_spam

def predecir_naive_bayes(matriz_caracteristicas, prob_spam, prob_no_spam, prob_palabras_spam, prob_palabras_no_spam):
    # Realiza predicciones con el modelo de Naive Bayes entrenado.
    log_prob_spam = np.log(prob_spam) + matriz_caracteristicas.dot(np.log(prob_palabras_spam.T)).A.flatten()
    log_prob_no_spam = np.log(prob_no_spam) + matriz_caracteristicas.dot(np.log(prob_palabras_no_spam.T)).A.flatten()
    
    return np.where(log_prob_spam > log_prob_no_spam, 1, 0)

def predecir_texto(vectorizador, modelo, texto):
    # Predice si un correo ingresado por consola es spam o no.
    texto_procesado = texto.lower()
    texto_procesado = ' '.join([palabra for palabra in word_tokenize(texto_procesado) if palabra not in stopwords.words('english')])
    texto_vectorizado = vectorizador.transform([texto_procesado])
    prediccion = predecir_naive_bayes(texto_vectorizado, *modelo)
    return "spam" if prediccion[0] == 1 else "no spam"

def main():
    #Ejecuta todo el proceso: carga de datos, entrenamiento y evaluación.
    datos = cargar_datos_y_limpiarlos("spam_assassin.csv")
    
    # Convertir texto en vectores numéricos con TF-IDF
    vectorizador = TfidfVectorizer(max_features=5000)
    datos_entrenamiento = vectorizador.fit_transform(datos['text'])
    
    # Entrenar modelo
    modelo = entrenar_naive_bayes(datos_entrenamiento, datos['target'].values)
    
    # Hacer predicciones
    predicciones_entrenamiento = predecir_naive_bayes(datos_entrenamiento, *modelo)
    
    # Evaluación del modelo
    precision = precision_score(datos['target'], predicciones_entrenamiento)
    recuperacion = recall_score(datos['target'], predicciones_entrenamiento)
    
    print("\n =========== Resultados ===============")
    print(f"Precision: {precision:.4f}")
    print(f"Recuperacion: {recuperacion:.4f}")
    return vectorizador, modelo
    
if __name__ == "__main__":
    vectorizador, modelo = main()

    # Entrada de usuario para predecir un correo nuevo
    opcion = 1
    while(opcion == 1):
        print("==============================")
        print("Sistema detector de SPAM ")
        correo = input("\nCorreo propio: ")
        nombre = input("\nNombre: ")
        asunto = input("\nAsunto: ")
        mensaje = input("\nMensaje: ")

        fecha = date.today()
        
        strEjemplo = f"" \
        f"From: \"{nombre}\" <{correo}>" \
        f"Subject: {asunto} " \
        f"Date: {fecha} " \
        "" \
        f"{mensaje}"
        print()
        resultado = predecir_texto(vectorizador, modelo, strEjemplo)
        print(f"El correo ingresado es: {resultado}")  
        print
        opcion = int(input("1 - Enviar Correo    2 - Salir: "))