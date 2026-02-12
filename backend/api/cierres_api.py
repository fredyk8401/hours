"""
API de Cierres
Verifica el estado de cierre de períodos de asistencia
"""
from backend.api.api_client import APIClient

class CierresAPI:
    def __init__(self):
        self.client = APIClient()
    
    def verificar_cierre(self, periodo):
        """
        Verifica si un período está cerrado
        
        Args:
            periodo (str): Período en formato 'YYYYMM' (ej: '202502')
        
        Returns:
            dict: {
                "success": True,
                "cerrado": True/False,
                "mensaje": "..."
            }
        """
        return self.client._make_request('GET', f'/cierres/verificar/{periodo}')
    
    def get_all_cierres(self):
        """Obtiene todos los cierres registrados"""
        return self.client._make_request('GET', '/cierres')
    
    def create_cierre(self, cierre_data):
        """
        Crea o actualiza un cierre
        
        Args:
            cierre_data (dict): {
                'cierre_periodo': str,  # YYYYMM
                'cierre_estado': str,   # 'C' o ''
                'cierre_autorizado_email': str
            }
        """
        return self.client._make_request('POST', '/cierres', cierre_data)
    
    def delete_cierre(self, cierre_id):
        """Elimina un cierre"""
        return self.client._make_request('DELETE', f'/cierres/{cierre_id}')