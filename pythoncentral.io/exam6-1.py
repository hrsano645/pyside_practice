# coding: utf-8
from __future__ import division, print_function, absolute_import, unicode_literals

__author__ = 'hiroshi'

from PySide.QtGui import *
import pprint

def main():
    pprint.pprint(QImageReader().supportedImageFormats())


if __name__ == '__main__':
    main()
