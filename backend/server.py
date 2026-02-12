"""
Servidor API REST para el Sistema de Registro de Horas BRAMIL
Ejecutar con: python backend/server.py
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.database import Database
import re

app = Flask(__name__)
CORS(app)  # Permitir peticiones desde el cliente

# Configuración
app.config['JSON_AS_ASCII'] = False

# ============================================================================
# RUTAS DE AUTENTICACIÓN
# ============================================================================

@app.route('/api/auth/login', methods=['POST'])
def login():
    """
    Endpoint para autenticar usuarios
    
    Body JSON:
    {
        "email": "usuario@ejemplo.com",
        "password": "Password123"
    }
    
    Response:
    {
        "success": true/false,
        "message": "...",
        "data": {
            "id": 1,
            "email": "usuario@ejemplo.com"
        }
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                "success": False,
                "message": "No se recibieron datos"
            }), 400
        
        email = data.get('email', '').strip()
        password = data.get('password', '')
        
        # Validaciones
        if not email or not password:
            return jsonify({
                "success": False,
                "message": "Email y contraseña son requeridos"
            }), 400
        
        # Conectar a la base de datos
        db = Database()
        if not db.connect():
            return jsonify({
                "success": False,
                "message": "Error de conexión a la base de datos"
            }), 500
        
        # Buscar usuario
        query = """
            SELECT autorizado_id, autorizado_email 
            FROM autorizados 
            WHERE autorizado_email = %s AND autorizado_password = %s
        """
        result = db.execute_query(query, (email, password))
        db.disconnect()
        
        if result and len(result) > 0:
            return jsonify({
                "success": True,
                "message": "Autenticación exitosa",
                "data": {
                    "id": result[0]['autorizado_id'],
                    "email": result[0]['autorizado_email']
                }
            }), 200
        else:
            return jsonify({
                "success": False,
                "message": "Credenciales inválidas"
            }), 401
    
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error en el servidor: {str(e)}"
        }), 500


# ============================================================================
# RUTAS DE PRUEBA
# ============================================================================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint para verificar que el servidor está funcionando"""
    return jsonify({
        "status": "online",
        "message": "API de Registro de Horas BRAMIL funcionando correctamente"
    }), 200


@app.route('/api/test-db', methods=['GET'])
def test_database():
    """Endpoint para probar la conexión a la base de datos"""
    db = Database()
    if db.connect():
        db.disconnect()
        return jsonify({
            "success": True,
            "message": "Conexión a la base de datos exitosa"
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Error al conectar a la base de datos"
        }), 500


# ============================================================================
# RUTAS DE EMPLEADOS
# ============================================================================

@app.route('/api/empleados', methods=['GET'])
def get_empleados():
    """
    Obtiene la lista de todos los empleados
    
    Response:
    {
        "success": true/false,
        "data": [
            {
                "empleado_id": 1,
                "empleado_codigo": 1001,
                "empleado_nombres": "Juan Pérez",
                "empleado_email": "juan@example.com",
                "empleado_estado": "V"
            }
        ]
    }
    """
    try:
        db = Database()
        if not db.connect():
            return jsonify({
                "success": False,
                "message": "Error de conexión a la base de datos"
            }), 500
        
        query = """
            SELECT empleado_id, empleado_codigo, empleado_nombres, 
                   empleado_email, empleado_estado
            FROM empleados
            ORDER BY empleado_codigo
        """
        result = db.execute_query(query)
        db.disconnect()
        
        return jsonify({
            "success": True,
            "data": result if result else []
        }), 200
    
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error en el servidor: {str(e)}"
        }), 500


