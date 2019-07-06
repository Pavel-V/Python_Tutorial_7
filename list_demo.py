# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 09:06:59 2019

@author: Pavel
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import form_list

class FormController(QtWidgets.QWidget, form_list.Ui_Form):
    def __init__(self):
        super().__init__()
        self.list = [] # создаем список как поле класса FormController
        self.setupUi(self)
        self.setup_connection()
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(['id', 'value'])
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.verticalHeader().setVisible(False)

        
    def setup_connection(self):
        self.push_button_append.clicked.connect(self.append_item)
        self.push_button_insert.clicked.connect(self.insert_item)
        self.push_button_del.clicked.connect(self.del_item_by_index)
        self.push_button_remove.clicked.connect(self.remove_item_by_value)

    def append_item(self):
        self.list.append(self.line_edit_new.text())
        self.update_view_list()

    def insert_item(self):
        self.list.insert(self.spin_box_insert.value(), self.line_edit_new.text())
        self.update_view_list()
            
    def del_item_by_index(self):
        id_deleted = self.spin_box_del.value()
        if 0 <= id_deleted < len(self.list): 
            del self.list[self.spin_box_del.value()]
            self.update_view_list()
    
    def remove_item_by_value(self):
        value_removed = self.line_edit_remove.text()
        if value_removed in self.list:
           self.list.remove(value_removed)
           self.update_view_list()
        
    def update_view_list(self):
        self.table_widget.setRowCount(0)
        self.table_widget.setRowCount(len(self.list))
        index = 0
        for e in self.list:
             self.table_widget.setItem(index, 0, QTableWidgetItem(str(index)))
             self.table_widget.setItem(index, 1, QTableWidgetItem(e))
             index += 1
        
        self.spin_box_del.setRange(0, len(self.list) - 1)
        self.spin_box_insert.setRange(0, len(self.list))

def main():
    app = QtWidgets.QApplication(sys.argv)
    form_controller = FormController()
    form_controller.show()
    app.exec()

if __name__ == '__main__':
    main()
