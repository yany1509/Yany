import music as ms
import streamlit as st


st.set_page_config(
    page_title="LyricFlow",
    layout="wide", #centered
    initial_sidebar_state="expanded",
    )
st.subheader("Aplicación de análisis y manipulación de audios")
st.markdown("""Esta aplicación te permite subir un archivo de audio, visualizar varias de sus características,poder modificar algunas de estas como el tempo o la velocidad y además ver el espectograma""")
ms.set_background('imagen21.jpg')

# Cargar los datos al iniciar la aplicación
if 'audio' not in st.session_state and 'sr' not in st.session_state:
    ms.cargar_audio()

if 'audio' in st.session_state and 'sr'  in st.session_state:
    ms.explorar_audio()
    ms.graficarDatos()
    ms.modificarDatos()

