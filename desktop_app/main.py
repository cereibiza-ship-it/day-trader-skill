from desktop_app.datos import cargar_acciones

import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
)


class DayTrader(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Day Trader - Analista Global")
        self.resize(950, 600)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        titulo = QLabel("DAY TRADER")
        titulo.setStyleSheet(
            "font-size: 30px; font-weight: bold;"
        )
        layout.addWidget(titulo)

        subtitulo = QLabel(
            "Analizador de bolsas mundiales y criptomonedas"
        )
        layout.addWidget(subtitulo)

        boton = QPushButton("Analizar mercados")
        boton.clicked.connect(self.analizar)
        layout.addWidget(boton)

        self.tabla = QTableWidget(0, 4)
        self.tabla.setHorizontalHeaderLabels([
            "Activo", "Mercado", "Señal", "Riesgo"
        ])
        self.tabla.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.tabla)

        aviso = QLabel(
            "Versión inicial: sin datos en directo "
            "ni operaciones reales."
        )
        layout.addWidget(aviso)

    def analizar(self):
        try:
            acciones = cargar_acciones()
            self.tabla.setRowCount(len(acciones))

            for fila, accion in enumerate(acciones):
                for columna, clave in enumerate(
                    ("activo", "mercado", "senal", "riesgo")
                ):
                    self.tabla.setItem(
                        fila,
                        columna,
                        QTableWidgetItem(str(accion.get(clave, "")))
                    )

            QMessageBox.information(
                self,
                "Day Trader",
                f"Se han cargado {len(acciones)} acciones del último análisis."
            )
        except Exception as error:
            QMessageBox.warning(self, "Error", str(error))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = DayTrader()
    ventana.show()
    sys.exit(app.exec())
