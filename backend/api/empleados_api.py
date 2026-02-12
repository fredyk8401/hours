"""
API de Empleados
Maneja las peticiones HTTP al servidor para operaciones CRUD de empleados
"""
from backend.api.api_client import APIClient

class EmpleadosAPI:
    def __init__(self):
        self.client = APIClient()
    
    def get_all_empleados(self):
        """Obtiene la lista de todos los empleados"""
        return self.client._make_request('GET', '/empleados')
    
    def create_empleado(self, empleado_data):
        """
        Crea un nuevo empleado
        
        Args:
            empleado_data (dict): {
                'empleado_codigo': int,
                'empleado_nombres': str,
                'empleado_estado': str (default 'V')
            }
        """
        return self.client._make_request('POST', '/empleados', empleado_data)
    
    def update_empleado(self, empleado_id, empleado_data):
        """
        Actualiza un empleado existente
        
        Args:
            empleado_id (int): ID del empleado
            empleado_data (dict): {
                'empleado_nombres': str,
                'empleado_estado': str
            }
        """
        return self.client._make_request('PUT', f'/empleados/{empleado_id}', empleado_data)
    
    def check_codigo_exists(self, codigo):
        """Verifica si un código de empleado ya existe"""
        return self.client._make_request('GET', f'/empleados/check-codigo/{codigo}')