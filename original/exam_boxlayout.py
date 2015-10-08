# coding: utf-8
from __future__ import division, print_function, absolute_import, unicode_literals

__author__ = 'hiroshi'

import sys

from PySide.QtCore import *
from Pyside.QtGui import *


qt_app = QApplication(sys.argv)

class ExamBoxLayout(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('ExamBoxLayout')
        self.setMinimumWidth(400)

        # 垂直
        self.layout = QVBoxLayout()

        # QGroupboxを追加
        self.groupbox = QGroupBox(self, "上部ボックス")

        # フォームレイアウトでラベルをセットできる
        self.form_layout = QFormLayout()

        # フォームに追加するボタン一覧用のhbox作成
        self.button_box = QHBoxLayout()

        # ボタン作成
        self.btn1 = QPushButton("ボタン1", self)
        self.btn2 = QPushButton("ボタン1", self)
        self.btn3 = QPushButton("ボタン1", self)

        # ボタンをHBoxに追加
        self.button_box.addWidget(self.btn1)
        self.button_box.addWidget(self.btn2)
        self.button_box.addWidget(self.btn3)

        # フォームにaddRow
        self.lform_layout.addRow("ボタンリスト", self.button_box)

        # コンボボックス追加
        self.nullstr = ["hoge","huga","hogehuga","ほげ","ふが"]
        self.combo1 = QComboBox(self)
        self.combo1.addItems(self.nullstr)

        # コンボボックスをふぉーむにaddRow
        self.form_layout.addRow('適当な文字列', self.combo1)

        # Add the form layout to the main VBox layout
        self.layout.addLayout(self.form_layout)

        # Add stretch to separate the form layout from the button
        self.layout.addStretch(1)


        # ツリービューを追加

        # ステータスバーを追加
        self.statusbar = QStatusBar(self)

        # ウィンドウに作ったレイアウト郡を追加
        self.setLayout(self.layout)

    def run(self):
        # Show the form
        self.show()
        # Run the qt application
        qt_app.exec_()


def main():
    pass


if __name__ == '__main__':
    main()
