import sys
from PyQt4 import QtGui

class GuiManager():
	"""docstring for GuiManager"""
	def __init__(self, arg):
		super(GuiManager, self).__init__()
		self.arg = arg
		
	def run():
	    app = QtGui.QApplication(sys.argv)
	    label = QtGui.QLabel('RigidChipsDeveloper')
	    w = QtGui.QMainWindow()
	    w.resize(250, 150)
	    w.move(300, 300)
	    w.setWindowTitle('logid')
	    w.setCentralWidget(label)
	    w.show()
	    sys.exit(app.exec_())
	    w.show()
	    sys.exit(app.exec_())
