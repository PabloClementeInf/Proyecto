from cmath import log
from pydub import AudioSegment
import numpy as np
from pvrecorder import PvRecorder
from scipy import signal
import wave, struct
import time
import librosa
import soundfile as sf
import random
import matplotlib.pyplot as plt
import os



class audio:
    
    def cargar_audio(nombre_archivo):
        ruta_archivo = nombre_archivo
        return AudioSegment.from_file(ruta_archivo)

    def procesar_audio_agudo(audio):
        ruta = "./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_agudo.wav"
        audio.export(nombre_salida, format="wav")
        y, sr = librosa.load(nombre_salida)

        nuevotono = librosa.effects.pitch_shift(y, sr=sr, n_steps=4)
        ruta = "./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_agudo.wav"
        sf.write(nombre_salida, nuevotono, sr)

    def procesar_audio_grave(audio):
        ruta = "./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_grave.wav"
        audio.export(nombre_salida, format="wav")
        y, sr = librosa.load(nombre_salida)

        nuevotono = librosa.effects.pitch_shift(y, sr=sr, n_steps=-4)
        ruta = "./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_grave.wav"
        sf.write(nombre_salida, nuevotono, sr)

    def procesar_audio_alien(audio):
        ruta = "./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_alien.wav"
        audio.export(nombre_salida, format="wav")
        y, sr = librosa.load(nombre_salida)
        t = np.arange(len(y)) / sr
        carrier = np.sin(2 * np.pi * 1500 * t)
        audio_alien = y * (2 * carrier)

        ruta = "./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_alien.wav"
        sf.write(nombre_salida, audio_alien, sr)

    def procesar_audio_radio(audio):
        # Cargar el audio de ruido de fondo de radio
        audio_radio = "./filter/radio.wav"
        radio = AudioSegment.from_wav(audio_radio)

        # Ajustar la duración del ruido de fondo al mismo que el audio original
        radio = radio[:len(audio)]

        # Ajustar el volumen del ruido de fondo
        ajuste = 10
        radio = radio - ajuste  # Ajustar el rango del volumen aquí

        audio = audio - 100
        # Mezclar el audio original con el ruido de fondo
        mixed_audio = audio.overlay(radio)
        # Creamos un audio auxiliar
        ruta = "./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_radio.wav"
        mixed_audio.export(nombre_salida, format="wav")
        y, sr = librosa.load(nombre_salida)
        # Aplicar la ecualización
        eq_audio = y * (10 ** (-10 / 20))

        # Normalizar el audio para evitar la distorsión
        eq_audio /= np.max(np.abs(eq_audio))
        ruta = "./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_radio.wav"
        sf.write(nombre_salida, eq_audio, sr)

    def procesar_audio_robot(audio):
        ruta = "./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_robot.wav"
        audio.export(nombre_salida, format="wav")
        y, sr = librosa.load(nombre_salida)
        # Obtener las frecuencias fundamentales (tonos) del audio
        pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

        # Ajustar las frecuencias fundamentales al tono deseado
        target_pitch = 11.0
        pitches = pitches * (target_pitch / np.mean(pitches))

        # Calcular la diferencia de tono entre las frecuencias originales y las ajustadas
        pitch_diff = np.mean(pitches, axis=0) - np.median(pitches)

        # Aplicar el cambio de tono al audio original frame por frame
        robot = np.zeros_like(y)
        for i, diff in enumerate(pitch_diff):
            y_frame = y[i * len(y) // len(pitch_diff):(i + 1) * len(y) // len(pitch_diff)]
            robot_frame = librosa.effects.pitch_shift(y_frame, sr=sr, n_steps=-diff)
            robot[i * len(y) // len(pitch_diff):(i + 1) * len(y) // len(pitch_diff)] = robot_frame

        # Exportar el resultado a un nuevo archivo de audio
        shifted = robot * (2 ** 31 - 1)  # Data ranges from -1.0 to 1.0
        robot = shifted.astype(np.int32)

        sound = AudioSegment(
            robot.tobytes(),
            frame_rate=sr,
            sample_width=np.dtype(robot.dtype).itemsize,
            channels=1
        )
        nuevoaudio = sound._spawn(sound.raw_data)
        ruta = "./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_robot.wav"
        nuevoaudio.export(nombre_salida, format="wav")

    def procesar_audio_cueva(audio):
        # Cargamos el filtro de cueva
        filter = AudioSegment.from_file("./filter/Cave.wav")
        # Transformamos de AudioSegment a array numpy
        filter1 = np.array(filter.get_array_of_samples())
        # Normalizamos el sonido
        filter_norm = filter1 / np.max(np.abs(filter1))

        # Transformamos el audio a un array numpy
        audio1 = np.array(audio.get_array_of_samples())

        # Utilizamos convolve para añadir el efecto al audio
        audio1_conv = signal.convolve(filter_norm, audio1)

        # Normalizamos de nuevo el audio
        audio1_conv = audio1_conv / np.max(np.abs(audio1_conv))

        # Transformamos de np.array a AudioSegment
        shifted = audio1_conv * (2 ** 31 - 1)  # Data ranges from -1.0 to 1.0
        audio1_conv = shifted.astype(np.int32)
        sound = AudioSegment(
            audio1_conv.tobytes(),
            frame_rate=audio.frame_rate,
            sample_width=np.dtype(audio1_conv.dtype).itemsize,
            channels=1
        )
        nuevoaudio = sound._spawn(sound.raw_data)
        ruta = "./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_cueva.wav"
        nuevoaudio.export(nombre_salida, format="wav")

    def grabar_audio():
        a = 0;

    def get_array_of_samples(self):
        return array.array(self.array_type, self._data)

audio_entrada = AudioSegment.from_file("./data/nombres.wav")

# Procesar el audio con todos los filtros
audio.procesar_audio_agudo(audio_entrada)
audio.procesar_audio_grave(audio_entrada)
audio.procesar_audio_alien(audio_entrada)
audio.procesar_audio_radio(audio_entrada)
audio.procesar_audio_robot(audio_entrada)
audio.procesar_audio_cueva(audio_entrada)

# Leer los archivos de audio procesados
audio_agudo = AudioSegment.from_wav("./data/audio_agudo.wav")
audio_grave = AudioSegment.from_wav("./data/audio_grave.wav")
audio_alien = AudioSegment.from_wav("./data/audio_alien.wav")
audio_radio = AudioSegment.from_wav("./data/audio_radio.wav")
audio_robot = AudioSegment.from_wav("./data/audio_robot.wav")
audio_cueva = AudioSegment.from_wav("./data/audio_cueva.wav")

# Graficar el audio de entrada
plt.figure(figsize=(12, 6))
plt.subplot(2, 3, 1)
plt.plot(audio_entrada.get_array_of_samples())
plt.title("Audio de entrada")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")

# Graficar el audio procesado por cada filtro
plt.subplot(2, 3, 2)
plt.plot(audio_agudo.get_array_of_samples())
plt.title("Audio agudo")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")

plt.subplot(2, 3, 3)
plt.plot(audio_grave.get_array_of_samples())
plt.title("Audio grave")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")

plt.subplot(2, 3, 4)
plt.plot(audio_alien.get_array_of_samples())
plt.title("Audio alien")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")

plt.subplot(2, 3, 5)
plt.plot(audio_radio.get_array_of_samples())
plt.title("Audio radio")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")

plt.subplot(2, 3, 6)
plt.plot(audio_robot.get_array_of_samples())
plt.title("Audio robot")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")

# Ajustar los espacios entre las subfiguras
plt.tight_layout()

# Mostrar las gráficas
plt.show()