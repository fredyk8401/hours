# Configuración de la base de datos
# Este archivo permite migrar fácilmente entre MySQL local y Railway

import os

class Config:
    # Configuración para MySQL Local
    LOCAL_DB_CONFIG = {
        'user': 'root',
        'password': 'Paco8401',
        'host': '127.0.0.1',
        'port': 3307,
        'database': 'helpdesk'
    }
    
    # Configuración para Railway (desde variables de entorno)
    RAILWAY_DB_CONFIG = {
        'user': os.environ.get('MYSQL_USER', 'root'),
        'password': os.environ.get('MYSQL_PASSWORD', ''),
        'host': os.environ.get('MYSQL_HOST', ''),
        'port': int(os.environ.get('MYSQL_PORT', 3306)),
        'database': os.environ.get('MYSQL_DATABASE', 'railway')
    }
    
    # URL del API (cambiar según el entorno)
    LOCAL_API_URL = 'http://127.0.0.1:5000/api'
    RAILWAY_API_URL = os.environ.get('RAILWAY_API_URL', 'https://your-railway-url.up.railway.app/api')
    
    # Detectar entorno automáticamente
    USE_LOCAL = os.environ.get('RAILWAY_ENVIRONMENT') is None
    
    @classmethod
    def get_db_config(cls):
        return cls.LOCAL_DB_CONFIG if cls.USE_LOCAL else cls.RAILWAY_DB_CONFIG
    
    @classmethod
    def get_api_url(cls):
        return cls.LOCAL_API_URL if cls.USE_LOCAL else cls.RAILWAY_API_URL