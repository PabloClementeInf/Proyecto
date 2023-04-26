import os
from pydub import AudioSegment

class audio:
    def cargar_audio(nombre_archivo):
        ruta_archivo = os.path.join('data', nombre_archivo)
        return AudioSegment.from_file(ruta_archivo)


    def procesar_audio_agudo(audio):
        return audio.high_pass_filter(2000)


    def procesar_audio_grave(audio):
        return audio.low_pass_filter(200)


    def procesar_audio_robot(audio):
        return audio._spawn(audio.raw_data, overrides={'frame_rate': int(audio.frame_rate * 0.8)})


    def exportar_audio(audio, nombre_archivo):
        ruta_archivo = os.path.join('data', nombre_archivo)
        audio.export(ruta_archivo, format='wav')

