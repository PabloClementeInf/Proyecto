from modules.gui import Interfaz

def main():
    # Crear instancia de la aplicación
    app = QApplication([])
    
    # Crear instancia de la interfaz
    interfaz = Interfaz()
    
    # Ejecutar la aplicación
    app.exec_()
