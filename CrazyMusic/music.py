import matplotlib.colorbar
import matplotlib.figure
import matplotlib.pyplot as plt
import matplotlib.tight_layout
import streamlit as st
import librosa
import numpy as np
import funcionesLogicas as fl
import matplotlib
import soundfile as sf
import base64

#Función para cargar audio
def cargar_audio():
    st.sidebar.header("Carga de Audio")
    archivo = st.sidebar.file_uploader("Sube un archivo de audio", type=["wav", "mp3"])
    if archivo is not None:
        audio, sr = librosa.load(archivo, sr=None)
        st.session_state['audio'] = audio  # Guardar audio en session_state
        st.session_state['sr'] = sr  # Guardar sample rate en session_state
        st.write("### Vista previa del audio")
        st.audio(archivo)
        return audio, sr
    return None, None

# Función para explorar audio
def explorar_audio():
    st.sidebar.header("Exploración de Audio")
    audio = st.session_state.get('audio')
    sr = st.session_state.get('sr')
    
    if audio is not None and sr is not None:
        if st.sidebar.checkbox("Mostrar características del audio"):
            duracion = fl.obtener_duracion(audio, sr)
            tempo= fl.obtener_tempo(audio, sr)
            velocidad = fl.obtener_velocidad(audio, sr)
            st.write("### Características del audio")
            st.write(f"**Duración:** {duracion:.2f} segundos")
            st.write(f"**Tempo:** {tempo:.2f} BPM")
            st.write(f"**Velocidad (RMS):** {velocidad:.4f}")
            
    else:
        st.write("No se ha cargado ningún audio.")

#Función para graficar espectograma y onda
def graficarDatos():
    st.sidebar.header("Graficar Datos")
    audio = st.session_state.get('audio')
    sr = st.session_state.get('sr')
    
    if audio is not None and sr is not None:
    
          if st.sidebar.checkbox("Mostrar espectograma"):
            # Mostrar espectrograma
            fl.obtener_espectograma(audio, sr)

          if st.sidebar.checkbox("Mostrar onda"):
            # Mostrar onda del audio
            fl.obtener_onda(audio, sr)
    
#función para modificar velocidad y tempo        
def modificarDatos():
    st.sidebar.header("Modificar Datos")
    audio = st.session_state.get('audio')
    sr = st.session_state.get('sr')

    if audio is not None and sr is not None:
        if st.sidebar.checkbox("Modificar características del audio"):
            velocidad=st.sidebar.slider("Velocidad", 0.5, 2.0, 1.0)
            audio=fl.cambiarVelocidad(audio, sr, velocidad)
            
#Funcion para poner imagen de fondo
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)



# Ejemplo de uso
if __name__ == "__main__":
    st.set_page_config(
    page_title="LyricFlow",
    layout="wide", #centered
    initial_sidebar_state="expanded",
    )
    st.subheader("Aplicación de análisis y manipulación de audios")
    st.markdown("""Esta aplicación te permite subir un archivo de audio, visualizar varias de sus características,poder modificar algunas de estas como el tempo o la velocidad y además ver el espectograma""")
    set_background('C:/Users/Yanisbe LA KUKY/Desktop/New folder (2)/imagen21.jpg')
    cargar_audio()
    explorar_audio()
    graficarDatos()
    modificarDatos()