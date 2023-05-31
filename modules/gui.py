from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QComboBox, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QVBoxLayout, QGridLayout, QWidget, QLabel, QFrame, QSizePolicy, QComboBox
from PyQt5.QtCore import Qt
from audio import audio
from scipy.io import wavfile
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QPixmap,QPalette, QFont, QColor
from skimage import io

class Interfaz(QMainWindow):
    archivo = []
    
    
    def __init__(self):
        super().__init__()

        imagen = QPixmap('.Proyecto/images/play.png')
        label = QLabel()
        label.setPixmap(imagen)
        label.show()

         # Título  y tamaño de la ventana
        self.setWindowTitle("Aplicación de Procesamiento de Audio")
        self.resize(400,300)
        # Crear el layout principal
        layout = QGridLayout()

        #Cambiar el color de fondo de la ventana a azul apagado
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(23, 104, 172))
        self.setPalette(palette)
        
        # Configurar el panel norte
        panel_norte = QWidget()
        layout_norte = QVBoxLayout(panel_norte)
        layout_norte.setAlignment(Qt.AlignTop)

        # Configurar el título de bienvenida
        titulo_label = QLabel("Bienvenido a Project Audio")
        titulo_label.setAlignment(Qt.AlignCenter)
        titulo_label.setStyleSheet("font-size: 18px; font-weight: bold; color: white;")
        layout_norte.addWidget(titulo_label)

        # Configurar la la Línea divisora
        linea_divisora = QFrame()
        linea_divisora.setFrameShape(QFrame.HLine)
        linea_divisora.setFrameShadow(QFrame.Sunken)
        layout_norte.addWidget(linea_divisora)
        
        # Configurar el panel sur
        panel_sur = QWidget()
        layout_sur = QGridLayout(panel_sur)
        layout_sur.setContentsMargins(0, 0, 0, 0)
        
        # Configurar el botón para seleccionar archivo
        self.btn_agregar = QPushButton("Seleccionar Archivo", self)
        self.btn_agregar.clicked.connect(self.agregar_archivo)
        layout_sur.addWidget(self.btn_agregar,1,0)
        
        # Configurar los botones para procesar el audio
        combo_box = QComboBox()
        combo_box.addItem("Grave")
        combo_box.addItem("Agudo")
        combo_box.addItem("Alien")
        combo_box.addItem("Robot")
        combo_box.addItem("Cueva")
        combo_box.addItem("Radio")

        combo_box.activated.connect(self.procesar_audio)
        layout_sur.addWidget(combo_box,2,0,1,2)

        self.btn_grabar = QPushButton("Grabar audio", self)
        self.btn_grabar.clicked.connect(self.grabar_audio)
        layout_sur.addWidget(self.btn_grabar,1,1)

        
        # # Configurar el botón para reproducir el audio
        self.btn_reproducir = QPushButton("Reproducir", self)
        self.btn_reproducir.clicked.connect(self.reproducir_audio)
        layout_sur.addWidget(self.btn_reproducir,3,0,1,2)
        
        # Establecer estilos y colores
        self.setStyleSheet("""
            QMainWindow {
                background-color: #B6C2D9;
            }
            QPushButton {
                background-color: #B6C2D9;
                color: black;
                padding: 10px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
            }
            QComboBox {
                background-color: #B6C2D9;
                color: black;
                padding: 10px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #A0AABB;
                
            }
            QComboBox:hover {
                background-color: #A0AABB;
                
            }
        """) 
       
        #Añadimos los layouts secundarios al principal
        layout.addWidget(panel_norte, 0, 0)
        layout.addWidget(panel_sur, 1, 0)
        
        tripleta = (36, 95, 144)

        # Cambiar el fondo del panel norte a color azul claro
        panel_norte.setAutoFillBackground(True)
        panel_norte_palette = panel_norte.palette()
        panel_norte_palette.setColor(QPalette.Background, QColor(*tripleta))
        panel_norte.setPalette(panel_norte_palette)
        panel_norte.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)


        # Cambiar el fondo del panel sur a color azul claro
        panel_sur.setAutoFillBackground(True)
        panel_sur_palette = panel_sur.palette()
        panel_sur_palette.setColor(QPalette.Background, QColor(*tripleta))
        panel_sur.setPalette(panel_sur_palette)

        # Configurar el widget central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        central_widget.setAutoFillBackground(True)
        central_widget_palette = central_widget.palette()
        central_widget_palette.setColor(QPalette.Background, QColor(*tripleta))
        central_widget.setPalette(central_widget_palette)
        self.setCentralWidget(central_widget)
  
        #
        self.playerMedia = QMediaPlayer(self)

    def procesar_audio(self, index):
        opciones = {
            0: self.procesar_audio_grave,
            1: self.procesar_audio_agudo,
            2: self.procesar_audio_cueva,
            3: self.procesar_audio_alien,
            4: self.procesar_audio_robot,
            5: self.procesar_audio_radio
        }
        # Obtener la función correspondiente al índice seleccionado
        funcion = opciones.get(index)
        # Ejecutar la función si existe
        if funcion:
            funcion()
            
    def agregar_archivo(self):
        opciones = QFileDialog.Options()
        opciones |= QFileDialog.DontUseNativeDialog
        archivo = QFileDialog.getOpenFileName(self, "Seleccionar Archivo", "", "Archivos de Audio (*.wav)", options=opciones)
        self.aud=audio.cargar_audio(archivo)
        if archivo:
            print("Archivos seleccionados: ",archivo)

    def grabar_audio(self):
        print("Grabando audio")
        audio.grabar_audio()

    def procesar_audio_grave(self):
        print("Procesando audio grave")
        # Lógica para procesar audio grave

    def procesar_audio_agudo(self):
        print("Procesando audio agudo")
        # Lógica para procesar audio agudo

    def procesar_audio_cueva(self):
        print("Procesando audio de la cueva")
        # Lógica para procesar audio de la cueva

    def procesar_audio_alien(self):
        print("Procesando audio alienígena")
        # Lógica para procesar audio alienígena

    def procesar_audio_robot(self):
        print("Procesando audio de robot")
        # Lógica para procesar audio de robot

    def procesar_audio_radio(self):
        print("Procesando audio de la radio")
        # Lógica para procesar audio de la radio

    
           
    def reproducir_audio(self):
        opciones = QFileDialog.Options()
        opciones |= QFileDialog.DontUseNativeDialog
        archivo = QFileDialog.getOpenFileName(self, "Seleccionar Archivo que deseas reproducir", "", "Archivos de Audio (*.wav)", options=opciones)
        contenido = QMediaContent(QUrl.fromLocalFile(archivo[0]))
        player=self.playerMedia
        player.setMedia(contenido)
        player.play()


if __name__ == '__main__':
    app = QApplication([])
    interfaz = Interfaz()
    interfaz.show()
    app.exec_()
