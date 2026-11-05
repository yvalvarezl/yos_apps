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

# Estilo personalizado: Rosa tierno con cards en rosado más oscuro y opacidad
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

    /* 5. Tarjetas de proyectos (Rosado más oscuro con opacidad) */
    [data-testid="stVerticalBlockBorderWrapper"] > div {
        background-color: rgba(255, 182, 193, 0.45) !important;
        backdrop-filter: blur(8px);
        border: 2px solid #FF69B4 !important;
        border-radius: 16px;
        box-shadow: 0 6px 14px rgba(255, 105, 180, 0.25);
    }

    /* 6. Estilo de las pestañas (st.tabs) */
    button[data-baseweb="tab"] {
        font-size: 1.1rem !important;
        font-weight: bold !important;
        color: #8B004B !important;
    }
    button[aria-selected="true"] {
        color: #FF1493 !important;
        border-bottom-color: #FF1493 !important;
    }

    /* 7. Botones */
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
    st.write("¡Hola! 👋 Bienvenid@ a mi portafolio interactivo. Explora los prototipos desarrollados en la **Entrega 1** (10 aplicaciones) y la **Entrega 2** (8 aplicaciones) navegando por las pestañas superiores.")
    st.info("💡 **Tip:** Haz clic en los botones de cada tarjeta para probar las aplicaciones.")

# --- CONTENIDO PRINCIPAL ---
st.title("⚡ Portafolio de Proyectos e Inteligencia Artificial")
st.write("Colección de herramientas y demostraciones interactivas desarrolladas con **Python** y **Streamlit** para la materia de Interfaces multimodales.")
st.write("---")

# Pestañas principales
tab1, tab2 = st.tabs(["📦 Entrega 1", "🚀 Entrega 2"])

# ---------------------------------------------------------
# PESTAÑA 1: ENTREGA 1 (10 Aplicaciones)
# ---------------------------------------------------------
with tab1:
    st.markdown("### 📦 Entrega 1: Fundamentos de PNL y Procesamiento de Texto")
    st.write("Exploración inicial de sintetizadores de voz, traductores, reconocedores OCR, nubes de palabras, análisis de sentimiento y TF-IDF.")
    st.write("")

    # Fila 1
    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        with st.container(border=True):
            st.subheader("1. 🚀 Mi Primera App")
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

    # Fila 2
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

    # Fila 3
    col7, col8, col9 = st.columns(3, gap="medium")

    with col7:
        with st.container(border=True):
            st.subheader("7. 😊 Análisis Sentimiento")
            img = cargar_imagen('sentimiento.jpg')
            if img:
                st.image(img, use_container_width=True)
            st.caption("*Evaluación del tono emocional e intencionalidad en textos utilizando modelos NLP.*")
            st.link_button("Probar App ↗", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/")

    with col8:
        with st.container(border=True):
            st.subheader("8. 📊 TF-IDF Español")
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
            st.caption("*Identificación y delimitación de elementos en imágenes en tiempo real.*")
            st.link_button("Probar App ↗", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/")

    # Fila 4
    col10, col_v1, col_v2 = st.columns(3, gap="medium")

    with col10:
        with st.container(border=True):
            st.subheader("10. 🤖 Teachable Machine Base")
            img = cargar_imagen('identidad.jpg')
            if img:
                st.image(img, use_container_width=True)
            st.caption("*Reconocimiento y clasificación de imágenes con modelos personalizados.*")
            st.link_button("Probar App ↗", "https://teachablemachineyose.streamlit.app/")


# ---------------------------------------------------------
# PESTAÑA 2: ENTREGA 2 (8 Aplicaciones con formato Entrega 1)
# ---------------------------------------------------------
with tab2:
    st.markdown("### 🚀 Entrega 2: Visión por Computador, IA y Control Ciberfísico")
    st.write("Proyectos de RAG, Visión por Computador, Lienzos Generativos e IoT.")
    st.write("")

    # Fila 1
    c1, c2, c3 = st.columns(3, gap="medium")

    with c1:
        with st.container(border=True):
            st.subheader("📈 Chat PDF")
            img = cargar_imagen('chatpdf.jpg')
            if img:
                st.image(img, use_container_width=True)
            st.caption("*Análisis conversacional e interacción con documentos PDF mediante arquitectura RAG.*")
            st.link_button("Probar App ↗", "https://chatpdf-yos.streamlit.app/")

    with c2:
        with st.container(border=True):
            st.subheader("👁️‍🗨️ App Vision")
            img = cargar_imagen('vision.jpg')
            if img:
                st.image(img, use_container_width=True)
            st.caption("*Interpretación visual, auditoría multimodal y análisis de imágenes.*")
            st.link_button("Probar App ↗", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/")

    with c3:
        with st.container(border=True):
            st.subheader("✍️ Handwrite (MNIST)")
            img = cargar_imagen('handwrite.jpg')
            if img:
                st.image(img, use_container_width=True)
            st.caption("*Predicción y reconocimiento de dígitos escritos a mano mediante redes neuronales.*")
            st.link_button("Probar App ↗", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/")

    # Fila 2
    c4, c5, c6 = st.columns(3, gap="medium")

    with c4:
        with st.container(border=True):
            st.subheader("🎨 Tablero Propio - Fábula Infantil")
            img = cargar_imagen('fabula.jpg')
            if img:
                st.image(img, use_container_width=True)
            st.caption("*Generador de fábulas e historias mágicas a partir de bocetos y dibujos interactivos.*")
            st.link_button("Probar App ↗", "https://drawrecog-yos.streamlit.app/")

    with c5:
        with st.container(border=True):
            st.subheader("🪄 Tablero API Key")
            img = cargar_imagen('tablero_api.jpg')
            if img:
                st.image(img, use_container_width=True)
            st.caption("*Reconocimiento de trazos e interpretación de dibujos con autenticación de API.*")
            st.link_button("Probar App ↗", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/")

    with c6:
        with st.container(border=True):
            st.subheader("📡 Lector de Sensor MQTT")
            img = cargar_imagen('sensor_mqtt.jpg')
            if img:
                st.image(img, use_container_width=True)
            st.caption("*Monitoreo y recepción de datos de telemetría de sensores en tiempo real desde ESP32 / Wokwi.*")
            st.link_button("Probar App ↗", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/")

    # Fila 3
    c7, c8, c_vacio = st.columns(3, gap="medium")

    with c7:
        with st.container(border=True):
            st.subheader("🕹️ Control Servomotor MQTT")
            img = cargar_imagen('cerradura.jpg')
            if img:
                st.image(img, use_container_width=True)
            st.caption("*Control presencial por visión y envío de comandos por MQTT al servomotor en Wokwi.*")
            st.link_button("Probar App ↗", "https://clase14-tm-gestos-fisico-main.streamlit.app/3_Cerradura_Inteligente")

    with c8:
        with st.container(border=True):
            st.subheader("🎙️ Control por Voz")
            img = cargar_imagen('control_voz.jpg')
            if img:
                st.image(img, use_container_width=True)
            st.caption("*Reconocimiento de comandos de voz para ejecutar acciones y enviar señales de control.*")
            st.link_button("Probar App ↗", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/")

st.write("---")
st.caption("Diseñado y desarrollado por Yoselin Álvarez © 2026 | Universidad EAFIT")
