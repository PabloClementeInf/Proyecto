from cmath import log
import os
from pydub import AudioSegment
import numpy as np
from pvrecorder import PvRecorder
from scipy import signal
import wave, struct
from scipy.io import wavfile
import time

class audio:
    

    #ruta="/Users/amade/Documents/GitHub/Proyecto/data/audionuevo"
    
    def cargar_audio(nombre_archivo):
        ruta_archivo = nombre_archivo
        return AudioSegment.from_file(ruta_archivo[0])


    def procesar_audio_agudo(audio):
        nuevo_rate = audio.frame_rate * 2
        nuevoaudio = audio._spawn(audio.raw_data, overrides={'frame_rate':nuevo_rate})
        ruta="./data/audionuevo"
        nombre_salida = f"{ruta[:-4]}_agudo.wav"
        nuevoaudio.export(nombre_salida, format="wav")
    
    def procesar_audio_radio(audio):
        audio1 = AudioSegment.from_wav(audio)

        # Cargar el audio de ruido de fondo de radio
        audio_radio = "radio.wav"
        radio = AudioSegment.from_wav(audio_radio)
        
        # Ajustar la duración del ruido de fondo al mismo que el audio original
        radio = radio[:len(audio1)]
        
        # Ajustar el volumen del ruido de fondo
        ajuste = 10
        radio = radio - ajuste  # Ajustar el rango del volumen aquí
        
        # Mezclar el audio original con el ruido de fondo
        mixed_audio = audio1.overlay(radio)
        
        # Exportar el resultado a un nuevo archivo de audio
        nuevo_audio = "audion_radio.wav"
        mixed_audio.export(nuevo_audio, format="wav")
    
    
    def procesar_audio_grave(audio):
        #Cargamos el filtro de cueva
        filter = AudioSegment.from_file("./filter/Cave.wav")
        #Transformamos de AudioSegment a array numpy
        filter1 = np.array(filter.get_array_of_samples())
        #Normalizamos el sonido
        filter_norm = filter1 / np.max(np.abs(filter1))

        #Transformamos el audio a un array numpy
        audio1 = np.array(audio.get_array_of_samples())

        #Utilizamos convolve para a�adir el efecto al audio
        audio1_conv = signal.convolve(filter_norm, audio1)

        #Normalizamos de nuevo el audio
        audio1_conv = audio1_conv/ np.max(np.abs(audio1_conv))

        #Transformamos de np.array a AudioSegment
        wavfile.write("./data/auxiliar.wav",audio.frame_rate, audio1_conv)

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
        nombre_salida = f"{ruta[:-4]}_grave.wav"
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

