#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:28:51 2024

@author: jeffmarstell
"""


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("icon goes here"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: cyan;"
                            "background-color: green;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        #label.setAlignment(Qt.AlignTop)#align top
        #label.setAlignment(Qt.AlignBottom)#align bottom
        #label.setAlignment(Qt.AlignVCenter) #vetically center

        #label.setAlignment(Qt.AlignRight)#Horizontally Right
        #label.setAlignment(Qt.AlignCenter)#Horizontally aligned center
        #label.setAlignment(Qt.AlignLeft) #qalign left
        
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)#center and top
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) #center Bottom
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #center & center
        label.setAlignment(Qt.AlignCenter)
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
