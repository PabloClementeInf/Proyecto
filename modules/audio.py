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

class audio:
    

    #ruta="/Users/amade/Documents/GitHub/Proyecto/data/audionuevo"
    
    def cargar_audio(nombre_archivo):
        ruta_archivo = nombre_archivo
        return AudioSegment.from_file(ruta_archivo[0])


    def procesar_audio_agudo(audio):
        
        ruta="./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_agudo.wav"
        audio.export(nombre_salida, format="wav")
        y, sr = librosa.load('./data/audio_agudo.wav')

        nuevotono = librosa.effects.pitch_shift(y,sr=sr,n_steps=4)
        ruta="./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_agudo.wav"
        sf.write(nombre_salida, nuevotono,sr)
    
    def procesar_audio_ave(audio):
        
        ruta="./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_grave.wav"
        audio.export(nombre_salida, format="wav")
        y, sr = librosa.load('./data/audio_grave.wav')

        nuevotono = librosa.effects.pitch_shift(y,sr=sr,n_steps=-4)
        ruta="./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_grave.wav"
        sf.write(nombre_salida, nuevotono,sr)

    def procesar_audio_alien(audio):
        #Creamos un audio auxiliar
        ruta="./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_alien.wav"
        audio.export(nombre_salida, format="wav")
        y, sr = librosa.load('./data/audio_alien.wav')
        t = np.arange(len(y)) / sr
        carrier = np.sin(2 * np.pi * 1500 * t)
        audio_alien = y * (2 * carrier)

        ruta="./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_alien.wav"
        sf.write(nombre_salida, audio_alien,sr)

    def procesar_audio_grave(audio):

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
        #Creamos un audio auxiliar
        ruta="./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_radio.wav"
        mixed_audio.export(nombre_salida, format="wav")
        y, sr = librosa.load('./data/audio_radio.wav')
        # Aplicar la ecualización
        eq_audio = y * (10 ** (-10 / 20))

        # Normalizar el audio para evitar la distorsión
        eq_audio /= np.max(np.abs(eq_audio))
        ruta="./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_radio.wav"
        sf.write(nombre_salida, eq_audio,sr)


    def procesar_audio_cueva(audio):
        #Cargamos el filtro de cueva
        filter = AudioSegment.from_file("./filter/Cave.wav")
        #Transformamos de AudioSegment a array numpy
        filter1 = np.array(filter.get_array_of_samples())
        #Normalizamos el sonido
        filter_norm = filter1 / np.max(np.abs(filter1))

        #Transformamos el audio a un array numpy
        audio1 = np.array(audio.get_array_of_samples())

        #Utilizamos convolve para añadir el efecto al audio
        audio1_conv = signal.convolve(filter_norm, audio1)

        #Normalizamos de nuevo el audio
        audio1_conv = audio1_conv/ np.max(np.abs(audio1_conv))

        #Transformamos de np.array a AudioSegment
        shifted = audio1_conv * (2 ** 31 - 1)   # Data ranges from -1.0 to 1.0
        audio1_conv = shifted.astype(np.int32)
        sound = AudioSegment(
            audio1_conv.tobytes(),
            frame_rate=audio.frame_rate,
            sample_width = np.dtype(audio1_conv.dtype).itemsize,
            channels=1
        )
        nuevoaudio = sound._spawn(sound.raw_data)
        ruta="./data/audionuevo"
        nombre_salida = f"{ruta[:-5]}_cueva.wav"
        nuevoaudio.export(nombre_salida, format="wav")

    def grabar_audio():
        #for index, device in enumerate(PvRecorder.get_audio_devices()):
                #print(f"[{index}] {device}")
        recorder = PvRecorder(device_index=0, frame_length=512)
        audio=[]
        ruta="./data/audionuevo.wav"
        recorder.start()
        timeout = 5
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
                frame = recorder.read()
                audio.extend(frame)
        recorder.stop()
        with wave.open(ruta, 'w') as f:
                f.setparams((1,2,16000,512,"NONE","NONE"))
                f.writeframes(struct.pack("h"*len(audio), *audio))

    def get_array_of_samples(self):
        return array.array(self.array_type, self._data)

