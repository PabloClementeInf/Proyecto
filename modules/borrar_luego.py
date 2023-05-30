
    """def procesar_audio_grave(audio):
        nuevo_rate = int(audio.frame_rate * 0.5)
        nuevoaudio = audio._spawn(audio.raw_data, overrides={'frame_rate':nuevo_rate})
        ruta="./data/audionuevo"
        nombre_salida = f"{ruta[:-4]}_grave.wav"
        nuevoaudio.export(nombre_salida, format="wav")
        

    def procesar_audio_grave(audio):
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

        """

         """
    def procesar_audio_grave(audio):
        octave_adjustment = 1.5  # Valor para controlar el efecto de robot
        audio = audio._spawn(audio.raw_data, overrides={
            "frame_rate": int(audio.frame_rate * (2.0 ** octave_adjustment))
        })
        # Aplicar un filtro de velocidad
        speed_factor = 1.2  # Factor de velocidad para el filtro
        audio = audio.speedup(playback_speed=speed_factor)

        ruta="./data/audionuevo"
        nombre_salida = f"{ruta[:-4]}_grave.wav"
        audio.export(nombre_salida, format="wav")
        """