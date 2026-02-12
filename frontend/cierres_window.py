from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QPushButton, QTableWidget, QTableWidgetItem,
                               QDialog, QComboBox, QSpinBox, QMessageBox, QHeaderView)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from frontend.styles import AppStyles
from backend.api.cierres_api import CierresAPI
from datetime import datetime

class CierresWindow(QMainWindow):
    def __init__(self, user_email):
        super().__init__()
        self.user_email = user_email
        self.cierres_api = CierresAPI()
        self.cierres_data = []
        self.init_ui()
        self.load_cierres()
    
    def init_ui(self):
        """Inicializa la interfaz de usuario"""
        self.setWindowTitle("Cierres del Mes")
        self.setMinimumSize(900, 600)
        self.setStyleSheet(AppStyles.WINDOW_STYLE)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 20, 30, 20)
        
        # Título
        title = QLabel("CIERRES DEL MES")
        title.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                font-size: 24px;
                font-weight: bold;
                padding: 15px;
                background-color: rgba(255, 140, 0, 0.3);
                border-radius: 8px;
            }
        """)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)
        
        # Botones superiores
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(15)
        
        # Botón Agregar
        self.btn_agregar = QPushButton("AGREGAR CIERRE")
        self.btn_agregar.setStyleSheet(AppStyles.BUTTON_STYLE)
        self.btn_agregar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_agregar.clicked.connect(self.agregar_cierre)
        buttons_layout.addWidget(self.btn_agregar)
        
        # Botón Modificar
        self.btn_modificar = QPushButton("MODIFICAR")
        self.btn_modificar.setStyleSheet(AppStyles.BUTTON_STYLE)
        self.btn_modificar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_modificar.clicked.connect(self.modificar_cierre)
        self.btn_modificar.setEnabled(False)
        buttons_layout.addWidget(self.btn_modificar)
        
        # Botón Eliminar
        self.btn_eliminar = QPushButton("ELIMINAR")
        self.btn_eliminar.setStyleSheet("""
            QPushButton {
                background-color: #DC3545;
                color: #FFFFFF;
                border: none;
                border-radius: 8px;
                padding: 12px 24px;
                font-size: 14px;
                font-weight: bold;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #C82333;
            }
        """)
        self.btn_eliminar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_eliminar.clicked.connect(self.eliminar_cierre)
        self.btn_eliminar.setEnabled(False)
        buttons_layout.addWidget(self.btn_eliminar)
        
        # Botón Cerrar
        self.btn_cerrar = QPushButton("CERRAR")
        self.btn_cerrar.setStyleSheet("""
            QPushButton {
                background-color: #6C757D;
                color: #FFFFFF;
                border: none;
                border-radius: 8px;
                padding: 12px 24px;
                font-size: 14px;
                font-weight: bold;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #5A6268;
            }
        """)
        self.btn_cerrar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_cerrar.clicked.connect(self.close)
        buttons_layout.addWidget(self.btn_cerrar)
        
        buttons_layout.addStretch()
        main_layout.addLayout(buttons_layout)
        
        # Tabla de cierres
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([
            "ID", "Período", "Estado", "Usuario", "Fecha Cambio"
        ])
        
        # Estilos de la tabla
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #F0F8FF;
                border: 2px solid #B0C4DE;
                border-radius: 8px;
                gridline-color: #B0C4DE;
            }
            QTableWidget::item {
                padding: 8px;
                color: #000000;
            }
            QTableWidget::item:selected {
                background-color: #FF8C00;
                color: #FFFFFF;
            }
            QHeaderView::section {
                background-color: #4682B4;
                color: #FFFFFF;
                padding: 10px;
                border: 1px solid #B0C4DE;
                font-weight: bold;
            }
        """)
        
        # Configurar tabla
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.itemSelectionChanged.connect(self.on_selection_changed)
        
        main_layout.addWidget(self.table)
    
    def load_cierres(self):
        """Carga los cierres desde la API"""
        try:
            result = self.cierres_api.get_all_cierres()
            
            if result["success"]:
                self.cierres_data = result["data"]
                self.populate_table()
            else:
                QMessageBox.warning(self, "Error", result["message"])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar cierres: {str(e)}")
    
    def populate_table(self):
        """Llena la tabla con los datos de cierres"""
        self.table.setRowCount(len(self.cierres_data))
        
        for row, cierre in enumerate(self.cierres_data):
            # ID
            self.table.setItem(row, 0, QTableWidgetItem(str(cierre['cierre_id'])))
            
            # Período (formato: MM/YYYY)
            periodo = cierre['cierre_periodo']
            periodo_formateado = f"{periodo[4:6]}/{periodo[0:4]}"
            self.table.setItem(row, 1, QTableWidgetItem(periodo_formateado))
            
            # Estado
            estado_text = "CERRADO" if cierre['cierre_estado'] == 'C' else "ABIERTO"
            estado_item = QTableWidgetItem(estado_text)
            if cierre['cierre_estado'] == 'C':
                estado_item.setBackground(QColor(255, 99, 71))  # Rojo
                estado_item.setForeground(QColor(255, 255, 255))  # Texto blanco
            else:
                estado_item.setBackground(QColor(144, 238, 144))  # Verde claro
            self.table.setItem(row, 2, estado_item)
            
            # Usuario
            self.table.setItem(row, 3, QTableWidgetItem(cierre['cierre_autorizado_email'] or ""))
            
            # Fecha cambio
            fecha_cambio = cierre['cierre_fecha_cambio']
            if fecha_cambio:
                # Formatear fecha
                if isinstance(fecha_cambio, str):
                    fecha_formateada = fecha_cambio
                else:
                    fecha_formateada = fecha_cambio.strftime("%d/%m/%Y %H:%M")
            else:
                fecha_formateada = ""
            self.table.setItem(row, 4, QTableWidgetItem(fecha_formateada))
    
    def on_selection_changed(self):
        """Habilita/deshabilita botones según la selección"""
        has_selection = len(self.table.selectedItems()) > 0
        self.btn_modificar.setEnabled(has_selection)
        self.btn_eliminar.setEnabled(has_selection)
    
    def agregar_cierre(self):
        """Abre el diálogo para agregar un nuevo cierre"""
        dialog = AgregarCierreDialog(self, self.cierres_api, self.user_email)
        if dialog.exec():
            self.load_cierres()
    
    def modificar_cierre(self):
        """Abre el diálogo para modificar el cierre seleccionado"""
        selected_row = self.table.currentRow()
        if selected_row < 0:
            return
        
        cierre = self.cierres_data[selected_row]
        dialog = ModificarCierreDialog(self, self.cierres_api, cierre, self.user_email)
        if dialog.exec():
            self.load_cierres()
    
    def eliminar_cierre(self):
        """Elimina el cierre seleccionado"""
        selected_row = self.table.currentRow()
        if selected_row < 0:
            return
        
        cierre = self.cierres_data[selected_row]
        periodo = cierre['cierre_periodo']
        periodo_formateado = f"{periodo[4:6]}/{periodo[0:4]}"
        
        reply = QMessageBox.question(
            self,
            "Confirmar Eliminación",
            f"¿Está seguro que desea eliminar el cierre del período {periodo_formateado}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            result = self.cierres_api.delete_cierre(cierre['cierre_id'])
            
            if result["success"]:
                QMessageBox.information(self, "Éxito", "Cierre eliminado exitosamente")
                self.load_cierres()
            else:
                QMessageBox.warning(self, "Error", result["message"])


class AgregarCierreDialog(QDialog):
    def __init__(self, parent, api, user_email):
        super().__init__(parent)
        self.api = api
        self.user_email = user_email
        self.init_ui()
    
    def init_ui(self):
        """Inicializa el diálogo de agregar cierre"""
        self.setWindowTitle("Agregar Cierre")
        self.setFixedSize(450, 350)
        self.setStyleSheet(AppStyles.WINDOW_STYLE)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(30, 20, 30, 20)
        
        # Título
        title = QLabel("Nuevo Cierre de Período")
        title.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                font-size: 18px;
                font-weight: bold;
                padding: 10px;
            }
        """)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # Campo Mes
        mes_label = QLabel("Mes:")
        mes_label.setStyleSheet(AppStyles.LABEL_STYLE)
        layout.addWidget(mes_label)
        
        self.mes_combo = QComboBox()
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                 "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        self.mes_combo.addItems(meses)
        self.mes_combo.setCurrentIndex(datetime.now().month - 1)
        self.mes_combo.setStyleSheet("""
            QComboBox {
                background-color: #F0F8FF;
                color: #000000;
                border: 2px solid #B0C4DE;
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 14px;
                min-height: 35px;
            }
        """)
        layout.addWidget(self.mes_combo)
        
        # Campo Año
        anio_label = QLabel("Año:")
        anio_label.setStyleSheet(AppStyles.LABEL_STYLE)
        layout.addWidget(anio_label)
        
        self.anio_spin = QSpinBox()
        self.anio_spin.setRange(2020, 2050)
        self.anio_spin.setValue(datetime.now().year)
        self.anio_spin.setStyleSheet("""
            QSpinBox {
                background-color: #F0F8FF;
                color: #000000;
                border: 2px solid #B0C4DE;
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 14px;
                min-height: 35px;
            }
        """)
        layout.addWidget(self.anio_spin)
        
        # Campo Estado
        estado_label = QLabel("Estado:")
        estado_label.setStyleSheet(AppStyles.LABEL_STYLE)
        layout.addWidget(estado_label)
        
        self.estado_combo = QComboBox()
        self.estado_combo.addItem("CERRADO", "C")
        self.estado_combo.addItem("ABIERTO", "")
        self.estado_combo.setStyleSheet("""
            QComboBox {
                background-color: #F0F8FF;
                color: #000000;
                border: 2px solid #B0C4DE;
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 14px;
                min-height: 35px;
            }
        """)
        layout.addWidget(self.estado_combo)
        
        # Mensaje de error
        self.error_label = QLabel("")
        self.error_label.setStyleSheet(AppStyles.ERROR_LABEL_STYLE)
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.error_label.setWordWrap(True)
        layout.addWidget(self.error_label)
        
        # Botones
        buttons_layout = QHBoxLayout()
        
        btn_guardar = QPushButton("GUARDAR")
        btn_guardar.setStyleSheet(AppStyles.BUTTON_STYLE)
        btn_guardar.clicked.connect(self.guardar)
        buttons_layout.addWidget(btn_guardar)
        
        btn_cancelar = QPushButton("CANCELAR")
        btn_cancelar.setStyleSheet(AppStyles.BUTTON_STYLE)
        btn_cancelar.clicked.connect(self.reject)
        buttons_layout.addWidget(btn_cancelar)
        
        layout.addLayout(buttons_layout)
    
    def guardar(self):
        """Guarda el nuevo cierre"""
        self.error_label.setText("")
        
        mes = self.mes_combo.currentIndex() + 1
        anio = self.anio_spin.value()
        estado = self.estado_combo.currentData()
        
        # Construir período YYYYMM
        periodo = f"{anio}{mes:02d}"
        
        # Crear cierre
        result = self.api.create_cierre({
            'cierre_periodo': periodo,
            'cierre_estado': estado,
            'cierre_autorizado_email': self.user_email
        })
        
        if result["success"]:
            QMessageBox.information(self, "Éxito", "Cierre guardado exitosamente")
            self.accept()
        else:
            self.error_label.setText(result["message"])


class ModificarCierreDialog(QDialog):
    def __init__(self, parent, api, cierre, user_email):
        super().__init__(parent)
        self.api = api
        self.cierre = cierre
        self.user_email = user_email
        self.init_ui()
    
    def init_ui(self):
        """Inicializa el diálogo de modificar cierre"""
        periodo = self.cierre['cierre_periodo']
        periodo_formateado = f"{periodo[4:6]}/{periodo[0:4]}"
        
        self.setWindowTitle("Modificar Cierre")
        self.setFixedSize(450, 300)
        self.setStyleSheet(AppStyles.WINDOW_STYLE)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(30, 20, 30, 20)
        
        # Título
        title = QLabel(f"Modificar Cierre - Período: {periodo_formateado}")
        title.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
            }
        """)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # Info del período (no editable)
        info_label = QLabel(f"El período no puede ser modificado.\nSolo puede cambiar el estado.")
        info_label.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                font-size: 12px;
                padding: 10px;
            }
        """)
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(info_label)
        
        # Campo Estado
        estado_label = QLabel("Estado:")
        estado_label.setStyleSheet(AppStyles.LABEL_STYLE)
        layout.addWidget(estado_label)
        
        self.estado_combo = QComboBox()
        self.estado_combo.addItem("CERRADO", "C")
        self.estado_combo.addItem("ABIERTO", "")
        self.estado_combo.setStyleSheet("""
            QComboBox {
                background-color: #F0F8FF;
                color: #000000;
                border: 2px solid #B0C4DE;
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 14px;
                min-height: 35px;
            }
        """)
        
        # Establecer estado actual
        if self.cierre['cierre_estado'] == 'C':
            self.estado_combo.setCurrentIndex(0)
        else:
            self.estado_combo.setCurrentIndex(1)
        
        layout.addWidget(self.estado_combo)
        
        # Mensaje de error
        self.error_label = QLabel("")
        self.error_label.setStyleSheet(AppStyles.ERROR_LABEL_STYLE)
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.error_label.setWordWrap(True)
        layout.addWidget(self.error_label)
        
        # Botones
        buttons_layout = QHBoxLayout()
        
        btn_guardar = QPushButton("GUARDAR")
        btn_guardar.setStyleSheet(AppStyles.BUTTON_STYLE)
        btn_guardar.clicked.connect(self.guardar)
        buttons_layout.addWidget(btn_guardar)
        
        btn_cancelar = QPushButton("CANCELAR")
        btn_cancelar.setStyleSheet(AppStyles.BUTTON_STYLE)
        btn_cancelar.clicked.connect(self.reject)
        buttons_layout.addWidget(btn_cancelar)
        
        layout.addLayout(buttons_layout)
    
    def guardar(self):
        """Guarda los cambios del cierre"""
        self.error_label.setText("")
        
        estado = self.estado_combo.currentData()
        
        # Actualizar cierre (mismo período, nuevo estado)
        result = self.api.create_cierre({
            'cierre_periodo': self.cierre['cierre_periodo'],
            'cierre_estado': estado,
            'cierre_autorizado_email': self.user_email
        })
        
        if result["success"]:
            QMessageBox.information(self, "Éxito", "Cierre actualizado exitosamente")
            self.accept()
        else:
            self.error_label.setText(result["message"])