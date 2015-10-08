# coding: utf-8
from __future__ import division, print_function, absolute_import, unicode_literals

__author__ = 'hiroshi'

import sys
from PySide.QtCore import *
from PySide.QtGui import *

def main():
    # Create a Qt application
    app = QApplication(sys.argv)

    # Our main window will be a QListView
    # info:2015-10-07:Change valiable name. because "list" is python reserve name.
    list_ = QListView()
    list_.setWindowTitle('Example List')
    list_.setMinimumSize(600, 400)

    # Create an empty model for the list_'s data
    model = QStandardItemModel(list_)

    # Add some textual items
    foods = [
        'Cookie dough', # Must be store-bought
        'Hummus', # Must be homemade
        'Spaghetti', # Must be saucy
        'Dal makhani', # Must be spicy
        'Chocolate whipped cream' # Must be plentiful
    ]

    for food in foods:
        # create an item with a caption
        item = QStandardItem(food)

        # add a checkbox to it
        item.setCheckable(True)

        # Add the item to the model
        model.appendRow(item)

    # Apply the model to the list_ view
    list_.setModel(model)

    # Show the window and run the app
    list_.show()
    app.exec_()


if __name__ == '__main__':
    main()
