import sys  # Only needed for access to command line arguments

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QListWidget,
                             QComboBox, QFrame, QLineEdit, QGroupBox, QSlider, QListView, QListWidgetItem)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Formulario Examen")

        layoutGeneral = QVBoxLayout()
        layoutFilaArriba = QHBoxLayout()
        layoutFilaAbajo = QHBoxLayout()


        # Diseñamos la parte de arriba a la izquierda con la imagen y la checkbox
        parteDisco = QWidget()
        verticalDisco = QVBoxLayout()
        parteDisco.setLayout(verticalDisco)
        disco = QLabel()
        pixMap = QPixmap("disco.png")
        disco.setPixmap(pixMap)
        checkAnimado = QCheckBox()
        checkAnimado.setText("Animado")
        verticalDisco.addWidget(disco)
        verticalDisco.addWidget(checkAnimado)
        layoutFilaArriba.addWidget(parteDisco)

        # Añadimos la lista en el centro de la zona superior

        lista = QListWidget()
        elementosLista = []
        lista.addItems(elementosLista)
        layoutFilaArriba.addWidget(lista)

        # Añadimos los botones de la zona superior derecha

        botonesVerticales = QVBoxLayout()
        botonAdd = QPushButton("Añadir canción")
        botonSubir = QPushButton("Subir")
        botonBajar = QPushButton("Bajar")
        botonesVerticales.addWidget(botonAdd)
        botonesVerticales.addWidget(botonSubir)
        botonesVerticales.addWidget(botonBajar)

        botonAdd.clicked.connect(lambda: self.clickAdd(lista))
        botonSubir.clicked.connect(lambda: self.subirLista(lista))
        botonBajar.clicked.connect(lambda: self.bajarLista(lista))

        # Añadimos el botón y combobox horizontales

        comboHorizontal = QHBoxLayout()
        botonSaltar = QPushButton("Saltar")
        comboSaltar = QComboBox()
        comboSaltar.addItems(["0", "1", "2", "3", "4", "5", "6", "7", "8"])
        comboHorizontal.addWidget(botonSaltar)
        comboHorizontal.addWidget(comboSaltar)
        botonesVerticales.addLayout(comboHorizontal)

        comboSaltar.currentIndexChanged.connect(lambda: self.actualizarRitmo(comboSaltar, ritmoSlider))

        # Añadimos los botones restantes

        botonAbrir = QPushButton("Abrir archivo")
        botonReproducir = QPushButton("Reproducir")
        botonGuardar = QPushButton("Guardar como...")
        botonEliminar = QPushButton("Eliminar")
        botonesVerticales.addWidget(botonAbrir)
        botonesVerticales.addWidget(botonReproducir)
        botonesVerticales.addWidget(botonGuardar)
        botonesVerticales.addWidget(botonEliminar)

        layoutFilaArriba.addLayout(botonesVerticales)

        # Con la parte superior completa, pasamos a la inferior.
        # En este layout horizontal tendremos una columna con cinco filas y una GroupBox
        # que tendrá dos columnas de checkbox.

        # Definimos el cuadro en el que tendremos las filas
        filasVer = QWidget()
        filasVerticales = QVBoxLayout()
        filasVer.setLayout(filasVerticales)

        # Definimos la primera fila
        primeraFila = QWidget()
        primFila = QHBoxLayout()
        primeraFila.setLayout(primFila)
        sonidoTexto = QLabel("Sonido")
        comboSonido = QComboBox()
        comboSonido.addItems(["", "Maracas", "Marimba", "Triángulo", "Timbales"])
        comboSonido.currentIndexChanged.connect(self.numSonidoEscogido)
        comboSonido.currentTextChanged.connect(self.sonidoEscogido)


        primFila.addWidget(sonidoTexto)
        primFila.addWidget(comboSonido)

        filasVerticales.addWidget(primeraFila)

        # Definimos la segunda fila
        segundaFila = QWidget()
        segFila = QHBoxLayout()
        segundaFila.setLayout(segFila)
        ritmoTexto = QLabel("Ritmo")
        ritmoSlider = QSlider(Qt.Orientation.Horizontal)
        segFila.addWidget(ritmoTexto)
        segFila.addWidget(ritmoSlider)

        ritmoSlider.setMinimum(0)
        ritmoSlider.setMaximum(8)

        filasVerticales.addWidget(segundaFila)

        # Definimos la tercera fila
        terceraFila = QWidget()
        tercFila = QHBoxLayout()
        terceraFila.setLayout(tercFila)
        volumenTexto = QLabel("Volumen")
        volumenSlider = QSlider(Qt.Orientation.Horizontal)

        volumenSlider.setMinimum(0)
        volumenSlider.setMaximum(100)
        volumenSlider.setSingleStep(1)
        volumenSlider.valueChanged.connect(self.cambioVolumen)


        tercFila.addWidget(volumenTexto)
        tercFila.addWidget(volumenSlider)

        filasVerticales.addWidget(terceraFila)

        # Definimos la cuarta fila
        cuartaFila = QWidget()
        cuaFila = QHBoxLayout()
        cuartaFila.setLayout(cuaFila)
        formatoTexto = QLabel("Formato")
        formatoCombo = QComboBox()
        formatoCombo.addItems(["", "MP3", "WAV", "WMA", "OGG"])
        cuaFila.addWidget(formatoTexto)
        cuaFila.addWidget(formatoCombo)
        formatoCombo.currentIndexChanged.connect(self.numFormatoEscogido)
        formatoCombo.currentTextChanged.connect(self.formatoEscogido)

        filasVerticales.addWidget(cuartaFila)

        # Definimos la quinta y última fila
        quintaFila = QWidget()
        quiFila = QHBoxLayout()
        quintaFila.setLayout(quiFila)
        salidaTexto = QLabel("Salida de audio")
        salidaCombo = QComboBox()
        salidaCombo.addItems(["", "1", "2"])
        quiFila.addWidget(salidaTexto)
        quiFila.addWidget(salidaCombo)

        filasVerticales.addWidget(quintaFila)

        # Añadimos el Widget de filas verticales al layout inferior

        layoutFilaAbajo.addWidget(filasVer)


        layoutGeneral.addLayout(layoutFilaArriba)
        layoutGeneral.addLayout(layoutFilaAbajo)

        # Procedemos con el QGroupBox con dos columnas de checkboxes en su interior
        groupBox = QGroupBox("Opciones de reproducción")
        horizontalBox = QHBoxLayout()
        groupBox.setLayout(horizontalBox)

        # Definimos la primera columna de checkboxes
        checkPrimera = QWidget()
        checkPrim = QVBoxLayout()
        checkPrimera.setLayout(checkPrim)
        checkAsinc = QCheckBox("Asíncrono")
        checkNombre = QCheckBox("Nombre de fichero")
        checkPersistente = QCheckBox("XML Persistente")

        checkAsinc.stateChanged.connect(lambda: self.addFiltrar(lista, checkAsinc))
        checkNombre.stateChanged.connect(lambda: self.addFiltrar(lista, checkNombre))
        checkPersistente.stateChanged.connect(lambda: self.addFiltrar(lista, checkPersistente))

        checkPrim.addWidget(checkAsinc)
        checkPrim.addWidget(checkNombre)
        checkPrim.addWidget(checkPersistente)

        horizontalBox.addWidget(checkPrimera)

        # Definimos la segunda columna de checkboxes
        checkSegunda = QWidget()
        checkSeg = QVBoxLayout()
        checkSegunda.setLayout(checkSeg)
        checkFiltrar = QCheckBox("Filtrar")
        checkXML = QCheckBox("Es XML")
        checkReproduccion = QCheckBox("Reproducción NPL")

        checkFiltrar.stateChanged.connect(lambda: self.addFiltrar(lista, checkFiltrar))
        checkXML.stateChanged.connect(lambda: self.addXML(lista, checkXML))
        checkReproduccion.stateChanged.connect(lambda: self.addRepro(lista, checkReproduccion))
        checkSeg.addWidget(checkFiltrar)
        checkSeg.addWidget(checkXML)
        checkSeg.addWidget(checkReproduccion)

        horizontalBox.addWidget(checkSegunda)

        # Y añadimos la groupbox a la parte de abajo

        layoutFilaAbajo.addWidget(groupBox)

        # Utilizamos un dummy widget para el layout base

        widgetLayoutGeneral = QWidget()
        widgetLayoutGeneral.setLayout(layoutGeneral)
        self.setCentralWidget(widgetLayoutGeneral)

    # FUNCIONALIDAD DE LA INTERFAZ

    # Valor del slider de volumen
    def cambioVolumen(self, value):
        print(f"Volumen: {value}")

    # Mostrar sonido escogido en ComboBox
    def numSonidoEscogido(self, i):
        print("Sonido número: ", i)
    def sonidoEscogido(self, s):
        print("Instrumento: ", s)

    # Mostrar formato escogido en ComboBox
    def numFormatoEscogido(self, i):
        print("Formato número: ", i)
    def formatoEscogido(self, s):
        print("Formato: ", s)

    # Añadir elementos a la lista al hacer click

    def clickAdd(self, lista):
        nombreCancion = input("Nombre de la canción: ")
        lista.addItem(nombreCancion)

    # Mostrar las opciones de reproducción en la lista
    def addFiltrar(self, lista, checkFiltrar):
        filtro = checkFiltrar.text()
        fila = lista.currentRow()
        if checkFiltrar.isChecked():
            lista.addItem(filtro)
        else:
            lista.takeItem(fila)

    def addXML(self, lista, checkXML):
        filtro = checkXML.text()
        fila = lista.currentRow()
        if checkXML.isChecked():
            lista.addItem(filtro)
        else:
            lista.takeItem(fila)

    def addRepro(self, lista, checkReproduccion):
        filtro = checkReproduccion.text()
        fila = lista.currentRow()
        if checkReproduccion.isChecked():
            lista.addItem(filtro)
        else:
            lista.takeItem(fila)

    def addAsinc(self, lista, checkAsinc):
        filtro = checkAsinc.text()
        fila = lista.currentRow()
        if checkAsinc.isChecked():
            lista.addItem(filtro)
        else:
            lista.takeItem(fila)

    def addNombre(self, lista, checkNombre):
        filtro = checkNombre.text()
        fila = lista.currentRow()
        if checkNombre.isChecked():
            lista.addItem(filtro)
        else:
            lista.takeItem(fila)

    def addPersistente(self, lista, checkPersistente):
        filtro = checkPersistente.text()
        fila = lista.currentRow()
        if checkPersistente.isChecked():
            lista.addItem(filtro)
        else:
            lista.takeItem(fila)

    # Botones de subir y bajar en la lista
    def subirLista(self, lista):
        fila = lista.currentRow()
        if fila>0:
            lista.setCurrentRow(fila-1)

    def bajarLista(selfs, lista):
        fila = lista.currentRow()
        if fila<lista.count()-1:
            lista.setCurrentRow(fila+1)

    # Función para que al seleccionar una opción el el ComboBox saltar se actualice el slider Ritmo

    def actualizarRitmo(self, comboSaltar, ritmoSlider):

        indiceCombo = comboSaltar.currentIndex()
        ritmoSlider.setSliderPosition(indiceCombo)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
