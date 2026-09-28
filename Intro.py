import streamlit as st
from PIL import Image
import os

# 1. Configuración general de la página
st.set_page_config(
    page_title="Portafolio | Yoselin Álvarez",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo personalizado: Rosa tierno con tarjetas blancas sólidas y limpias
st.markdown("""
    <style>
    /* 1. Fondo de la barra superior */
    header[data-testid="stHeader"] {
        background-color: #FFD1DC !important;
    }
    
    /* 2. Fondo principal de la app */
    .stApp {
        background-color: #FFD1DC;
        color: #1A1A1A !important;
    }

    /* 3. Fondo de la barra lateral */
    [data-testid="stSidebar"] {
        background-color: #FFC0CB !important;
    }

    /* 4. Texto general */
    .stApp p, .stApp span, .stApp label, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        color: #2B1B22 !important;
        font-weight: 500;
    }

    /* 5. Tarjetas de proyectos (Blanco casi puro con borde sutil rosa) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: rgba(255, 255, 255, 0.92) !important;
        border-radius: 16px;
    }

    [data-testid="stVerticalBlockBorderWrapper"] > div {
        background-color: rgba(255, 255, 255, 0.92) !important;
        border: 2px solid #FF8DA1 !important;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }

    /* 6. Botones */
    .stButton>button, .stLinkButton>a {
        width: 100%;
        border-radius: 10px;
        background-color: #FFB6C1 !important;
        color: #2B1B22 !important;
        border: 1px solid #FF69B4 !important;
        font-weight: bold !important;
    }

    .stButton>button:hover, .stLinkButton>a:hover {
        background-color: #FF1493 !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 10px rgba(255, 20, 147, 0.4);
    }

    /* Títulos y Subtítulos */
    h1, h2, h3, h4, h5, h6 {
        color: #8B004B !important;
        font-weight: 800 !important;
    }

    /* Ocultar menú de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Función aux para cargar imágenes sin fallar si no existen
def cargar_imagen(nombre):
    if os.path.exists(nombre):
        return Image.open(nombre)
    return None

# --- SIDEBAR / BARRA LATERAL ---
with st.sidebar:
    st.title("🎨 Yoselin Álvarez")
    st.caption("*Diseñadora Interactiva*")
    st.write("---")
    st.write("¡Hola! 👋 Bienvenid@ a mi portafolio interactivo. Aquí presento **10 aplicaciones interactivas** enfocadas en IA, procesamiento de texto, visión por computador y análisis de datos.")
    st.info("💡 **Tip:** Haz clic en los botones de cada tarjeta para probar los prototipos.")

# --- CONTENIDO PRINCIPAL ---
st.title("⚡ Portafolio de Proyectos e Inteligencia Artificial")
st.write("Colección de 10 herramientas y demostraciones interactivas desarrolladas con **Python** y **Streamlit** para la materia de Interfaces multimodales.")
st.write("---")

# Fila 1: Proyectos 1, 2 y 3
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    with st.container(border=True):
        st.subheader("1. 🚀 Mi Primera App (Intro)")
        img = cargar_imagen('primerapp.jpg')
        if img:
            st.image(img, use_container_width=True)
        st.caption("*Prototipo base con prueba de widgets, columnas y entradas de texto.*")
        st.link_button("Probar App ↗", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/")

with col2:
    with st.container(border=True):
        st.subheader("2. 🗣️ Texto a Audio")
        img = cargar_imagen('textoaaudio.jpg')
        if img:
            st.image(img, use_container_width=True)
        st.caption("*Sintetizador de voz que convierte entradas de texto en archivos de audio reproducibles.*")
        st.link_button("Probar App ↗", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/")

with col3:
    with st.container(border=True):
        st.subheader("3. 🌐 Traductor")
        img = cargar_imagen('traductor.jpg')
        if img:
            st.image(img, use_container_width=True)
        st.caption("*Herramienta de traducción automática multilingüe con procesamiento de lenguaje natural.*")
        st.link_button("Probar App ↗", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/")

# Fila 2: Proyectos 4, 5 y 6
col4, col5, col6 = st.columns(3, gap="medium")

with col4:
    with st.container(border=True):
        st.subheader("4. 📄 OCR")
        img = cargar_imagen('ocr.jpg')
        if img:
            st.image(img, use_container_width=True)
        st.caption("*Reconocimiento óptico de caracteres para extraer texto a partir de imágenes y documentos.*")
        st.link_button("Probar App ↗", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/")

with col5:
    with st.container(border=True):
        st.subheader("5. 🔊 OCR Audio")
        img = cargar_imagen('ocraudio.jpg')
        if img:
            st.image(img, use_container_width=True)
        st.caption("*Extracción de texto desde imágenes con lectura asistida por síntesis de voz.*")
        st.link_button("Probar App ↗", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/")

with col6:
    with st.container(border=True):
        st.subheader("6. ☁️ Word Cloud Studio")
        img = cargar_imagen('wordcloud.jpg')
        if img:
            st.image(img, use_container_width=True)
        st.caption("*Generador de nubes de palabras interactivas para análisis visual de frecuencias en texto.*")
        st.link_button("Probar App ↗", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/")

# Fila 3: Proyectos 7, 8 y 9
col7, col8, col9 = st.columns(3, gap="medium")

with col7:
    with st.container(border=True):
        st.subheader("7. 😊 Análisis de Sentimiento")
        img = cargar_imagen('sentimiento.jpg')
        if img:
            st.image(img, use_container_width=True)
        st.caption("*Evaluación del tono emocional e intencionalidad en textos utilizando modelos NLP.*")
        st.link_button("Probar App ↗", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/")

with col8:
    with st.container(border=True):
        st.subheader("8. 📊 TF-IDF en Español")
        img = cargar_imagen('tfidf.jpg')
        if img:
            st.image(img, use_container_width=True)
        st.caption("*Cálculo de relevancia de palabras clave en corpus de texto en español mediante algoritmo TF-IDF.*")
        st.link_button("Probar App ↗", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/")

with col9:
    with st.container(border=True):
        st.subheader("9. 👁️ Detección de Objetos")
        img = cargar_imagen('identificador.jpg')
        if img:
            st.image(img, use_container_width=True)
        st.caption("*Identificación y delimitación de elementos en imágenes en tiempo real con modelos YOLO.*")
        st.link_button("Probar App ↗", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/")

# Fila 4: Proyecto 10
col10, col_vacía1, col_vacía2 = st.columns(3, gap="medium")

with col10:
    with st.container(border=True):
        st.subheader("10. 🤖 Teachable Machine")
        img = cargar_imagen('identidad.jpg')
        if img:
            st.image(img, use_container_width=True)
        st.caption("*Reconocimiento y clasificación de imágenes con modelos personalizados de Teachable Machine.*")
        st.link_button("Probar App ↗", "https://teachablemachineyose.streamlit.app/")

st.write("---")
st.caption("Diseñado y desarrollado por Yoselin Álvarez © 2026 | Universidad EAFIT")
