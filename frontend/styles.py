# Estilos centralizados para toda la aplicación

class AppStyles:
    # Colores principales
    BACKGROUND_COLOR = "#4682B4"  # Azul acero
    BUTTON_COLOR = "#FF8C00"      # Naranja oscuro para botones
    BUTTON_HOVER = "#FFA500"      # Naranja más claro al pasar el mouse
    TEXT_COLOR = "#FFFFFF"        # Blanco para texto
    INPUT_BG = "#F0F8FF"          # Azul Alice para inputs
    INPUT_TEXT = "#000000"        # Negro para texto de inputs
    ERROR_COLOR = "#FF6B6B"       # Rojo para errores
    SUCCESS_COLOR = "#51CF66"     # Verde para éxito
    
    # Estilos para ventanas principales
    WINDOW_STYLE = f"""
        QMainWindow {{
            background-color: {BACKGROUND_COLOR};
        }}
        QWidget {{
            font-family: 'Segoe UI', Arial, sans-serif;
        }}
    """
    
    # Estilos para botones
    BUTTON_STYLE = f"""
        QPushButton {{
            background-color: {BUTTON_COLOR};
            color: {TEXT_COLOR};
            border: none;
            border-radius: 8px;
            padding: 12px 24px;
            font-size: 14px;
            font-weight: bold;
            min-width: 120px;
        }}
        QPushButton:hover {{
            background-color: {BUTTON_HOVER};
        }}
        QPushButton:pressed {{
            background-color: #FF7F00;
        }}
    """
    
    # Estilos para campos de entrada
    INPUT_STYLE = f"""
        QLineEdit {{
            background-color: {INPUT_BG};
            color: {INPUT_TEXT};
            border: 2px solid #B0C4DE;
            border-radius: 6px;
            padding: 10px 12px;
            font-size: 14px;
            min-height: 30px;
            selection-background-color: {BUTTON_COLOR};
            selection-color: {TEXT_COLOR};
        }}
        QLineEdit:focus {{
            border: 2px solid {BUTTON_COLOR};
            background-color: #FFFFFF;
        }}
        QLineEdit::placeholder {{
            color: #999999;
        }}
    """
    
    # Estilos para etiquetas
    LABEL_STYLE = f"""
        QLabel {{
            color: {TEXT_COLOR};
            font-size: 13px;
            font-weight: bold;
        }}
    """
    
    # Estilos para títulos
    TITLE_STYLE = f"""
        QLabel {{
            color: {TEXT_COLOR};
            font-size: 24px;
            font-weight: bold;
            padding: 20px;
        }}
    """
    
    # Estilos para mensajes de error
    ERROR_LABEL_STYLE = f"""
        QLabel {{
            color: {ERROR_COLOR};
            font-size: 12px;
            font-weight: bold;
            padding: 5px;
        }}
    """
    
    # Estilos para botones de menú principal (más grandes)
    MENU_BUTTON_STYLE = f"""
        QPushButton {{
            background-color: {BUTTON_COLOR};
            color: {TEXT_COLOR};
            border: 2px solid #FFA500;
            border-radius: 10px;
            padding: 20px;
            font-size: 15px;
            font-weight: bold;
            min-width: 200px;
            min-height: 80px;
        }}
        QPushButton:hover {{
            background-color: {BUTTON_HOVER};
            border: 2px solid #FFD700;
        }}
        QPushButton:pressed {{
            background-color: #FF7F00;
        }}
    """