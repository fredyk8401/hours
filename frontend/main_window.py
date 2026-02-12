from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QPushButton, QGridLayout, QMessageBox)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from frontend.styles import AppStyles

class MainWindow(QMainWindow):
    def __init__(self, user_data):
        super().__init__()
        self.user_data = user_data
        self.init_ui()
    
    def init_ui(self):
        """Inicializa la interfaz principal"""
        self.setWindowTitle("Sistema de Registro de Horas BRAMIL")
        self.setMinimumSize(1000, 700)
        self.setStyleSheet(AppStyles.WINDOW_STYLE)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(30)
        main_layout.setContentsMargins(40, 30, 40, 30)
        
        # Banner de bienvenida
        self.create_welcome_banner(main_layout)
        
        # Menú de opciones
        self.create_menu_buttons(main_layout)
        
        # Espaciador para empujar contenido hacia arriba
        main_layout.addStretch()
    
    def create_welcome_banner(self, parent_layout):
        """Crea el banner de bienvenida"""
        banner_layout = QVBoxLayout()
        banner_layout.setSpacing(10)
        
        # Título principal
        title = QLabel("BIENVENIDO AL SISTEMA REGISTRO DE HORAS BRAMIL")
        title.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                font-size: 28px;
                font-weight: bold;
                padding: 20px;
                background-color: rgba(255, 140, 0, 0.3);
                border-radius: 10px;
            }
        """)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        banner_layout.addWidget(title)
        
        # Información del usuario
        user_info = QLabel(f"Usuario: {self.user_data['email']}")
        user_info.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                font-size: 14px;
                padding: 10px;
            }
        """)
        user_info.setAlignment(Qt.AlignmentFlag.AlignRight)
        banner_layout.addWidget(user_info)
        
        parent_layout.addLayout(banner_layout)
    
    def create_menu_buttons(self, parent_layout):
        """Crea los botones del menú principal en 2 filas"""
        # Contenedor para los botones
        buttons_container = QWidget()
        grid_layout = QGridLayout(buttons_container)
        grid_layout.setSpacing(20)
        grid_layout.setContentsMargins(0, 20, 0, 0)
        
        # Definir botones (preparados para iconos)
        # NOTA: Para agregar iconos, descomenta y ajusta las rutas:
        # QIcon("resources/icons/registro.png")
        
        buttons_config = [
            # Fila 1
            ("Registro de Horas", self.open_registro_horas, 0, 0),
            ("Mantenimiento de Empleados", self.open_mantenimiento, 0, 1),
            ("Reportes", self.open_reportes, 0, 2),
            # Fila 2
            ("Cierres del Mes", self.open_cierres, 1, 0),
            ("Opción 5", self.open_opcion5, 1, 1),
            ("Opción 6", self.open_opcion6, 1, 2),
        ]
        
        # Crear y posicionar botones
        for text, handler, row, col in buttons_config:
            btn = QPushButton(text)
            btn.setStyleSheet(AppStyles.MENU_BUTTON_STYLE)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(handler)
            
            # Preparado para iconos:
            # btn.setIcon(QIcon("resources/icons/nombre_icono.png"))
            # btn.setIconSize(QSize(40, 40))
            
            grid_layout.addWidget(btn, row, col)
        
        parent_layout.addWidget(buttons_container)
    
    # Métodos para manejar cada opción del menú
    # Estos métodos están listos para conectarse con los módulos futuros
    
    def open_registro_horas(self):
        """Abre el módulo de Registro de Horas"""
        from frontend.asistencias_window import AsistenciasWindow
        self.asistencias_window = AsistenciasWindow(self.user_data['email'])
        self.asistencias_window.show()
    
    def open_mantenimiento(self):
        """Abre el módulo de Mantenimiento de Empleados"""
        from frontend.empleados_window import EmpleadosWindow
        self.empleados_window = EmpleadosWindow()
        self.empleados_window.show()
    
    def open_reportes(self):
        """Abre el módulo de Reportes"""
        QMessageBox.information(
            self,
            "Reportes",
            "Módulo en desarrollo.\nEste abrirá la ventana de reportes."
        )
        # TODO: Implementar apertura del módulo
    
    def open_cierres(self):
        """Abre el módulo de Cierres del Mes"""
        from frontend.cierres_window import CierresWindow
        self.cierres_window = CierresWindow(self.user_data['email'])
        self.cierres_window.show()
    
    def open_opcion5(self):
        """Abre la Opción 5 (pendiente de definir)"""
        QMessageBox.information(
            self,
            "Opción 5",
            "Módulo pendiente de definir."
        )
    
    def open_opcion6(self):
        """Abre la Opción 6 (pendiente de definir)"""
        QMessageBox.information(
            self,
            "Opción 6",
            "Módulo pendiente de definir."
        )