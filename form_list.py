# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python_Projects\PyQtTest\work_7\form_list.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1117, 354)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.line_edit_new = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_new.sizePolicy().hasHeightForWidth())
        self.line_edit_new.setSizePolicy(sizePolicy)
        self.line_edit_new.setObjectName("line_edit_new")
        self.verticalLayout.addWidget(self.line_edit_new)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.push_button_append = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_append.sizePolicy().hasHeightForWidth())
        self.push_button_append.setSizePolicy(sizePolicy)
        self.push_button_append.setObjectName("push_button_append")
        self.verticalLayout.addWidget(self.push_button_append)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.push_button_insert = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_insert.sizePolicy().hasHeightForWidth())
        self.push_button_insert.setSizePolicy(sizePolicy)
        self.push_button_insert.setObjectName("push_button_insert")
        self.horizontalLayout.addWidget(self.push_button_insert)
        self.spin_box_insert = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_box_insert.sizePolicy().hasHeightForWidth())
        self.spin_box_insert.setSizePolicy(sizePolicy)
        self.spin_box_insert.setObjectName("spin_box_insert")
        self.horizontalLayout.addWidget(self.spin_box_insert)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.push_button_del = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_del.sizePolicy().hasHeightForWidth())
        self.push_button_del.setSizePolicy(sizePolicy)
        self.push_button_del.setObjectName("push_button_del")
        self.horizontalLayout_3.addWidget(self.push_button_del)
        self.spin_box_del = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_box_del.sizePolicy().hasHeightForWidth())
        self.spin_box_del.setSizePolicy(sizePolicy)
        self.spin_box_del.setObjectName("spin_box_del")
        self.horizontalLayout_3.addWidget(self.spin_box_del)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.push_button_remove = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_remove.sizePolicy().hasHeightForWidth())
        self.push_button_remove.setSizePolicy(sizePolicy)
        self.push_button_remove.setObjectName("push_button_remove")
        self.horizontalLayout_2.addWidget(self.push_button_remove)
        self.line_edit_remove = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_remove.sizePolicy().hasHeightForWidth())
        self.line_edit_remove.setSizePolicy(sizePolicy)
        self.line_edit_remove.setObjectName("line_edit_remove")
        self.horizontalLayout_2.addWidget(self.line_edit_remove)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.table_widget = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_widget.sizePolicy().hasHeightForWidth())
        self.table_widget.setSizePolicy(sizePolicy)
        self.table_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setColumnCount(0)
        self.table_widget.setRowCount(0)
        self.horizontalLayout_4.addWidget(self.table_widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Список"))
        self.label_2.setText(_translate("Form", "Новый элемент"))
        self.label.setText(_translate("Form", "Добавить в конец"))
        self.push_button_append.setText(_translate("Form", "Добавить"))
        self.label_3.setText(_translate("Form", "Вставить в позицию"))
        self.push_button_insert.setText(_translate("Form", "Вставить"))
        self.label_4.setText(_translate("Form", "Удалить по индексу"))
        self.push_button_del.setText(_translate("Form", "Удалить"))
        self.label_5.setText(_translate("Form", "Удалить по значению"))
        self.push_button_remove.setText(_translate("Form", "Удалить"))

