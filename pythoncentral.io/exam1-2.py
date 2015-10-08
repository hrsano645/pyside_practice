# coding: utf-8
from __future__ import division, print_function, absolute_import, unicode_literals

__author__ = 'hiroshi'
# Allow access to command-line arguments
import sys

# Import the core and GUI elements of Qt
from PySide.QtCore import *
from PySide.QtGui import *

# Create the QApplication object
qt_app = QApplication(sys.argv)

class HelloWorldApp(QLabel):
    ''' A Qt application that displays the text, "Hello, world!" '''
    def __init__(self):
        # Initialize the object as a QLabel
        QLabel.__init__(self, "Hello, world! 日本語も行けるっしょ！！！")

        # Set the size, alignment, and title
        self.setMinimumSize(QSize(600, 400))
        self.setAlignment(Qt.AlignCenter)
        self.setWindowTitle('Hello, world!')

    def run(self):
        ''' Show the application window and start the main event loop '''
        self.show()
        qt_app.exec_()

def main():
# Create an instance of the application and run it
    HelloWorldApp().run()


if __name__ == '__main__':
    main()
