#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:30:22 2024

@author: jeffmarstell
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.button = QPushButton("clickme!", self)
        self.label = QLabel("Hello", self)
        self.initUI()
       
        
    def initUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)
        
        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px")
        
        
    def on_click(self):
        self.label.setText("Goodbye")
            
            
            
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
