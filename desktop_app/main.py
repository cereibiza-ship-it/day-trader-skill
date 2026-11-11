
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
        QMessageBox.information(
            self,
            "Day Trader",
            "La conexión con el analizador "
            "se añadirá en el siguiente paso."
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = DayTrader()
    ventana.show()
    sys.exit(app.exec())
