# Form implementation generated from reading ui file 'song.ui'
#
# Created by: PyQt6 UI code generator 6.8.0.dev2410211537
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Song_Form(object):
    def setupUi(self, Song_Form):
        Song_Form.setObjectName("Song_Form")
        Song_Form.resize(595, 276)
        self.label = QtWidgets.QLabel(parent=Song_Form)
        self.label.setGeometry(QtCore.QRect(180, 20, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Song_Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 70, 171, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=Song_Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 130, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(parent=Song_Form)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Song_Form)
        self.label_3.setGeometry(QtCore.QRect(390, 20, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.aut_box = QtWidgets.QComboBox(parent=Song_Form)
        self.aut_box.setGeometry(QtCore.QRect(10, 70, 161, 31))
        self.aut_box.setObjectName("aut_box")
        self.genre_box = QtWidgets.QComboBox(parent=Song_Form)
        self.genre_box.setGeometry(QtCore.QRect(380, 70, 161, 31))
        self.genre_box.setObjectName("genre_box")

        self.retranslateUi(Song_Form)
        QtCore.QMetaObject.connectSlotsByName(Song_Form)

    def retranslateUi(self, Song_Form):
        _translate = QtCore.QCoreApplication.translate
        Song_Form.setWindowTitle(_translate("Song_Form", "Form"))
        self.label.setText(_translate("Song_Form", "Введите название песни:"))
        self.pushButton.setText(_translate("Song_Form", "Готово!"))
        self.label_2.setText(_translate("Song_Form", "Выберите автора:"))
        self.label_3.setText(_translate("Song_Form", "Выберите жанр:"))
