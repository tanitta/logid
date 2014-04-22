import sys
from PyQt4 import QtGui
import gui.gui_manager


def main():
    gui_manager = gui.gui_manager.GuiManager
    gui_manager.run()

if __name__ == '__main__':
    main()
