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

# Estilo personalizado en paleta Rosa & Blanco
st.markdown("""
    <style>
    /* Fondo principal de la app */
    .stApp {
        background-color: #FFF5F7;
        color: #4A2E35;
    }
    
    /* Fondo de la barra lateral */
    [data-testid="stSidebar"] {
        background-color: #FFE4E1;
    }
    
    /* Estilo de las tarjetas / contenedores */
    [data-testid="stVerticalBlockBorderWrapper"] > div {
        background-color: #FFFFFF;
        border: 1px solid #FFB6C1 !important;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(255, 182, 193, 0.2);
    }
    
    /* Botones principales */
    .stButton>button, .stLinkButton>a {
        width: 100%;
        border-radius: 8px;
        background-color: #FFB6C1 !important;
        color: #4A2E35 !important;
        border: none !important;
        font-weight: bold;
    }
    
    .stButton>button:hover, .stLinkButton>a:hover {
        background-color: #FF69B4 !important;
        color: white !important;
    }
    
    /* Títulos y encabezados */
    h1, h2, h3 {
        color: #D87093 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Barra Lateral (Sidebar) - Identidad de Marca
with st.sidebar:
    st.title("🎨 Yoselin Álvarez")
    st.caption("Diseñadora Interactiva")
    
    st.markdown("""
    ¡Hola! 👋 Bienvenido a mi portafolio interactivo. Aquí exploro la intersección entre el **diseño de experiencia**, la **inteligencia artificial** y los **sistemas ciberfísicos**.
    """)
    
    st.divider()
    st.info("💡 **Tip:** Haz clic en los enlaces de cada tarjeta para probar los prototipos desplegados.")

# 3. Encabezado Principal
st.title("⚡ Portafolio de Proyectos e Inteligencia Artificial")
st.markdown("""
Esta colección reúne aplicaciones web interactivas, modelos de visión por computador, procesamiento de lenguaje natural y prototipos ciberfísicos desarrollados con **Python**, **Streamlit** y modelos de vanguardia.
""")

st.divider()

# Función auxiliar para cargar imágenes sin romper el layout si no existen
def cargar_imagen(nombre_archivo):
    if os.path.exists(nombre_archivo):
        return Image.open(nombre_archivo)
    return None

# 4. Rejilla de Proyectos (3 Columnas)
col1, col2, col3 = st.columns(3, gap="medium")

# --- COLUMNA 1 ---
with col1:
    with st.container(border=True):
        st.subheader("🗣️ Texto a Voz")
        img = cargar_imagen('txt_to_audio2.png')
        if img:
            st.image(img, use_container_width=True)
        st.write("Generador de voz sintetizada a partir de entrada de texto utilizando librerías multimodal.")
        st.link_button("Probar App ↗", "https://imultimod.streamlit.app/")

    with st.container(border=True):
        st.subheader("👁️ Detección de Objetos")
        img = cargar_imagen('txt_to_audio.png')
        if img:
            st.image(img, use_container_width=True)
        st.write("Identificación y segmentación de objetos en tiempo real con arquitecturas YOLOv5.")
        st.link_button("Probar App ↗", "https://yolov5cmc.streamlit.app/")

    with st.container(border=True):
        st.subheader("🧠 Modelos Personalizados")
        img = cargar_imagen('OIG5.jpg')
        if img:
            st.image(img, use_container_width=True)
        st.write("Implementación y despliegue de modelos de visión entrenados con conjuntos de datos propios.")
        st.link_button("Probar App ↗", "https://yolov5cmc.streamlit.app/")

# --- COLUMNA 2 ---
with col2:
    with st.container(border=True):
        st.subheader("🎙️ Voz a Texto")
        img = cargar_imagen('audio_to_txt.png')
        if img:
            st.image(img, use_container_width=True)
        st.write("Transcripción y reconocimiento de voz continua convertida a caracteres de texto.")
        st.link_button("Probar App ↗", "https://vvoztext.streamlit.app/")

    with st.container(border=True):
        st.subheader("📊 Análisis de Datos con Agentes")
        img = cargar_imagen('data_analisis.png')
        if img:
            st.image(img, use_container_width=True)
        st.write("Exploración e interpretación automatizada de datasets mediante agentes inteligentes.")
        st.link_button("Probar App ↗", "https://agenteanalisis.streamlit.app/")

    with st.container(border=True):
        st.subheader("📝 Transcriptor Multimedia")
        img = cargar_imagen('OIG2.jpg')
        if img:
            st.image(img, use_container_width=True)
        st.write("Procesamiento de archivos de audio y video para extracción e indexación de texto.")
        st.link_button("Probar App ↗", "https://vtranscrip.streamlit.app/")

# --- COLUMNA 3 ---
with col3:
    with st.container(border=True):
        st.subheader("📚 RAG en Documentos (PDF)")
        img = cargar_imagen('Chat_pdf.png')
        if img:
            st.image(img, use_container_width=True)
        st.write("Sistema de generación aumentada por recuperación para interactuar y consultar PDFs.")
        st.link_button("Probar App ↗", "https://ragpdf.streamlit.app/")

    with st.container(border=True):
        st.subheader("🔍 Análisis Visual con VLM")
        img = cargar_imagen('OIG3.jpg')
        if img:
            st.image(img, use_container_width=True)
        st.write("Evaluación razonada e interpretación del contexto de imágenes mediante modelos de visión-lenguaje.")
        st.link_button("Probar App ↗", "https://agente-vision.streamlit.app/")

    with st.container(border=True):
        st.subheader("🌐 Sistema Ciberfísico")
        img = cargar_imagen('OIG4.jpg')
        if img:
            st.image(img, use_container_width=True)
        st.write("Integración de sensores y actuadores con la nube para monitoreo e interacción en tiempo real.")
        st.link_button("Probar App ↗", "https://ciberfisico.streamlit.app/")

# 5. Pie de página
st.divider()
st.caption("Diseñado y desarrollado por Yoselin Álvarez © 2026 | Universidad EAFIT")
