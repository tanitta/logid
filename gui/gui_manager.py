import sys
from PyQt4 import QtGui


class GuiManager():
    def __init__(self):
        super(GuiManager, self).__init__()

    def create_action(self):
        self.na = QtGui.QAction()
        self.na.setText('Teste')
        self.na.setShortcut('Ctrl+W')
        self.connect(self.na, QtGui.SIGNAL('triggered()'), self.action_callback)
        
    def run(self):
        app = QtGui.QApplication(sys.argv)
        # label = QtGui.QLabel('RigidChipsDeveloper')
        # button = QtGui.QPushButton('OK')
        # button.resize(200, 50)
        # button.move(100,50)
        w = QtGui.QMainWindow()
        w.resize(250, 150)
        w.move(300, 300)
        w.setWindowTitle('logid')
        # w.setCentralWidget(label)
        # w.setCentralWidget(button)
        
        self.file_menu = self.menuBar().addMenu("&File")
        self.file_menu.addMenu("New...")
        self.file_menu.addMenu("Open...")
        self.edit_menu = self.menuBar().addMenu("&Edit")
        self.edit_menu.addMenu("Undo...")
        
        w.show()
        # self.create_action()
        sys.exit(app.exec_())
        
