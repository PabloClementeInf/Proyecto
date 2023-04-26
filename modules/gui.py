from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QComboBox, QVBoxLayout, QWidget
from .audio import audio
from scipy.io import wavfile


class Interfaz(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Aplicación de Conversión de Audio")
        
        
        # Configurar el botón para agregar archivos
        self.btn_agregar = QPushButton("Agregar Archivos", self)
        self.btn_agregar.clicked.connect(self.agregar_archivos)
        
        # Configurar los botones para procesar el audio
        self.btn_agudo = QPushButton("Agudo", self)
        self.btn_agudo.clicked.connect(self.procesar_audio_agudo)
        
        self.btn_grave = QPushButton("Grave", self)
        self.btn_grave.clicked.connect(self.procesar_audio_grave)
        
        self.btn_robot = QPushButton("Robot", self)
        self.btn_robot.clicked.connect(self.procesar_audio_robot)
        
        # Configurar el botón para exportar archivos
        self.btn_exportar = QPushButton("Exportar Archivos", self)
        self.btn_exportar.clicked.connect(self.exportar_archivos)
        
        # Configurar el layout
        layout = QVBoxLayout()
        layout.addWidget(self.btn_agregar)
        layout.addWidget(self.btn_agudo)
        layout.addWidget(self.btn_grave)
        layout.addWidget(self.btn_robot)
        layout.addWidget(self.btn_exportar)
        
        # Configurar el widget central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        # Configurar la lista de archivos
        self.archivos = []
    
    def agregar_archivos(self):
        opciones = QFileDialog.Options()
        opciones |= QFileDialog.DontUseNativeDialog
        archivos, _ = QFileDialog.getOpenFileNames(self, "Seleccionar Archivos", "", "Archivos de Audio (*.wav)", options=opciones)
        if archivos:
            self.archivos += archivos
            print(f"Archivos seleccionados: {self.archivos}")

    def procesar_audio_agudo(self):
        print
        for archivo in self.archivos:
            salida=audio.procesar_audio_agudo(archivo)
        wavfile.write('agudo.wav', 8000, salida.astype('int16'))

    def procesar_audio_grave(self):
        for archivo in self.archivos:
            salida=audio.procesar_audio_grave(archivo)
        wavfile.write('grave.wav', 8000, salida.astype('int16'))

    def procesar_audio_robot(self):
        for archivo in self.archivos:
            salida=audio.procesar_audio_robot(archivo)
        wavfile.write('Robot.wav', 8000, salida.astype('int16'))
    
    def exportar_archivos(self):
        for archivo in self.archivos:
            print(f"Exportando archivo: {archivo}")


if __name__ == '__main__':
    app = QApplication([])
    interfaz = Interfaz()
    interfaz.show()
    app.exec_()
