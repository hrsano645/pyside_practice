# coding: utf-8
from __future__ import division, print_function, absolute_import, unicode_literals

__author__ = 'hiroshi'

import sys
from PySide import QtCore


class Communicate(QtCore.QObject):
     # シグナルをその場で作成し、名前を「speak」とします
     speak = QtCore.Signal(str)


# 新たなスロットを定義します。このスロットは文字列を受け取り
# 名前が「saySomeWords」になります
@QtCore.Slot(str)
def saySomeWords(words):
    print(words)


def main():
    someone = Communicate()
    # シグナルとスロットを接続します
    someone.speak.connect(saySomeWords)
    # 「speak」シグナルを送出します
    someone.speak.emit("Hello everybody!")


if __name__ == '__main__':
    main()
