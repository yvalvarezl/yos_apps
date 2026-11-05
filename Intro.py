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

# Estilo personalizado: Botones blancos y tarjeta rosada ajustada
st.markdown("""
    <style>
    /* 1. Fondo de la barra superior */
    header[data-testid="stHeader"] {
        background-color: #FFD1DC !important;
    }
    
    /* 2. Fondo principal de la app */
    .stApp {
        background-color: #FFD1DC !important;
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

    /* 5. Estilo de las pestañas (st.tabs) */
    button[data-baseweb="tab"] {
        font-size: 1.1rem !important;
        font-weight: bold !important;
        color: #8B004B !important;
    }
    button[aria-selected="true"] {
        color: #FF1493 !important;
        border-bottom-color: #FF1493 !important;
    }

    /* 6. BOTONES BLANCOS dentro de tarjetas */
    .stButton>button, .stLinkButton>a {
        width: 100%;
        border-radius: 10px !important;
        background-color: #FFFFFF !important;
        color: #8B004B !important;
        border: 2px solid #FF69B4 !important;
        font-weight: bold !important;
        margin-top: 8px !important;
    }

    .stButton>button:hover, .stLinkButton>a:hover {
        background-color: #FF1493 !important;
        color: #FFFFFF !important;
        border-color: #FF1493 !important;
        box-shadow: 0 4px 10px rgba(255, 20, 147, 0.4) !important;
    }

    /* Títulos de la página */
    h1, h2 {
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

# Función auxiliar compacta para la tarjeta
def crear_tarjeta(titulo, desc, enlace, img_nombre=None):
    with st.container():
        # Encabezado apretado dentro del contenedor rosa
        st.markdown(f"""
            <div style="
                background-color: #FFB6C1;
                border: 2px solid #FF69B4;
                border-radius: 16px 16px 0px 0px;
                padding: 10px 14px 4px 14px;
                box-shadow: 0 4px 10px rgba(255, 105, 180, 0.2);
            ">
                <h3 style="color: #8B004B; margin: 0; font-size: 1.15rem; font-weight: 800; padding: 0;">{titulo}</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # Bloque inferior integrado con la imagen y el botón
        with st.container():
            st.markdown("""
                <style>
                div[data-testid="stVerticalBlock"] > div:has(div.card-body) {
                    background-color: #FFB6C1;
                    border: 2px solid #FF69B4;
                    border-top: none;
                    border-radius: 0px 0px 16px 16px;
                }
                </style>
            """, unsafe_allow_html=True)
            
            img = cargar_imagen(img_nombre) if img_nombre else None
            if img:
                st.image(img, use_container_width=True)
                
            st.caption(f"*{desc}*")
            st.link_button("Probar App ↗", enlace)

# --- SIDEBAR / BARRA LATERAL ---
with st.sidebar:
    st.title("🎨 Yoselin Álvarez")
    st.caption("*Diseñadora Interactiva*")
    st.write("---")
    st.write("¡Hola! 👋 Bienvenid@ a mi portafolio interactivo. Explora los prototipos desarrollados en la **Entrega 1** y la **Entrega 2** navegando por las pestañas superiores.")
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

    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        crear_tarjeta("1. 🚀 Mi Primera App", "Prototipo base con prueba de widgets, columnas y entradas de texto.", "https://4gzh5pcun8wvb4uwagf3pb.streamlit.app/", "primerapp.jpg")
    with col2:
        crear_tarjeta("2. 🗣️ Texto a Audio", "Sintetizador de voz que convierte entradas de texto en archivos de audio reproducibles.", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/", "textoaaudio.jpg")
    with col3:
        crear_tarjeta("3. 🌐 Traductor", "Herramienta de traducción automática multilingüe con procesamiento de lenguaje natural.", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/", "traductor.jpg")

    col4, col5, col6 = st.columns(3, gap="medium")
    with col4:
        crear_tarjeta("4. 📄 OCR", "Reconocimiento óptico de caracteres para extraer texto a partir de imágenes y documentos.", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/", "ocr.jpg")
    with col5:
        crear_tarjeta("5. 🔊 OCR Audio", "Extracción de texto desde imágenes con lectura asistida por síntesis de voz.", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/", "ocraudio.jpg")
    with col6:
        crear_tarjeta("6. ☁️ Word Cloud Studio", "Generador de nubes de palabras interactivas para análisis visual de frecuencias en texto.", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/", "wordcloud.jpg")

    col7, col8, col9 = st.columns(3, gap="medium")
    with col7:
        crear_tarjeta("7. 😊 Análisis Sentimiento", "Evaluación del tono emocional e intencionalidad en textos utilizando modelos NLP.", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/", "sentimiento.jpg")
    with col8:
        crear_tarjeta("8. 📊 TF-IDF Español", "Cálculo de relevancia de palabras clave en corpus de texto en español mediante algoritmo TF-IDF.", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/", "tfidf.jpg")
    with col9:
        crear_tarjeta("9. 👁️ Detección de Objetos", "Identificación y delimitación de elementos en imágenes en tiempo real.", "https://yosapps-bqstvwppbkbssmj6nvn72f.streamlit.app/", "identificador.jpg")

    col10, c_v1, c_v2 = st.columns(3, gap="medium")
    with col10:
        crear_tarjeta("10. 🤖 Teachable Machine Base", "Reconocimiento y clasificación de imágenes con modelos personalizados.", "https://teachablemachineyose.streamlit.app/", "identidad.jpg")

# ---------------------------------------------------------
# PESTAÑA 2: ENTREGA 2 (8 Aplicaciones)
# ---------------------------------------------------------
with tab2:
    st.markdown("### 🚀 Entrega 2: Visión por Computador, IA y Control Ciberfísico")
    st.write("Proyectos de RAG, Visión por Computador, Lienzos Generativos e IoT.")
    st.write("")

    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        crear_tarjeta("📈 Chat PDF", "Análisis conversacional e interacción con documentos PDF mediante arquitectura RAG.", "https://chatpdf-guuyxeyj6opc52mohgdjhw.streamlit.app/", "chatpdf.jpg")
    with c2:
        crear_tarjeta("👁️‍🗨️ App Vision", "Interpretación visual, auditoría multimodal y análisis de imágenes.", "https://visionapp-7glas3iqv3ivsgoncb8hbc.streamlit.app/", "vision.jpg")
    with c3:
        crear_tarjeta("✍️ Handwrite (MNIST)", "Predicción y reconocimiento de dígitos escritos a mano mediante redes neuronales.", "https://handwr-vcjhv2exufrmuhmhuwlmwh.streamlit.app/", "handwrite.jpg")

    c4, c5, c6 = st.columns(3, gap="medium")
    with c4:
        crear_tarjeta("🎨 Lienzo estelar", "Generador de fábulas e historias estelares a partir de bocetos y dibujos interactivos.", "https://drawrecog-bk7ffymwumpvkzfskyxde6.streamlit.app/", "fabula.jpg")
    with c5:
        crear_tarjeta("🪄 Tablero API Key", "Reconocimiento de trazos e interpretación de dibujos con autenticación de API.", "https://lienzoestelar.streamlit.app/", "tablero_api.jpg")
    with c6:
        crear_tarjeta("📡 Lector de Sensor MQTT", "Monitoreo y recepción de datos de telemetría de sensores en tiempo real desde ESP32 / Wokwi.", "https://recepmqtt-2cqknwecapwgv6ovblpic5.streamlit.app/", "sensor_mqtt.jpg")

    c7, c8, c_vac = st.columns(3, gap="medium")
    with c7:
        crear_tarjeta("🕹️ Control Servomotor MQTT", "Control presencial por visión y envío de comandos por MQTT al servomotor en Wokwi.", "https://sendcmqtt-scgitb537zhrtedqbdr6gq.streamlit.app/", "cerradura.jpg")
    with c8:
        crear_tarjeta("🎙️ Control por Voz", "Reconocimiento de comandos de voz para ejecutar acciones y enviar señales de control.", "https://ctrlvoice-yvijbccbux4an56bxmhamr.streamlit.app/", "control_voz.jpg")

st.write("---")
st.caption("Diseñado y desarrollado por Yoselin Álvarez © 2026 | Universidad EAFIT")
