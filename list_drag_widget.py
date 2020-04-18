from PyQt5.QtWidgets import QListWidget
from PyQt5.QtCore import Qt
 
class ListboxWidget(QListWidget):
    VALID_FILE_TYPES = ['png', 'jpg']

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
 
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
 
    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)          
            event.accept()
        else:
            event.ignore()
 
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
 
            links = []
            for url in event.mimeData().urls():
                file_path = str(url.toLocalFile())
                file_type = str(url.toLocalFile()).split('.')[-1]
                if (url.isLocalFile() and file_type.lower() in ListboxWidget.VALID_FILE_TYPES):
                    links.append(file_path)
                else:
                    pass
            self.addItems(links)
        else:
            event.ignore()