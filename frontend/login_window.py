import re
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                               QLabel, QLineEdit, QPushButton, QMessageBox)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon
from frontend.styles import AppStyles
from backend.api.auth_api import AuthAPI

class LoginWindow(QMainWindow):
    login_successful = Signal(dict)  # Signal para notificar login exitoso
    
    def __init__(self):
        super().__init__()
        self.auth_api = AuthAPI()
        self.init_ui()
    
    def init_ui(self):
        """Inicializa la interfaz de usuario"""
        self.setWindowTitle("Sistema de Registro de Horas - Login")
        self.setFixedSize(500, 450)
        self.setStyleSheet(AppStyles.WINDOW_STYLE)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QVBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(40, 30, 40, 30)
        
        # Título
        title = QLabel("SISTEMA DE REGISTRO DE HORAS")
        title.setStyleSheet(AppStyles.TITLE_STYLE)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)
        
        # Subtítulo
        subtitle = QLabel("Autenticación de Usuario")
        subtitle.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                font-size: 16px;
                padding: 10px;
            }
        """)
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(subtitle)
        
        # Espaciador
        main_layout.addSpacing(10)
        
        # Contenedor para el formulario
        form_layout = QVBoxLayout()
        form_layout.setSpacing(15)
        
        # Campo Email
        email_label = QLabel("Email:")
        email_label.setStyleSheet(AppStyles.LABEL_STYLE)
        form_layout.addWidget(email_label)
        
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("usuario@ejemplo.com")
        self.email_input.setStyleSheet(AppStyles.INPUT_STYLE)
        self.email_input.setMaxLength(40)
        self.email_input.setFocus()  # Establecer foco inicial
        form_layout.addWidget(self.email_input)
        
        # Campo Password
        password_label = QLabel("Contraseña:")
        password_label.setStyleSheet(AppStyles.LABEL_STYLE)
        form_layout.addWidget(password_label)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Mínimo 8 caracteres")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet(AppStyles.INPUT_STYLE)
        self.password_input.setMaxLength(15)
        form_layout.addWidget(self.password_input)
        
        # Label para mensajes de error
        self.error_label = QLabel("")
        self.error_label.setStyleSheet(AppStyles.ERROR_LABEL_STYLE)
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.error_label.setWordWrap(True)
        self.error_label.setMinimumHeight(40)
        form_layout.addWidget(self.error_label)
        
        main_layout.addLayout(form_layout)
        
        # Espaciador
        main_layout.addSpacing(10)
        
        # Botón de login
        login_btn = QPushButton("INGRESAR")
        login_btn.setStyleSheet(AppStyles.BUTTON_STYLE)
        login_btn.clicked.connect(self.handle_login)
        login_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        login_btn.setMinimumHeight(45)
        main_layout.addWidget(login_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Conectar Enter key al login
        self.email_input.returnPressed.connect(self.handle_login)
        self.password_input.returnPressed.connect(self.handle_login)
        
        # Establecer tab order correcto
        self.setTabOrder(self.email_input, self.password_input)
        self.setTabOrder(self.password_input, login_btn)
    
    def showEvent(self, event):
        """Evento cuando se muestra la ventana"""
        super().showEvent(event)
        # Asegurar que el campo email tenga el foco
        self.email_input.setFocus()
        self.email_input.activateWindow()
    
    def validate_email(self, email):
        """Valida formato de email"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_password(self, password):
        """
        Valida que la contraseña tenga:
        - Mínimo 8 caracteres
        - Al menos una letra mayúscula
        - Al menos un número
        """
        if len(password) < 8:
            return False, "La contraseña debe tener al menos 8 caracteres"
        
        if not re.search(r'[A-Z]', password):
            return False, "La contraseña debe tener al menos una letra mayúscula"
        
        if not re.search(r'\d', password):
            return False, "La contraseña debe tener al menos un número"
        
        return True, ""
    
    def handle_login(self):
        """Maneja el proceso de autenticación"""
        email = self.email_input.text().strip()
        password = self.password_input.text()
        
        # Limpiar mensaje de error previo
        self.error_label.setText("")
        
        # Validar email
        if not email:
            self.error_label.setText("Por favor ingrese su email")
            self.email_input.setFocus()
            return
        
        if not self.validate_email(email):
            self.error_label.setText("Formato de email inválido")
            self.email_input.setFocus()
            return
        
        # Validar password
        if not password:
            self.error_label.setText("Por favor ingrese su contraseña")
            self.password_input.setFocus()
            return
        
        is_valid, message = self.validate_password(password)
        if not is_valid:
            self.error_label.setText(message)
            self.password_input.setFocus()
            return
        
        # Intentar autenticar
        try:
            result = self.auth_api.authenticate_user(email, password)
            
            if result["success"]:
                # Login exitoso
                self.login_successful.emit(result["data"])
                self.close()
            else:
                # Login fallido
                self.error_label.setText(result["message"])
                self.password_input.clear()
                self.password_input.setFocus()
        except Exception as e:
            self.error_label.setText(f"Error de conexión: {str(e)}")