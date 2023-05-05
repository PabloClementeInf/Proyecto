import os
from pydub import AudioSegment
from pvrecorder import PvRecorder
import wave, struct
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

    def procesar_audio_grave(audio):
        nuevo_rate = int(audio.frame_rate * 0.5)
        nuevoaudio = audio._spawn(audio.raw_data, overrides={'frame_rate':nuevo_rate})
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



