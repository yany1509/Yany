import streamlit as st
import librosa
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

#1er commit: funciones para obtener las características generales del audio
def obtener_duracion(y, sr):
    return librosa.get_duration(y=y, sr=sr)

def obtener_tono(y, sr, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz("C7")):
    tono, _, _= librosa.pyin(y, fmin=fmin, fmax=fmax)
    tonoMedio=np.nanmean(tono)
    return tonoMedio

def obtener_tempo(y, sr):
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
    return tempo[0]


def obtener_velocidad(y, sr):
    return np.mean(librosa.feature.rms(y=y))


#2do commit: funciones para obtener el espectograma y la onda
def obtener_espectograma(audio, sr):
    S = librosa.feature.melspectrogram(y=audio, sr=sr)
    S_dB = librosa.power_to_db(S, ref=np.max)
    plt.figure(figsize=(10,4))
    librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Espectograma')
    plt.tight_layout()
    st.pyplot(plt)

def obtener_onda(audio, sr):
    fig, ax = plt.subplots()
    librosa.display.waveshow(y=audio, sr=sr, ax=ax)
    ax.set(title='Onda del Audio')
    st.pyplot(fig)
           
            
#3er commit: funciones para modificar velocidad y tempo
def cambiarVelocidad(audio, sr, velocidad):
    
    if len(audio)>0:
        audioModificado=librosa.effects.time_stretch(audio, rate=velocidad)
        if audioModificado is not None:
                    if audioModificado.ndim == 1:
                        audioModificado=np.expand_dims(audioModificado, axis=1)
                    elif audioModificado.ndim == 2 and audioModificado.shape[1] == 1:
                        audioModificado=audioModificado[:,0]

                    sf.write("audioModificado.wav",audioModificado, sr)
                    st.write("Reproducir nuevo audio")
                    st.audio("audioModificado.wav", format='audio/wav')  
    return audioModificado


