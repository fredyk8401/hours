"""
Sistema de Registro de Horas BRAMIL
Aplicación principal
"""
import sys
import os

# IMPORTANTE: Configurar ANTES de importar QApplication
# Esto soluciona problemas de renderizado de fuentes en Windows
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
os.environ["QT_SCALE_FACTOR"] = "1"

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from frontend.login_window import LoginWindow
from frontend.main_window import MainWindow

class Application:
    def __init__(self):
        # Habilitar High DPI antes de crear la aplicación
        QApplication.setHighDpiScaleFactorRoundingPolicy(
            Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
        )
        
        self.app = QApplication(sys.argv)
        self.app.setApplicationName("Sistema de Registro de Horas BRAMIL")
        
        # Establecer fuente por defecto para toda la aplicación
        default_font = QFont("Segoe UI", 10)
        default_font.setStyleStrategy(QFont.PreferAntialias)
        self.app.setFont(default_font)
        
        self.login_window = None
        self.main_window = None
    
    def show_login(self):
        """Muestra la ventana de login"""
        self.login_window = LoginWindow()
        self.login_window.login_successful.connect(self.on_login_success)
        self.login_window.show()
    
    def on_login_success(self, user_data):
        """Maneja el login exitoso y muestra la ventana principal"""
        self.main_window = MainWindow(user_data)
        self.main_window.show()
    
    def run(self):
        """Ejecuta la aplicación"""
        self.show_login()
        return self.app.exec()

if __name__ == "__main__":
    app = Application()
    sys.exit(app.run())