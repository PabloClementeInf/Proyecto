# Proyecto de teoria de PDS 
## Procesador de audio
##### Autores:  Manuel Medina Martín, Pablo Clemente Infantes, Amador Carmona Méndez y Amadeo Martínez Sánchez
### Requisitos para poder ejecutar nuestro proyecto:
Instalar con pip install PyQT, pydub y scipy con los siguientes comandos:
~~~bash
$pip install PyQT5
$pip install pydub
$pip install scipy
~~~
Documentacion de pydub: https://github.com/jiaaro/pydub 

Documentacion de PyQT: https://doc.qt.io/qtforpython-6/

Documentacion de scipy: https://docs.scipy.org/doc/scipy/

### Ejecucion de nuestro proyecto:
Para ejecutar nuestro proyecto ejecutar hay que ejecutar el main con el comando:
~~~bash
$python main.py
~~~
### Estructuración y archivos del proyecto:

proyecto: carpeta principal del proyecto en la que encontramos los siquientes archivos y/o carpetas:
- main.py: archivo principal del proyecto en el que se ejecuta la interfaz. 
- modules: carpeta en la que tenemos los diferentes modulos donde implementamos la interfaz y todas las funcionalidades del proyecto.
- --init.py: para que python interprete que la carpeta modules es un paquete/libreria.
- --gui.py: interfaz del proyecto donde tambien implementamos alguna funcionalidad como el reproductor de audios gracias al paquete PyQT.
- --audio.py: donde tenemos las funcionalidades del proyecto relacionadas con el tratamiento de audios como son los filtros.
- data: carpeta con todos los audios con los que se trabaje y donde se extraeran los resultados.

### Filtros y funcionalidades:

#### Filtro agudo y Grave

En estos filtros modificamos el tono de nuestra señal de entrada, para ello utilizamos la la función pitch_shift() de la biblioteca librosa , Cambiar el tono de una señal implica modificar su frecuencia fundamental. Esta función aplica un desplazamiento en la frecuencia de la señal de audio original para lograr el cambio de tono deseado. Los parámetros utilizados en la función son los siguientes:

y: La forma de onda de audio original.

sr: La tasa de muestreo de la señal de audio original.

n_steps: El número de pasos de semitono que se desea cambiar el tono. Un paso de semitono es la mínima diferencia de altura entre dos notas en una escala musical.

Un valor positivo de n_steps(argumento de la función) aumentará el tono (más agudo), mientras que un valor negativo lo disminuirá (más grave).

#### Filtro Robot

En este filtro obtenemos las frecuencias fundamentales o tonos presentes en el audio con la funcion piptrack() de la libreria librosa.Despues ajustamos las frecuencias fundamentales a un valor objetivo de tono de 11.0. Se multiplica cada frecuencia fundamental por el cociente entre target_pitch y la media de pitches. Esto produce un ajuste en las frecuencias para lograr el tono deseado.
PDespues calculamos la diferencia de tono entre las frecuencias originales y las frecuencias ajustadas y restamos la mediana de pitches a la media de pitches para obtener pitch_diff, que representa la diferencia de tono para cada frame de la señal de audio. Para aplicar el cambio de tono al audio original,vamos frame por frame cada frame se basa en la longitud de pitch_diff.
Por ultimo utilizamos la función librosa.effects.pitch_shift() para aplicar el cambio de tono a cada frame según el valor correspondiente de pitch_diff. Por ultimo realizamos un ajuste en la escala de amplitud del audio. La señal se multiplica por (2 ** 31 - 1) para escalarla en el rango que queremos.

#### Filtro Cueva

En este filtro como hemos visto en una de las practicas aplicamos al audio de entrada con la función signal.convolve() de scipy, para convulcionarlo con un audio de cueva.

#### Filtro Radio

En este filtro lo que hacemos es crear ruido de fondo en nuestro audio de entrada para ello mezclamos la señal de audio original y una señal nueva creada con la duración de el audio de entrada del ruido de fondo. Esto superpone el ruido de fondo al audio original.
Despues ecualizamos el audio multiplicándolo por un factor específico (10 ** (-10 / 20)). Esto ajusta los niveles de amplitud en relación con una referencia y puede tener un efecto de realce o atenuación en diferentes frecuencias.
Por ultimo normalizamos el audio para evitar distorsiones dividiendo cada elemento por el valor máximo absoluto de todos los elementos del arreglo. Esto asegura que la amplitud del audio esté en el rango adecuado.

#### Filtro Alien

En este filtro creamos una señal portadora utilizando la función np.sin(). Esta señal portadora es una onda sinusoidal con una frecuencia de 1500 Hz y una duración basada en el tiempo de la señal de audio de entrada. La frecuencia de la señal portadora puede ajustarse según se desee para obtener diferentes efectos de sonido.
Tras esto modificamos la señal de audio y multiplicándola por dos veces la señal portadora. Esto modula la señal de audio original con la señal portadora, lo que produce un efecto de modulación de amplitud (AM). La multiplicación de las señales mezcla las características de la señal de audio original con las características de la señal portadora, lo que genera el efecto de sonido alienígena
