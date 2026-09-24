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
    
    /* 7. Títulos */
    h1, h2, h3 {
        color: #C71585 !important;
        font-weight: 800 !important;
    }
    
    .stAlert {
        background-color: #FFF0F5 !important;
        border: 1px solid #FF69B4 !important;
        color: #2B1B22 !important;
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Barra Lateral (Sidebar)
with st.sidebar:
    st.title("🎨 Yoselin Álvarez")
    st.caption("Diseñadora Interactiva")
    st.markdown("""
    ¡Hola! 👋 Bienvenido a mi portafolio interactivo. Aquí presento **10 aplicaciones interactivas** enfocadas en IA, procesamiento de texto, visión por computador y análisis de datos.
    """)
    st.divider()
    st.info("💡 **Tip:** Haz clic en los botones de cada tarjeta para probar los prototipos.")

# 3. Encabezado Principal
st.title("⚡ Portafolio de Proyectos e Inteligencia Artificial")
st.markdown("""
Colección de 10 herramientas y demostraciones interactivas desarrolladas con **Python** y **Streamlit** para la materia de Inteligencia Artificial.
""")

st.divider()

# Función auxiliar para cargar imágenes
def cargar_imagen(nombre_archivo):
    if os.path.exists(nombre_archivo):
        return Image.open(nombre_archivo)
    return None

# 4. Rejilla de Proyectos (Ordenada Horizontalmente: 1, 2, 3 | 4, 5, 6 | 7, 8, 9 | 10)

# --- FILA 1 (Apps 1, 2, 3) ---
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    with st.container(border=True):
        st.subheader("1. 🚀 Mi Primera App (Intro)")
        img = cargar_imagen('OIG8.jpg')
        if img:
            st.image(img, use_container_width=True)
        st.write("Prototipo base con prueba de widgets, columnas y entradas de texto.")
        st.link_button("Probar App ↗", "https://4gzh5pcun8wvb4uwagf3pb.streamlit.app/")

with col2:
    with st.container(border=True):
        st.subheader("2. 🗣️ Texto a Audio")
        img = cargar_imagen('txt_to_audio2.png')
        if img:
            st.image(img, use_container_width=True)
        st.write("Sintetizador de voz que convierte entradas de texto en archivos de audio reproducibles.")
        st.link_button("Probar App ↗", "https://muft7fr6sdrf56gmap3rdk.streamlit.app")

with col3:
    with st.container(border=True):
        st.subheader("3. 🌐 Traductor")
        img = cargar_imagen('OIG2.jpg')
        if img:
            st.image(img, use_container_width=True)
        st.write("Herramienta de traducción automática multilingüe con procesamiento de lenguaje natural.")
        st.link_button("Probar App ↗", "https://clase7-bnkuljdihpt7zbva3lggy7.streamlit.app")

# --- FILA 2 (Apps 4, 5, 6) ---
col4, col5, col6 = st.columns(3, gap="medium")

with col4:
    with st.container(border=True):
        st.subheader("4. 📄 OCR")
        img = cargar_imagen('Chat_pdf.png')
        if img:
            st.image(img, use_container_width=True)
        st.write("Reconocimiento óptico de caracteres para extraer texto a partir de imágenes y documentos.")
        st.link_button("Probar App ↗", "https://ragpdf.streamlit.app/")

with col5:
    with st.container(border=True):
        st.subheader("5. 🔊 OCR Audio")
        img = cargar_imagen('audio_to_txt.png')
        if img:
            st.image(img, use_container_width=True)
        st.write("Extracción de texto desde imágenes con lectura asistida por sintesis de voz.")
        st.link_button("Probar App ↗", "https://vvoztext.streamlit.app/")

with col6:
    with st.container(border=True):
        st.subheader("6. ☁️ Word Cloud Studio")
        img = cargar_imagen('data_analisis.png')
        if img:
            st.image(img, use_container_width=True)
        st.write("Generador de nubes de palabras interactivas para análisis visual de frecuencias en texto.")
        st.link_button("Probar App ↗", "https://agenteanalisis.streamlit.app/")

# --- FILA 3 (Apps 7, 8, 9) ---
col7, col8, col9 = st.columns(3, gap="medium")

with col7:
    with st.container(border=True):
        st.subheader("7. 😊 Análisis de Sentimiento")
        img = cargar_imagen('OIG6.jpg')
        if img:
            st.image(img, use_container_width=True)
        st.write("Evaluación del tono emocional e intencionalidad en textos utilizando modelos NLP.")
        st.link_button("Probar App ↗", "https://agenteanalisis.streamlit.app/")

with col8:
    with st.container(border=True):
        st.subheader("8. 📊 TF-IDF en Español")
        img = cargar_imagen('OIG3.jpg')
        if img:
            st.image(img, use_container_width=True)
        st.write("Cálculo de relevancia de palabras clave en corpus de texto en español mediante algoritmo TF-IDF.")
        st.link_button("Probar App ↗", "https://agente-vision.streamlit.app/")

with col9:
    with st.container(border=True):
        st.subheader("9. 👁️ Detección de Objetos")
        img = cargar_imagen('txt_to_audio.png')
        if img:
            st.image(img, use_container_width=True)
        st.write("Identificación y delimitación de elementos en imágenes en tiempo real con modelos YOLO.")
        st.link_button("Probar App ↗", "https://yolov5cmc.streamlit.app/")

# --- FILA 4 (App 10) ---
col10, col11, col12 = st.columns(3, gap="medium")

with col10:
    with st.container(border=True):
        st.subheader("10. 🤖 Teachable Machine")
        img = cargar_imagen('OIG5.jpg')
        if img:
            st.image(img, use_container_width=True)
        st.write("Reconocimiento y clasificación de imágenes con modelos personalizados de Teachable Machine.")
        st.link_button("Probar App ↗", "https://yolov5cmc.streamlit.app/")

# 5. Pie de página
st.divider()
st.caption("Diseñado y desarrollado por Yoselin Álvarez © 2026 | Universidad EAFIT")
