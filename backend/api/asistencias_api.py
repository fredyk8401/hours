"""
API de Asistencias
Maneja las peticiones HTTP al servidor para operaciones de asistencias
"""
from backend.api.api_client import APIClient

class AsistenciasAPI:
    def __init__(self):
        self.client = APIClient()
    
    def get_asistencias_mes(self, mes, anio):
        """
        Obtiene las asistencias de un mes específico
        
        Args:
            mes (int): Mes (1-12)
            anio (int): Año (ej: 2024)
        
        Returns:
            dict: {
                "success": True,
                "data": {
                    "empleados": [...],
                    "asistencias": [...]
                }
            }
        """
        return self.client._make_request('GET', f'/asistencias/{anio}/{mes}')
    
    def registrar_asistencia(self, empleado_codigo, fecha, estado, autorizado_email):
        """
        Registra o actualiza una asistencia
        
        Args:
            empleado_codigo (int): Código del empleado
            fecha (str): Fecha en formato 'YYYY-MM-DD'
            estado (str): 'P' (Presente) o 'A' (Ausente)
            autorizado_email (str): Email del usuario que registra
        """
        return self.client._make_request('POST', '/asistencias', {
            'empleado_codigo': empleado_codigo,
            'fecha': fecha,
            'estado': estado,
            'autorizado_email': autorizado_email
        })
    
    def eliminar_asistencia(self, empleado_codigo, fecha):
        """
        Elimina una asistencia (marca como ausente)
        
        Args:
            empleado_codigo (int): Código del empleado
            fecha (str): Fecha en formato 'YYYY-MM-DD'
        """
        return self.client._make_request('DELETE', f'/asistencias/{empleado_codigo}/{fecha}')