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

# Estilo personalizado: Fondo rosa suave semitransparente con texto oscuro legibilidad alta
st.markdown("""
    <style>
    /* 1. Barra superior limpia e integrada */
    header[data-testid="stHeader"] {
        background-color: rgba(255, 240, 243, 0.95) !important;
    }
    
    /* 2. Fondo principal (Rosita suave con transparencia) */
    .stApp {
        background-color: rgba(255, 240, 243, 0.95);
        color: #1A1A1A !important;
    }
    
    /* 3. Fondo de la barra lateral (Rosa pastel suave semitransparente) */
    [data-testid="stSidebar"] {
        background-color: rgba(255, 228, 230, 0.95) !important;
    }

    /* 4. Color del texto principal y de la barra lateral */
    .stApp p, .stApp span, .stApp label, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        color: #1A1A1A !important;
        font-weight: 500;
    }
    
    /* 5. Tarjetas / Contenedores en blanco puro para destacar los proyectos */
    [data-testid="stVerticalBlockBorderWrapper"] > div {
        background-color: #FFFFFF !important;
        border: 1px solid #FFB6C1 !important;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(255, 182, 193, 0.25);
    }
    
    /* 6. Botones en tono rosa con texto oscuro destacado */
    .stButton>button, .stLinkButton>a {
        width: 100%;
        border-radius: 8px;
        background-color: #FFB6C1 !important;
        color: #1A1A1A !important;
        border: none !important;
        font-weight: bold !important;
    }
    
    .stButton>button:hover, .stLinkButton>a:hover {
        background-color: #FF69B4 !important;
        color: #FFFFFF !important;
    }
    
    /* 7. Títulos principales y subtítulos */
    h1, h2, h3 {
        color: #C71585 !important;
        font-weight: 700 !important;
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
