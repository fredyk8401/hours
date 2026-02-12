"""
API de Autenticación
Este módulo usa el APIClient para hacer peticiones al servidor backend
"""
from backend.api.api_client import APIClient

class AuthAPI:
    def __init__(self):
        self.client = APIClient()
    
    def authenticate_user(self, email, password):
        """
        Autentica un usuario haciendo una petición al servidor backend
        
        Args:
            email (str): Email del usuario
            password (str): Contraseña del usuario
        
        Returns:
            dict: Respuesta del servidor con success, message y data
        """
        return self.client.login(email, password)