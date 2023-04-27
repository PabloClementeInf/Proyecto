from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QComboBox, QVBoxLayout, QWidget
from .audio import audio
from scipy.io import wavfile


class Interfaz(QMainWindow):
    archivo = []
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Aplicación de Conversión de Audio")
        
        
        # Configurar el botón para seleccionar archivo
        self.btn_agregar = QPushButton("Seleccionar Archivo", self)
        self.btn_agregar.clicked.connect(self.agregar_archivo)
        
        # Configurar los botones para procesar el audio
        self.btn_agudo = QPushButton("Agudo", self)
        self.btn_agudo.clicked.connect(self.procesar_audio_agudo)
        
        self.btn_grave = QPushButton("Grave", self)
        self.btn_grave.clicked.connect(self.procesar_audio_grave)
        
        self.btn_robot = QPushButton("Robot", self)
        self.btn_robot.clicked.connect(self.procesar_audio_robot)
        
        # Configurar el botón para exportar archivo
        
        
        # Configurar el layout
        layout = QVBoxLayout()
        layout.addWidget(self.btn_agregar)
        layout.addWidget(self.btn_agudo)
        layout.addWidget(self.btn_grave)
        layout.addWidget(self.btn_robot)
        
        
        # Configurar el widget central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        # inicializamos el archivos
        
    def agregar_archivo(self):
        opciones = QFileDialog.Options()
        opciones |= QFileDialog.DontUseNativeDialog
        archivo = QFileDialog.getOpenFileName(self, "Seleccionar Archivo", "", "Archivos de Audio (*.wav)", options=opciones)
        self.aud=audio.cargar_audio(archivo)
        if archivo:
            print("Archivos seleccionados: ",archivo)

    def procesar_audio_agudo(self):
        print("Procesando a audio agudo")
        audio.procesar_audio_agudo(self.aud)
    #wavfile.write('agudo.wav', 8000, salida.astype('int16'))

    def procesar_audio_grave(self):
        print("Procesando a audio grave")
        audio.procesar_audio_grave(self.aud)
    

    def procesar_audio_robot(self):
        print("Procesando a audio grave")
        audio.procesar_audio_robot(self.aud)
 
    



if __name__ == '__main__':
    app = QApplication([])
    interfaz = Interfaz()
    interfaz.show()
    app.exec_()
