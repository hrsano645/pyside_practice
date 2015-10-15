# coding: utf-8
from __future__ import division, print_function, absolute_import, unicode_literals

import sys
from PySide.QtCore import *
from PySide.QtGui import *


class ExamMainWindow(QMainWindow):
    def __init__(self):
        # QMainWindowsの初期化
        super(ExamMainWindow, self).__init__()

        self.setWindowTitle('メタ構文変数を叫ぶウィンドウ')
        self.setMinimumWidth(400)

        # QWidgetの追加
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # メインのレイアウトを追加
        self.main_layout = QVBoxLayout()

        # QGroupBoxを追加
        self.control_groupbox = QGroupBox(self, title="コントロールエリア")

        # 上-----------
        # フォームレイアウトでラベルをセットできる
        self.form_layout = QFormLayout()

        # フォームに追加するボタン一覧用のhbox作成
        self.button_box = QHBoxLayout()

        # ボタン作成
        self.btn1 = QPushButton("叫ぶ”！！", self)
        self.btn1.setMaximumWidth(150)

        # ボタンをHBoxに追加
        self.button_box.addWidget(self.btn1)

        # フォームにaddRow
        self.form_layout.addRow("叫ぶボタン", self.button_box)

        # コンボボックス追加
        self.meta_val_names = ["hoge", "huga", "hogehuga",
                               "ほげ",  "ふが",
                               "foo", "baz", "bar",
                               "spam", "ham", "egg"
                               ]
        self.combo1 = QComboBox(self)
        self.combo1.addItems(self.meta_val_names)

        # コンボボックスをフォームにaddRow
        self.form_layout.addRow('よく使うメタ構文変数', self.combo1)

        self.control_groupbox.setLayout(self.form_layout)

        self.main_layout.addWidget(self.control_groupbox)

        # ビュー側のレイアウトを生成
        self.list_layout = QVBoxLayout()

        # レイアウトにリストビューを追加
        self.table = QTableView(self)

        # リストビューの変更を禁止
        # ref:http://stackoverflow.com/questions/6226185/uneditable-qlistview
        # ref:http://pyside.github.io/docs/pyside/PySide/QtGui/QAbstractItemView.html?highlight=noedittriggers#PySide.QtGui.PySide.QtGui.QAbstractItemView.editTriggers
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setEditTriggers(QAbstractItemView.NoSelection)

        # tableの見た目を作る
        self.table.hideColumn(False)
        self.table.setShowGrid(True)


        # モデルを追加
        self.table_model = QStandardItemModel(self.table)
        # カラム名を生成する
        # for column_index, column_name in enumerate(["meta word", "test1", "test2"]):
        #     self.table_model.setHorizontalHeaderItem(column_index, QStandardItem(column_name))
        self.table_model.setHorizontalHeaderLabels(["meta word", "test1", "test2"])

        self.table.setModel(self.table_model)

        # リストビューをレイアウトに追加
        self.list_layout.addWidget(self.table)

        # 下側のレイアウトをメインのレイアウトに追加
        self.main_layout.addLayout(self.list_layout)

        # 集まったレイアウトをメインウィジェットに登録
        main_widget.setLayout(self.main_layout)

        message = "A context menu is available by right-clicking"
        self.statusBar().showMessage(message)

        # ボタンクリックのシグナルにスロットを追加
        self.btn1.clicked.connect(self.say_meta_word_button)

        # コンボックスの変更シグナルにスロットを追加
        self.combo1.currentIndexChanged.connect(self.choiced_status)

    @Slot()
    def say_meta_word_button(self):
        """ボタンを押したらコンボックスの現在の選択している文字列を追加する"""
        self.table_model.appendRow(QStandardItem("{} !!".format(self.combo1.currentText())))

    @Slot()
    def choiced_status(self):
        """コンボックスを変更したら変更した文字列をステータスバーに表示する"""
        self.statusBar().showMessage("\"{}\" が選択されました".format(self.combo1.currentText()))


def main():
    app = QApplication(sys.argv)
    window = ExamMainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
