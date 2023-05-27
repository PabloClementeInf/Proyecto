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

    """def procesar_audio_grave(audio):
        nuevo_rate = int(audio.frame_rate * 0.5)
        nuevoaudio = audio._spawn(audio.raw_data, overrides={'frame_rate':nuevo_rate})
        ruta="./data/audionuevo"
        nombre_salida = f"{ruta[:-4]}_grave.wav"
        nuevoaudio.export(nombre_salida, format="wav")
        """
    """
    def procesar_audio_grave(audio):
        #Cargamos el filtro de cueva
        filter = AudioSegment.from_file("./filter/Cave.wav")
        #Transformamos de AudioSegment a array numpy
        filter = np.array(filter.get_array_of_samples())

        #Normalizamos el sonido
        filter = filter.astype(np.float64) / np.max(np.abs(filter))
        fr =audio.frame_rate
        #Transformamos el audio a un array numpy
        audio = np.array(audio.get_array_of_samples())
        #Utilizamos convolve para añadir el efecto al audio
        audio = signal.convolve(filter, audio)
        #Normalizamos de nuevo el audio
        audio = audio.astype(np.float64) / np.max(np.abs(audio))
        #Transformamos de np.array a AudioSegment
        wavfile.write("./data/auxiliar.wav",fr, audio)
        fr,audio = wavfile.read("./data/auxiliar.wav")
        
        sound = AudioSegment(
            data = audio.astype(np.float32).tobytes(),
            frame_rate=fr,
            sample_width=4, 
            channels=1
        )
        nuevoaudio = sound._spawn(sound.raw_data)
        ruta="./data/audionuevo"
        nombre_salida = f"{ruta[:-4]}_grave.wav"
        nuevoaudio.export(nombre_salida, format="wav")
        """
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

