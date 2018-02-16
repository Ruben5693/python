#!/usr/bin/python
# -*- coding: utf-8 -*-

# Convierte temperaturas
# www.pythondiario.com

import sys
from PyQt4 import QtCore, QtGui, uic

# Cargar nuestro archivo .ui
form_class = uic.loadUiType("eliminar_editar.ui")[0]
ruta=""
class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.cmv_iso.clicked.connect(self.cmv_iso_clicked)

    # Evento del boton cmv_iso
    def cmv_iso_clicked(self):
        text = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home',"Imagen (*.iso)")
        self.cmv_tex_iso.setText(str(text))


app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()
