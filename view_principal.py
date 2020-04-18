import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from list_drag_widget import ListboxWidget

qt_tela_inicial = "telas/principal.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_tela_inicial)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        self.list_images = ListboxWidget()
        self.centralwidget.layout().addWidget(self.list_images)

        self.btn_search.clicked.connect(self.uploate_photos)
    
    def uploate_photos(self):
        tokens = []
        if self.list_images.count() > 0:
            for i in range(self.list_images.count()-1, -1, -1):
                #image_token = self.gp.upload_image(self.list_images.item(i).text())
                tokens.append(image_token)
                self.list_images.takeItem(i)
        
        a=1