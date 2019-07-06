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
        self.setup_connection() # установка соединений между сигналами и слотами вынесена в отдельную функцию
        self.setup_table() # настройка внешнего вида таблицы для отображения списка

    def setup_table(self):
        self.table_widget.setColumnCount(2) # два столбца
        self.table_widget.setHorizontalHeaderLabels(['id', 'value']) # установка заголовков (названий) столбцов
        self.table_widget.horizontalHeader().setStretchLastSection(True) # мы хотим чтобы столбец с элементами списка растягивался и занимал все свободное место
        self.table_widget.verticalHeader().setVisible(False) # метки (названия) строк не нужны, они будут невидимыми 

        
    def setup_connection(self):
        ''' Каждая кнопка соединяется с соответствующей функцией.'''
        self.push_button_append.clicked.connect(self.append_item)
        self.push_button_insert.clicked.connect(self.insert_item)
        self.push_button_del.clicked.connect(self.del_item_by_index)
        self.push_button_remove.clicked.connect(self.remove_item_by_value)

    def append_item(self):
        ''' Добавляет элемент в конец списка и обновляет таблицу для отображения списка.'''
        self.list.append(self.line_edit_new.text())
        self.update_view()

    def insert_item(self):
        ''' Добавляет элемент в список на заданную позицию и обновляет таблицу для отображения списка.'''
        self.list.insert(self.spin_box_insert.value(), self.line_edit_new.text())
        self.update_view()
            
    def del_item_by_index(self):
        ''' Удаляет элемент с заданным индексом из списка и обновляет таблицу для отображения списка.'''
        id_deleted = self.spin_box_del.value()
        if 0 <= id_deleted < len(self.list):  # проверка индекса на коорректность (id_deleted >= 0 and id_deleted  < len(self.list)
            del self.list[self.spin_box_del.value()]
            self.update_view()
    
    def remove_item_by_value(self):
        ''' Ищет и удаляет элемент с заданным значением из списка и обновляет таблицу для отображения списка.'''
        value_removed = self.line_edit_remove.text()
        if value_removed in self.list:
           self.list.remove(value_removed)
           self.update_view()
        
    def update_view(self):
        ''' Обновляет таблицу и поля для ввода индексов.'''
        self.update_table()
        self.update_spin_boxes()
        
    def update_table(self):
        ''' Обновляет таблицу для отображения списка.'''
        self.table_widget.setRowCount(0) # установка числа строк в ноль удаляет все данные из таблицы
        
        # после очистки таблицы заполняем ее элементами списка
        self.table_widget.setRowCount(len(self.list)) 
        index = 0
        for e in self.list:
             self.table_widget.setItem(index, 0, QTableWidgetItem(str(index)))
             self.table_widget.setItem(index, 1, QTableWidgetItem(e))
             index += 1
        
    def update_spin_boxes(self):
        ''' Обновляет поля ввода индексов с учетом количества элементов в спике.'''
        self.spin_box_del.setRange(0, len(self.list) - 1)
        self.spin_box_insert.setRange(0, len(self.list))

def main():
    app = QtWidgets.QApplication(sys.argv)
    form_controller = FormController()
    form_controller.show()
    app.exec()

if __name__ == '__main__':
    main()