@app.route('/api/empleados', methods=['POST'])
def create_empleado():
    """
    Crea un nuevo empleado
    
    Body JSON:
    {
        "empleado_codigo": 1001,
        "empleado_nombres": "Juan Pérez"
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                "success": False,
                "message": "No se recibieron datos"
            }), 400
        
        codigo = data.get('empleado_codigo')
        nombres = data.get('empleado_nombres', '').strip()
        
        # Validaciones
        if not codigo:
            return jsonify({
                "success": False,
                "message": "El código del empleado es requerido"
            }), 400
        
        if not nombres:
            return jsonify({
                "success": False,
                "message": "El nombre del empleado es requerido"
            }), 400
        
        db = Database()
        if not db.connect():
            return jsonify({
                "success": False,
                "message": "Error de conexión a la base de datos"
            }), 500
        
        # Verificar si el código ya existe
        check_query = "SELECT empleado_id FROM empleados WHERE empleado_codigo = %s"
        existing = db.execute_query(check_query, (codigo,))
        
        if existing and len(existing) > 0:
            db.disconnect()
            return jsonify({
                "success": False,
                "message": f"El código {codigo} ya existe"
            }), 400
        
        # Insertar nuevo empleado
        insert_query = """
            INSERT INTO empleados (empleado_codigo, empleado_nombres, empleado_estado)
            VALUES (%s, %s, 'V')
        """
        success = db.execute_update(insert_query, (codigo, nombres))
        db.disconnect()
        
        if success:
            return jsonify({
                "success": True,
                "message": "Empleado creado exitosamente"
            }), 201
        else:
            return jsonify({
                "success": False,
                "message": "Error al crear el empleado"
            }), 500
    
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error en el servidor: {str(e)}"
        }), 500


@app.route('/api/empleados/<int:empleado_id>', methods=['PUT'])
def update_empleado(empleado_id):
    """
    Actualiza un empleado existente
    
    Body JSON:
    {
        "empleado_nombres": "Juan Pérez Actualizado",
        "empleado_estado": "V"
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                "success": False,
                "message": "No se recibieron datos"
            }), 400
        
        nombres = data.get('empleado_nombres', '').strip()
        estado = data.get('empleado_estado', '').strip()
        
        # Validaciones
        if not nombres:
            return jsonify({
                "success": False,
                "message": "El nombre del empleado es requerido"
            }), 400
        
        if not estado or estado not in ['V', 'I']:
            return jsonify({
                "success": False,
                "message": "Estado inválido. Use 'V' (Vigente) o 'I' (Inactivo)"
            }), 400
        
        db = Database()
        if not db.connect():
            return jsonify({
                "success": False,
                "message": "Error de conexión a la base de datos"
            }), 500
        
        # Actualizar empleado
        update_query = """
            UPDATE empleados 
            SET empleado_nombres = %s, empleado_estado = %s
            WHERE empleado_id = %s
        """
        success = db.execute_update(update_query, (nombres, estado, empleado_id))
        db.disconnect()
        
        if success:
            return jsonify({
                "success": True,
                "message": "Empleado actualizado exitosamente"
            }), 200
        else:
            return jsonify({
                "success": False,
                "message": "Error al actualizar el empleado"
            }), 500
    
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error en el servidor: {str(e)}"
        }), 500


@app.route('/api/empleados/check-codigo/<int:codigo>', methods=['GET'])
def check_codigo_empleado(codigo):
    """Verifica si un código de empleado ya existe"""
    try:
        db = Database()
        if not db.connect():
            return jsonify({
                "success": False,
                "message": "Error de conexión a la base de datos"
            }), 500
        
        query = "SELECT empleado_id FROM empleados WHERE empleado_codigo = %s"
        result = db.execute_query(query, (codigo,))
        db.disconnect()
        
        exists = result and len(result) > 0
        
        return jsonify({
            "success": True,
            "exists": exists
        }), 200
    
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error en el servidor: {str(e)}"
        }), 500


# ============================================================================
# RUTAS DE CIERRES
# ============================================================================

