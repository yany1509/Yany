# Proyecto de Procesamiento de Audio con Streamlit y Librosa: LyricFlow

## Descripción:
Este proyecto permite subir un archivo de audio a una aplicación web creada con Streamlit, y muestra varias características del audio como su velocidad, tempo, duración, espectrograma, forma de onda, y permite cambiar la velocidad del audio.

## Requisitos
- Python 3.8 o 3.10
- Streamlit
- Librosa
- Numpy 1.24
- Matplotlib
- Soundfile

Puedes instalar los requisitos con el siguiente comando:

```bash
pip install streamlit librosa numpy matplotlib soundfile
```

## Uso

1. Clona este repositorio:

```bash
git clone https://github.com/yany1509/Yany.git
```

2. Ejecuta la aplicación de Streamlit:

```bash
streamlit run mainMusic.py
```

3. Sube un archivo de audio a través de la interfaz de usuario de Streamlit.

## Funcionalidades

- **Carga de Audio**: Permite subir archivos de audio en formato WAV, MP3, etc.
- **Extracción de Características**: Muestra la velocidad, tempo y duración del audio.
- **Visualización**: Muestra el espectrograma y la forma de onda del audio.
- **Modificación de Velocidad**: Permite cambiar la velocidad del audio.

## Estructura del Proyecto

```
├── funcionesLogicas.py : contiene las funciones para obtener las diferentes caracterísiticas, el espectograma, la onda y cambiar velocidad
├── mainMusic.py: para ejecutar la aplicación
├── music.py: contiene las funciones de la interfaz de streamlit
└── README.md
```
## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request para discutir cualquier cambio.

## Licencia

Este proyecto está bajo la Licencia MIT. (profe aquí no sabía muy bien que poner)

