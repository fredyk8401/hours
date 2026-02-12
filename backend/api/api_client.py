"""
Cliente API para realizar peticiones HTTP al servidor backend
Este módulo se usa desde el frontend para comunicarse con el servidor
"""
import requests
from backend.config import Config

class APIClient:
    def __init__(self):
        self.base_url = Config.get_api_url()
        self.timeout = 10  # Timeout de 10 segundos
    
    def _make_request(self, method, endpoint, data=None, params=None):
        """
        Método interno para hacer peticiones HTTP
        
        Args:
            method (str): GET, POST, PUT, DELETE
            endpoint (str): Ruta del endpoint (ej: '/auth/login')
            data (dict): Datos para enviar en el body (POST, PUT)
            params (dict): Parámetros de query string (GET)
        
        Returns:
            dict: Respuesta del servidor
        """
        url = f"{self.base_url}{endpoint}"
        
        try:
            if method == 'GET':
                response = requests.get(url, params=params, timeout=self.timeout)
            elif method == 'POST':
                response = requests.post(url, json=data, timeout=self.timeout)
            elif method == 'PUT':
                response = requests.put(url, json=data, timeout=self.timeout)
            elif method == 'DELETE':
                response = requests.delete(url, timeout=self.timeout)
            else:
                return {"success": False, "message": "Método HTTP no válido"}
            
            # Intentar parsear JSON
            try:
                return response.json()
            except:
                return {
                    "success": False,
                    "message": "Error al procesar respuesta del servidor",
                    "status_code": response.status_code
                }
        
        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "message": "No se pudo conectar al servidor. Verifica que esté ejecutándose."
            }
        except requests.exceptions.Timeout:
            return {
                "success": False,
                "message": "La petición tardó demasiado. Intenta de nuevo."
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error inesperado: {str(e)}"
            }
    
    # ========================================================================
    # MÉTODOS DE AUTENTICACIÓN
    # ========================================================================
    
    def login(self, email, password):
        """
        Autentica un usuario
        
        Args:
            email (str): Email del usuario
            password (str): Contraseña
        
        Returns:
            dict: Respuesta con success, message y data
        """
        return self._make_request('POST', '/auth/login', {
            'email': email,
            'password': password
        })
    
    # ========================================================================
    # MÉTODOS DE PRUEBA
    # ========================================================================
    
    def health_check(self):
        """Verifica que el servidor esté funcionando"""
        return self._make_request('GET', '/health')
    
    def test_database(self):
        """Prueba la conexión a la base de datos"""
        return self._make_request('GET', '/test-db')
    
    # ========================================================================
    # MÉTODOS PARA FUTUROS MÓDULOS (Preparados)
    # ========================================================================
    
    # Ejemplo de estructura para futuros métodos:
    
    # def get_empleados(self):
    #     """Obtiene lista de empleados"""
    #     return self._make_request('GET', '/empleados')
    #
    # def create_empleado(self, data):
    #     """Crea un nuevo empleado"""
    #     return self._make_request('POST', '/empleados', data)
    #
    # def update_empleado(self, id, data):
    #     """Actualiza un empleado existente"""
    #     return self._make_request('PUT', f'/empleados/{id}', data)
    #
    # def delete_empleado(self, id):
    #     """Elimina un empleado"""
    #     return self._make_request('DELETE', f'/empleados/{id}')