import os
from pydub import AudioSegment
#from pydub.effects import robotize
class audio:
    
    #ruta="/Users/amade/Documents/GitHub/Proyecto/data/audionuevo"
    
    def cargar_audio(nombre_archivo):
        ruta_archivo = nombre_archivo
        return AudioSegment.from_file(ruta_archivo[0])


    def procesar_audio_agudo(audio):
        nuevo_rate = audio.frame_rate * 2
        nuevoaudio = audio._spawn(audio.raw_data, overrides={'frame_rate':nuevo_rate})
        ruta="/Users/amade/Documents/GitHub/Proyecto/data/audionuevo"
        nombre_salida = f"{ruta[:-4]}_agudo.wav"
        nuevoaudio.export(nombre_salida, format="wav")

    def procesar_audio_grave(audio):
        nuevo_rate = int(audio.frame_rate * 0.5)
        nuevoaudio = audio._spawn(audio.raw_data, overrides={'frame_rate':nuevo_rate})
        ruta="/Users/amade/Documents/GitHub/Proyecto/data/audionuevo"
        nombre_salida = f"{ruta[:-4]}_grave.wav"
        nuevoaudio.export(nombre_salida, format="wav")


    def procesar_audio_robot(audio):
        x=2
        #nuevoaudio= robotize(audio, 1)
        #ruta='C:\Users\amade\Documents\GitHub\Proyecto\data\audio_nuevo'
        #nombre_salida = f"{ruta[:-4]}_grave.wav"
        #nuevoaudio.export(nombre_salida, format="wav")




