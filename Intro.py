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

# Estilo personalizado: Rosa tierno e intenso con alta legibilidad
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

    /* 5. Tarjetas de proyectos */
    [data-testid="stVerticalBlockBorderWrapper"] > div {
        background-color: #FFFFFF !important;
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
    st.write("¡Hola! 👋 Bienvenid@ a mi portafolio interactivo. Explora los prototipos desarrollados en la **Entrega 1** y la **Entrega 2** navegando por las pestañas superiores.")
    st.info("💡 **Tip:** Haz clic en los botones de cada tarjeta para probar las aplicaciones.")

# --- CONTENIDO PRINCIPAL ---
st.title("⚡ Portafolio de Proyectos e Inteligencia Artificial")
st.write("Colección de herramientas y demostraciones interactivas desarrolladas con **Python** y **Streamlit** para la materia de Interfaces multimodales.")
st.write("---")

# Pestañas para organizar la Entrega 1 y la Entrega 2
tab1, tab2 = st.tabs(["📦 Entrega 1 (NLP & Procesamiento)", "🚀 Entrega 2 (Visión & Control IoT)"])

# ---------------------------------------------------------
# PESTAÑA 1: ENTREGA 1 (Proyectos 1 al 8)
# ---------------------------------------------------------
with tab1:
    st.markdown("### 📦 Entrega 1: Fundamentos de PNL y Procesamiento de Texto")
    st.write("Exploración inicial de sintetizadores de voz, traductores, reconocedores OCR, análisis de sentimiento y TF-IDF.")
    st.write("")

    # Fila 1: Proyectos 1, 2 y 3
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
                st.image(img,
