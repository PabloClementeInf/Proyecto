import os
from pydub import AudioSegment
#from pydub.effects import robotize
class audio:
    
    #ruta="/Users/amadorcarmonamendez/Desktop/ProyectoPDS/Proyecto/data/audionuevo"
    
    def cargar_audio(nombre_archivo):
        ruta_archivo = nombre_archivo
        return AudioSegment.from_file(ruta_archivo[0])


    def procesar_audio_agudo(audio):
        nuevoaudio=audio+100
        ruta="/Users/amadorcarmonamendez/Desktop/ProyectoPDS/Proyecto/data/audionuevo"
        nombre_salida = f"{ruta[:-4]}_agudo.wav"
        nuevoaudio.export(nombre_salida, format="wav")

    def procesar_audio_grave(audio):
        nuevoaudio=audio+3
        ruta="/Users/amadorcarmonamendez/Desktop/ProyectoPDS/Proyecto/data/audionuevo"
        nombre_salida = f"{ruta[:-4]}_grave.wav"
        nuevoaudio.export(nombre_salida, format="wav")


    def procesar_audio_robot(audio):
        x=2
        #nuevoaudio= robotize(audio, 1)
        #ruta="/Users/amadorcarmonamendez/Desktop/ProyectoPDS/Proyecto/data/audionuevo"
        #nombre_salida = f"{ruta[:-4]}_grave.wav"
        #nuevoaudio.export(nombre_salida, format="wav")




