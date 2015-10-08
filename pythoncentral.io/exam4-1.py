# coding: utf-8
from __future__ import division, print_function, absolute_import, unicode_literals

__author__ = 'hiroshi'
from PySide.QtCore import QObject, Signal, Slot

class PunchingBag(QObject):
    ''' Represents a punching bag; when you punch it, it
        emits a signal that indicates that it was punched. '''
    punched = Signal()

    def __init__(self):
        # Initialize the PunchingBag as a QObject
        QObject.__init__(self)

    def punch(self):
        ''' Punch the bag '''
        self.punched.emit()

@Slot()
def say_punched():
    ''' Give evidence that a bag was punched. '''
    print('Bag was punched.')

def main():
    bag = PunchingBag()
    # Connect the bag's punched signal to the say_punched slot
    bag.punched.connect(say_punched)
    for i in range(10):
        bag.punch()


if __name__ == '__main__':
    main()