@app.route('/api/cierres/verificar/<string:periodo>', methods=['GET'])
def verificar_cierre(periodo):
    """
    Verifica si un período está cerrado
    
    Args:
        periodo: Formato YYYYMM (ej: '202502' para Febrero 2025)
    
    Response:
    {
        "success": true,
        "cerrado": false,
        "mensaje": "Período abierto para edición"
    }
    """
    try:
        # Validar formato del período
        if len(periodo) != 6 or not periodo.isdigit():
            return jsonify({
                "success": False,
                "message": "Formato de período inválido. Use YYYYMM"
            }), 400
        
        db = Database()
        if not db.connect():
            return jsonify({
                "success": False,
                "message": "Error de conexión a la base de datos"
            }), 500
        
        # Verificar si existe un cierre para este período
        query = """
            SELECT cierre_estado 
            FROM cierres 
            WHERE cierre_periodo = %s
        """
        result = db.execute_query(query, (periodo,))
        db.disconnect()
        
        # Si no existe registro, el período está abierto
        if not result or len(result) == 0:
            return jsonify({
                "success": True,
                "cerrado": False,
                "mensaje": "Período abierto para edición"
            }), 200
        
        # Si existe, verificar el estado
        estado = result[0]['cierre_estado']
        
        if estado == 'C':
            return jsonify({
                "success": True,
                "cerrado": True,
                "mensaje": f"El período {periodo[4:6]}/{periodo[0:4]} está CERRADO y no puede ser modificado"
            }), 200
        else:
            return jsonify({
                "success": True,
                "cerrado": False,
                "mensaje": f"Período {periodo[4:6]}/{periodo[0:4]} abierto para edición (Estado: {estado})"
            }), 200
    
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error en el servidor: {str(e)}"
        }), 500
###
@app.route('/api/cierres', methods=['GET'])
def get_cierres():
    """Obtiene todos los cierres registrados"""
    try:
        db = Database()
        if not db.connect():
            return jsonify({
                "success": False,
                "message": "Error de conexión a la base de datos"
            }), 500
        
        query = """
            SELECT cierre_id, cierre_periodo, cierre_estado, 
                   cierre_autorizado_email, cierre_fecha_cambio
            FROM cierres
            ORDER BY cierre_periodo DESC
        """
        result = db.execute_query(query)
        db.disconnect()
        
        return jsonify({
            "success": True,
            "data": result if result else []
        }), 200
    
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error en el servidor: {str(e)}"
        }), 500


