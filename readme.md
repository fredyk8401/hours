# Sistema de Registro de Horas BRAMIL

Sistema modular de registro de asistencia con arquitectura cliente-servidor.

## 📁 Estructura del Proyecto

```
HOURS/
├── backend/                    # Servidor API REST
│   ├── api/
│   │   ├── __init__.py
│   │   ├── api_client.py      # Cliente HTTP para peticiones
│   │   └── auth_api.py        # API de autenticación
│   ├── __init__.py
│   ├── config.py              # Configuración (local/Railway)
│   ├── database.py            # Manejo de MySQL
│   └── server.py              # Servidor Flask (EJECUTAR PRIMERO)
│
├── frontend/                   # Interfaz gráfica (PySide6)
│   ├── __init__.py
│   ├── styles.py              # Estilos centralizados
│   ├── login_window.py        # Ventana de login
│   └── main_window.py         # Ventana principal
│
├── resources/                  # Recursos estáticos
│   └── icons/                 # Carpeta para iconos/imágenes
│
├── main.py                     # Punto de entrada del cliente
├── run_server.bat             # Ejecutar servidor (Windows)
├── run_client.bat             # Ejecutar cliente (Windows)
├── requirements.txt           # Dependencias
└── README.md                  # Este archivo
```

## 🚀 Instalación

1. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

2. **Configurar la base de datos:**
   - Asegúrate de que MySQL esté corriendo en el puerto 3307
   - La base de datos `helpdesk` debe existir
   - La tabla `autorizados` debe existir con la estructura indicada

## ▶️ Ejecución

### **IMPORTANTE: Ejecutar en orden**

**Opción 1 - Usando archivos .bat (Windows):**

1. **Primero: Ejecutar el servidor backend**
   ```
   Doble clic en: run_server.bat
   ```
   - Espera a ver el mensaje: "Servidor corriendo..."
   - **NO CERRAR esta ventana**

2. **Segundo: Ejecutar el cliente (interfaz gráfica)**
   ```
   Doble clic en: run_client.bat
   ```

**Opción 2 - Desde la terminal:**

1. **Terminal 1 - Servidor:**
   ```bash
   python backend/server.py
   ```

2. **Terminal 2 - Cliente:**
   ```bash
   python main.py
   ```

## 🔧 Configuración

### Base de Datos Local
Edita `backend/config.py` si tus credenciales son diferentes:
```python
LOCAL_DB_CONFIG = {
    'user': 'root',
    'password': 'Paco8401',
    'host': '127.0.0.1',
    'port': 3307,
    'database': 'helpdesk'
}
```

### Migración a Railway
Cuando migres a Railway:
1. Actualiza `RAILWAY_DB_CONFIG` en `backend/config.py`
2. Cambia `USE_LOCAL = False`
3. Despliega el servidor backend en Railway
4. Actualiza `RAILWAY_API_URL` con la URL de Railway

## 🎨 Características

### ✅ Implementado
- ✅ Arquitectura Cliente-Servidor separada
- ✅ API REST con Flask
- ✅ Validación de email (formato válido)
- ✅ Validación de contraseña (8+ caracteres, mayúscula, número)
- ✅ Autenticación contra tabla `autorizados`
- ✅ Interfaz gráfica con PySide6
- ✅ Diseño con colores azul acero
- ✅ Ventana principal con 6 botones de menú
- ✅ Preparado para agregar iconos

### 🔜 Próximos Módulos
- Registro de Horas
- Mantenimiento de Empleados
- Reportes
- Opciones 4, 5 y 6 (por definir)

## 📡 Endpoints API

### Autenticación
- `POST /api/auth/login` - Login de usuario
  ```json
  Request:
  {
    "email": "usuario@ejemplo.com",
    "password": "Password123"
  }
  
  Response:
  {
    "success": true,
    "message": "Autenticación exitosa",
    "data": {
      "id": 1,
      "email": "usuario@ejemplo.com"
    }
  }
  ```

### Pruebas
- `GET /api/health` - Verifica que el servidor esté corriendo
- `GET /api/test-db` - Prueba la conexión a la base de datos

## 🖼️ Agregar Iconos

1. Coloca tus iconos en: `resources/icons/`
2. En los archivos de ventanas, descomenta y ajusta:
   ```python
   btn.setIcon(QIcon("resources/icons/nombre_icono.png"))
   ```

## 🐛 Solución de Problemas

**Error: "No se pudo conectar al servidor"**
- Verifica que el servidor backend esté corriendo
- Revisa que esté en http://127.0.0.1:5000

**Error de conexión a MySQL:**
- Verifica que MySQL esté corriendo
- Confirma el puerto (3307)
- Revisa usuario y contraseña en `config.py`

**Error: "Módulo no encontrado"**
- Ejecuta: `pip install -r requirements.txt`

## 📝 Notas

- El servidor backend **DEBE** estar corriendo antes de ejecutar el cliente
- Los cambios en el código del servidor requieren reiniciarlo
- En producción, cambiar `debug=False` en `server.py`