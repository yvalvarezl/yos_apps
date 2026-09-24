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
    
    /* 2. Fondo principal de la app (Rosa tierno v%C3%ADvido) */
    .stApp {
        background-color: #FFD1DC;
        color: #1A1A1A !important;
    }
    
    /* 3. Fondo de la barra lateral (Rosa dulce) */
    [data-testid="stSidebar"] {
        background-color: #FFC0CB !important;
    }

    /* 4. Texto general en negro/marr%C3%B3n oscuro bien n%C3%ADtido */
    .stApp p, .stApp span, .stApp label, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        color: #2B1B22 !important;
        font-weight: 500;
    }
    
    /* 5. Tarjetas/Contenedores de proyectos en blanco con sombra y borde rosa fucsia */
    [data-testid="stVerticalBlockBorderWrapper"] > div {
        background-color: #FFFFFF !important;
        border: 2px solid #FF69B4 !important;
        border-radius: 16px;
        box-shadow: 0 6px 14px rgba(255, 105, 180, 0.25);
    }
    
    /* 6. Botones rosados con texto oscuro y borde suave */
    .stButton>button, .stLinkButton>a {
        width: 100%;
        border-radius: 10px;
        background-color: #FFB6C1 !important;
        color: #2B1B22 !important;
        border: 1px solid #FF69B4 !important;
        font-weight: bold !important;
    }
    
    /* Efecto al pasar el cursor por los botones */
    .stButton>button:hover, .stLinkButton>a:hover {
        background-color: #FF1493 !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 10px rgba(255, 20, 147, 0.4);
    }
    
    /* 7. T%C3%ADtulos principales en Magenta/Fucsia dulce */
    h1, h2, h3 {
        color: #C71585 !important;
        font-weight: 800 !important;
    }
    
    /* Ajuste de cajas informativas (st.info) */
    .stAlert {
        background-color: #FFF0F5 !important;
        border: 1px solid #FF69B4 !important;
        color: #2B1B22 !important;
        border-radius: 12px;
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