@app.route('/api/cierres', methods=['POST'])
def create_cierre():
    """Crea o actualiza un cierre de período"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                "success": False,
                "message": "No se recibieron datos"
            }), 400
        
        periodo = data.get('cierre_periodo')
        estado = data.get('cierre_estado', '').strip()
        autorizado_email = data.get('cierre_autorizado_email')
        
        # Validaciones
        if not periodo or len(periodo) != 6 or not periodo.isdigit():
            return jsonify({
                "success": False,
                "message": "Período inválido. Use formato YYYYMM"
            }), 400
        
        if estado not in ['C', '']:
            return jsonify({
                "success": False,
                "message": "Estado inválido. Use 'C' (Cerrado) o '' (Abierto)"
            }), 400
        
        if not autorizado_email:
            return jsonify({
                "success": False,
                "message": "Email del usuario autorizado es requerido"
            }), 400
        
        db = Database()
        if not db.connect():
            return jsonify({
                "success": False,
                "message": "Error de conexión a la base de datos"
            }), 500
        
        query = """
            INSERT INTO cierres 
                (cierre_periodo, cierre_estado, cierre_autorizado_email, cierre_fecha_cambio)
            VALUES (%s, %s, %s, NOW())
            ON DUPLICATE KEY UPDATE 
                cierre_estado = VALUES(cierre_estado),
                cierre_autorizado_email = VALUES(cierre_autorizado_email),
                cierre_fecha_cambio = NOW()
        """
        success = db.execute_update(query, (periodo, estado, autorizado_email))
        db.disconnect()
        
        if success:
            return jsonify({
                "success": True,
                "message": "Cierre registrado exitosamente"
            }), 200
        else:
            return jsonify({
                "success": False,
                "message": "Error al registrar el cierre"
            }), 500
    
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error en el servidor: {str(e)}"
        }), 500


@app.route('/api/cierres/<int:cierre_id>', methods=['DELETE'])
def delete_cierre(cierre_id):
    """Elimina un cierre"""
    try:
        db = Database()
        if not db.connect():
            return jsonify({
                "success": False,
                "message": "Error de conexión a la base de datos"
            }), 500
        
        query = "DELETE FROM cierres WHERE cierre_id = %s"
        success = db.execute_update(query, (cierre_id,))
        db.disconnect()
        
        if success:
            return jsonify({
                "success": True,
                "message": "Cierre eliminado exitosamente"
            }), 200
        else:
            return jsonify({
                "success": False,
                "message": "Error al eliminar el cierre"
            }), 500
    
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error en el servidor: {str(e)}"
        }), 500
###

# ============================================================================
# RUTAS DE ASISTENCIAS
# ============================================================================

@app.route('/api/asistencias/<int:anio>/<int:mes>', methods=['GET'])
def get_asistencias_mes(anio, mes):
    """
    Obtiene empleados vigentes y sus asistencias del mes
    
    Response:
    {
        "success": true,
        "data": {
            "empleados": [
                {
                    "empleado_codigo": 1001,
                    "empleado_nombres": "Juan Pérez"
                }
            ],
            "asistencias": [
                {
                    "empleado_codigo": 1001,
                    "fecha": "2024-01-15",
                    "estado": "P"
                }
            ]
        }
    }
    """
    try:
        db = Database()
        if not db.connect():
            return jsonify({
                "success": False,
                "message": "Error de conexión a la base de datos"
            }), 500
        
        # Obtener empleados vigentes (SIN empleado_id para ahorrar espacio)
        empleados_query = """
            SELECT empleado_codigo, empleado_nombres
            FROM empleados
            WHERE empleado_estado = 'V'
            ORDER BY empleado_codigo
        """
        empleados = db.execute_query(empleados_query)
        
        # Obtener asistencias del mes
        asistencias_query = """
            SELECT asistencia_empleado_codigo, 
                   DATE_FORMAT(fecha, '%Y-%m-%d') as fecha, 
                   estado
            FROM asistencias
            WHERE YEAR(fecha) = %s AND MONTH(fecha) = %s
            ORDER BY fecha
        """
        asistencias = db.execute_query(asistencias_query, (anio, mes))
        
        db.disconnect()
        
        return jsonify({
            "success": True,
            "data": {
                "empleados": empleados if empleados else [],
                "asistencias": asistencias if asistencias else []
            }
        }), 200
    
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error en el servidor: {str(e)}"
        }), 500


@app.route('/api/asistencias', methods=['POST'])
def registrar_asistencia():
    """
    Registra o actualiza una asistencia
    
    Body JSON:
    {
        "empleado_codigo": 1001,
        "fecha": "2024-01-15",
        "estado": "P",
        "autorizado_email": "admin@example.com"
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                "success": False,
                "message": "No se recibieron datos"
            }), 400
        
        empleado_codigo = data.get('empleado_codigo')
        fecha = data.get('fecha')
        estado = data.get('estado')
        autorizado_email = data.get('autorizado_email')
        
        # Validaciones
        if not empleado_codigo or not fecha or not estado:
            return jsonify({
                "success": False,
                "message": "Datos incompletos"
            }), 400
        
        if estado not in ['P', 'A']:
            return jsonify({
                "success": False,
                "message": "Estado inválido. Use 'P' o 'A'"
            }), 400
        
        db = Database()
        if not db.connect():
            return jsonify({
                "success": False,
                "message": "Error de conexión a la base de datos"
            }), 500
        
        # Insertar o actualizar (usando ON DUPLICATE KEY UPDATE)
        query = """
            INSERT INTO asistencias 
                (asistencia_empleado_codigo, fecha, estado, 
                 asistencia_autorizado_email, asistencia_fecha_cambio)
            VALUES (%s, %s, %s, %s, NOW())
            ON DUPLICATE KEY UPDATE 
                estado = VALUES(estado),
                asistencia_autorizado_email = VALUES(asistencia_autorizado_email),
                asistencia_fecha_cambio = NOW()
        """
        success = db.execute_update(query, (empleado_codigo, fecha, estado, autorizado_email))
        db.disconnect()
        
        if success:
            return jsonify({
                "success": True,
                "message": "Asistencia registrada"
            }), 200
        else:
            return jsonify({
                "success": False,
                "message": "Error al registrar asistencia"
            }), 500
    
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error en el servidor: {str(e)}"
        }), 500


