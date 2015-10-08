# coding: utf-8
from __future__ import division, print_function, absolute_import, unicode_literals

__author__ = 'hiroshi'

import sys
from PySide import QtCore, QtGui


def main():
    # スロットとして使用する関数を定義します
    def sayHello():
        print('Hello world!')

    app = QtGui.QApplication(sys.argv)

    button = QtGui.QPushButton('Say hello!')

    # clickedシグナルとsayHelloスロットを接続します
    button.clicked.connect(sayHello)
    button.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
