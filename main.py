# import sys
# from PyQt4 import QtGui
import sys
import gui.main_window
import PyQt4.QtCore
import PyQt4.QtGui

class TestClass(object):
    """docstring for TestClass"""
    def __init__(self):
        super(TestClass, self).__init__()
    
    def fnc(self):
        self.a = 'hoge'
        print(self.a)
        

def main():
    app = PyQt4.QtGui.QApplication(sys.argv)
    mainwindow = gui.main_window.MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