@app.route('/api/asistencias/<int:empleado_codigo>/<string:fecha>', methods=['DELETE'])
def eliminar_asistencia(empleado_codigo, fecha):
    """Elimina una asistencia"""
    try:
        db = Database()
        if not db.connect():
            return jsonify({
                "success": False,
                "message": "Error de conexión a la base de datos"
            }), 500
        
        query = """
            DELETE FROM asistencias 
            WHERE asistencia_empleado_codigo = %s AND fecha = %s
        """
        success = db.execute_update(query, (empleado_codigo, fecha))
        db.disconnect()
        
        if success:
            return jsonify({
                "success": True,
                "message": "Asistencia eliminada"
            }), 200
        else:
            return jsonify({
                "success": False,
                "message": "Error al eliminar asistencia"
            }), 500
    
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error en el servidor: {str(e)}"
        }), 500


# ============================================================================
# RUTAS PARA FUTUROS MÓDULOS (Preparadas)
# ============================================================================

# Ejemplo de estructura para futuros endpoints:
# @app.route('/api/empleados', methods=['GET', 'POST'])
# @app.route('/api/empleados/<int:id>', methods=['GET', 'PUT', 'DELETE'])
# @app.route('/api/horas', methods=['GET', 'POST'])
# @app.route('/api/reportes', methods=['GET'])


# ============================================================================
# INICIAR SERVIDOR
# ============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Servidor API de Registro de Horas BRAMIL")
    print("=" * 60)
    
    # Detectar si estamos en Railway o local
    import os
    port = int(os.environ.get('PORT', 5000))
    is_railway = os.environ.get('RAILWAY_ENVIRONMENT') is not None
    host = '0.0.0.0' if is_railway else '127.0.0.1'
    debug_mode = not is_railway
    
    print(f"📡 Entorno: {'RAILWAY' if is_railway else 'LOCAL'}")
    print(f"📡 URL del servidor: http://{host}:{port}")
    print("📋 Endpoints disponibles:")
    print("   - GET  /api/health       (Verificar estado del servidor)")
    print("   - GET  /api/test-db      (Probar conexión a BD)")
    print("   - POST /api/auth/login   (Autenticación de usuarios)")
    print("   - GET  /api/empleados    (Listar empleados)")
    print("   - POST /api/empleados    (Crear empleado)")
    print("   - PUT  /api/empleados/:id (Actualizar empleado)")
    print("   - GET  /api/cierres      (Listar cierres)")
    print("   - POST /api/cierres      (Crear/actualizar cierre)")
    print("   - DELETE /api/cierres/:id (Eliminar cierre)")
    print("   - GET  /api/cierres/verificar/:periodo (Verificar cierre)")
    print("   - GET  /api/asistencias/:anio/:mes (Listar asistencias del mes)")
    print("   - POST /api/asistencias  (Registrar asistencia)")
    print("   - DELETE /api/asistencias/:codigo/:fecha (Eliminar asistencia)")
    print("=" * 60)
    print("✅ Servidor corriendo... (Ctrl+C para detener)")
    print()
    
    app.run(
        host=host,
        port=port,
        debug=debug_mode
    )