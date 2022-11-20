import peewee

from classes import *
from operations import *
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem, QHeaderView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(703, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 0, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 321, 17))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 60, 651, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addbook_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.addbook_btn.setObjectName("addbook_btn")
        self.horizontalLayout_2.addWidget(self.addbook_btn)
        self.delbook_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.delbook_btn.setObjectName("delbook_btn")
        self.horizontalLayout_2.addWidget(self.delbook_btn)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 90, 651, 27))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addshelf_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.addshelf_btn.setObjectName("addshelf_btn")
        self.horizontalLayout_3.addWidget(self.addshelf_btn)
        self.delshelf_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.delshelf_btn.setObjectName("delshelf_btn")
        self.horizontalLayout_3.addWidget(self.delshelf_btn)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(20, 120, 651, 411))
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 703, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Картотека"))
        self.label_2.setText(_translate("MainWindow", "Ваш путеводитель в мире книжных шкафов"))
        self.addbook_btn.setText(_translate("MainWindow", "Добавить книгу"))
        self.delbook_btn.setText(_translate("MainWindow", "Удалить книгу"))
        self.addshelf_btn.setText(_translate("MainWindow", "Добавить шкаф"))
        self.delshelf_btn.setText(_translate("MainWindow", "Удалить шкаф/полку"))


class HomeWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addbook_btn.clicked.connect(self.add_book)
        self.addshelf_btn.clicked.connect(self.add_shelf)
        self.delbook_btn.clicked.connect(self.delete_book)
        self.delshelf_btn.clicked.connect(self.delete_shelf)
        self.loadTable()

    def loadTable(self):
        self.table.clear()
        res = all_cabinets()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['Шкаф', 'Полка', 'Книга', 'Автор', 'Жанр'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.table.setRowCount(0)
        for i, row in enumerate(res):
            self.table.setRowCount(
                self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(
                    i, j, QTableWidgetItem(elem))
        self.table.resizeColumnsToContents()

    def add_book(self):
        self.window = AddNewBook()
        self.window.setMainWin(self)
        self.window.show()

    def add_shelf(self):
        self.windoww = AddNewShelf()
        self.windoww.setMainWin(self)
        self.windoww.show()

    def delete_book(self):
        self.window1 = DeleteBook()
        self.window1.setMainWin(self)
        self.window1.show()

    def delete_shelf(self):
        self.windoww1 = DeleteShelf()
        self.windoww1.setMainWin(self)
        self.windoww1.show()


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 205)
        Dialog.setModal(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 10, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.error_label = QtWidgets.QLabel(Dialog)
        self.error_label.setGeometry(QtCore.QRect(10, 109, 371, 41))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 371, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.shelfname_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.shelfname_line.setObjectName("shelfname_line")
        self.horizontalLayout.addWidget(self.shelfname_line)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 80, 371, 28))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.shelves_count = QtWidgets.QSpinBox(self.layoutWidget1)
        self.shelves_count.setObjectName("shelves_count")
        self.horizontalLayout_2.addWidget(self.shelves_count)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(190, 150, 191, 41))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cancel_btn = QtWidgets.QPushButton(self.layoutWidget2)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_3.addWidget(self.cancel_btn)
        self.ok_btn = QtWidgets.QPushButton(self.layoutWidget2)
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout_3.addWidget(self.ok_btn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Добавить новый шкаф"))
        self.label_2.setText(_translate("Dialog", "Название:"))
        self.label_3.setText(_translate("Dialog", "Количество полок:"))
        self.cancel_btn.setText(_translate("Dialog", "Отмена"))
        self.ok_btn.setText(_translate("Dialog", "ОК"))


class AddNewShelf(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ok_btn.clicked.connect(self.run)
        self.cancel_btn.clicked.connect(self.cancel)

    def setMainWin(self, win):
        self.mainWin = win

    def run(self):
        self.shelf_name = self.shelfname_line.text()
        self.n = self.shelves_count.value()
        if not self.shelf_name:
            self.error_label.setText('Ошибка! Введите название шкафа.')
        elif self.shelf_name in all_bookshelves():
            self.error_label.setText('Ошибка! Неправильное название шкафа.')
        elif self.n == 0:
            self.error_label.setText('Ошибка! Добавьте полки.')
        else:
            add_bookshelf(self.shelf_name, self.n)
            self.mainWin.loadTable()
            self.close()

    def cancel(self):
        self.mainWin.loadTable()
        self.close()


class Ui_delete_shelf(object):
    def setupUi(self, delete_shelf):
        delete_shelf.setObjectName("delete_shelf")
        delete_shelf.resize(401, 197)
        self.label = QtWidgets.QLabel(delete_shelf)
        self.label.setGeometry(QtCore.QRect(90, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.error_label = QtWidgets.QLabel(delete_shelf)
        self.error_label.setGeometry(QtCore.QRect(10, 130, 381, 17))
        self.error_label.setObjectName("error_label")
        self.widget = QtWidgets.QWidget(delete_shelf)
        self.widget.setGeometry(QtCore.QRect(10, 50, 381, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.bookshelf_box = QtWidgets.QComboBox(self.widget)
        self.bookshelf_box.setObjectName("bookshelf_box")
        self.horizontalLayout.addWidget(self.bookshelf_box)
        self.widget1 = QtWidgets.QWidget(delete_shelf)
        self.widget1.setGeometry(QtCore.QRect(10, 90, 381, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.shelf_box = QtWidgets.QComboBox(self.widget1)
        self.shelf_box.setObjectName("shelf_box")
        self.horizontalLayout_2.addWidget(self.shelf_box)
        self.widget2 = QtWidgets.QWidget(delete_shelf)
        self.widget2.setGeometry(QtCore.QRect(220, 160, 168, 31))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cancel_btn = QtWidgets.QPushButton(self.widget2)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_3.addWidget(self.cancel_btn)
        self.ok_btn = QtWidgets.QPushButton(self.widget2)
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout_3.addWidget(self.ok_btn)

        self.retranslateUi(delete_shelf)
        QtCore.QMetaObject.connectSlotsByName(delete_shelf)

    def retranslateUi(self, delete_shelf):
        _translate = QtCore.QCoreApplication.translate
        delete_shelf.setWindowTitle(_translate("delete_shelf", "Dialog"))
        self.label.setText(_translate("delete_shelf", "Удалить шкаф/полку"))
        self.error_label.setText(_translate("delete_shelf", "  "))
        self.label_2.setText(_translate("delete_shelf", "Выберите шкаф:"))
        self.label_3.setText(_translate("delete_shelf", "Выберите полку:"))
        self.cancel_btn.setText(_translate("delete_shelf", "Отмена"))
        self.ok_btn.setText(_translate("delete_shelf", "ОК"))


class DeleteShelf(QDialog, Ui_delete_shelf):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ok_btn.clicked.connect(self.run)
        self.cancel_btn.clicked.connect(self.cancel)
        self.bookshelf_box.addItems(all_bookshelves())
        self.bookshelf_box.currentTextChanged.connect(self.load)

    def load(self, name):
        self.shelf_box.clear()
        self.shelf_box.addItems(all_shelves(get_storage_id(name)))

    def setMainWin(self, win):
        self.mainWin = win

    def run(self):
        self.shelf_name = self.shelf_box.currentText()
        if not self.shelf_name:
            delete_storage(self.bookshelf_box.currentText())
            self.mainWin.loadTable()
            self.close()
        elif all_books_on_shelf(get_storage_id(self.bookshelf_box.currentText(), self.shelf_box.currentText())):
            self.error_label.setText('Ошибка! Удалите книги с полки перед её удалением.')
        else:
            delete_storage(self.bookshelf_box.currentText(), self.shelf_box.currentText())
            self.mainWin.loadTable()
            self.close()

    def cancel(self):
        self.mainWin.loadTable()
        self.close()


class Ui_Dialog1(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(482, 372)
        Dialog.setModal(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 10, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 50, 461, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.bookname_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.bookname_line.setObjectName("bookname_line")
        self.horizontalLayout.addWidget(self.bookname_line)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 100, 461, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.author_box = QtWidgets.QComboBox(self.layoutWidget1)
        self.author_box.setObjectName("author_box")
        self.horizontalLayout_2.addWidget(self.author_box)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.author_line = QtWidgets.QLineEdit(self.layoutWidget1)
        self.author_line.setObjectName("author_line")
        self.horizontalLayout_2.addWidget(self.author_line)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 150, 461, 41))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.genre_box = QtWidgets.QComboBox(self.layoutWidget2)
        self.genre_box.setObjectName("genre_box")
        self.horizontalLayout_3.addWidget(self.genre_box)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.genre_line = QtWidgets.QLineEdit(self.layoutWidget2)
        self.genre_line.setObjectName("genre_line")
        self.horizontalLayout_3.addWidget(self.genre_line)
        self.layoutWidget3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget3.setGeometry(QtCore.QRect(270, 320, 201, 51))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cancel_btn = QtWidgets.QPushButton(self.layoutWidget3)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_4.addWidget(self.cancel_btn)
        self.ok_btn = QtWidgets.QPushButton(self.layoutWidget3)
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout_4.addWidget(self.ok_btn)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 200, 461, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.bookshelf_box = QtWidgets.QComboBox(self.layoutWidget_2)
        self.bookshelf_box.setObjectName("bookshelf_box")
        self.horizontalLayout_5.addWidget(self.bookshelf_box)
        self.layoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 250, 461, 41))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.shelf_box = QtWidgets.QComboBox(self.layoutWidget_3)
        self.shelf_box.setObjectName("shelf_box")
        self.horizontalLayout_6.addWidget(self.shelf_box)
        self.error_label = QtWidgets.QLabel(Dialog)
        self.error_label.setGeometry(QtCore.QRect(10, 300, 461, 17))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Информация о книге"))
        self.label_2.setText(_translate("Dialog", "Название:"))
        self.label_3.setText(_translate("Dialog", "Автор:"))
        self.label_5.setText(_translate("Dialog", "Другой:"))
        self.label_4.setText(_translate("Dialog", "Жанр"))
        self.label_6.setText(_translate("Dialog", "Другой:"))
        self.cancel_btn.setText(_translate("Dialog", "Отмена"))
        self.ok_btn.setText(_translate("Dialog", "ОК"))
        self.label_7.setText(_translate("Dialog", "Выбрать шкаф:"))
        self.label_8.setText(_translate("Dialog", "Выбрать полку:"))


class AddNewBook(QDialog, Ui_Dialog1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.author_box.addItems(all_authors())
        self.genre_box.addItems(all_genres())
        self.bookshelf_box.addItems(all_bookshelves())
        self.bookshelf_box.currentTextChanged.connect(self.load)
        self.ok_btn.clicked.connect(self.run)
        self.cancel_btn.clicked.connect(self.cancel)

    def setMainWin(self, win):
        self.mainWin = win

    def load(self, name):
        self.shelf_box.clear()
        self.shelf_box.addItems(all_shelves(get_storage_id(name)))

    def run(self):
        self.book_name = self.bookname_line.text()
        self.author_name1 = self.author_box.currentText()
        self.author_name2 = self.author_line.text()
        self.genre1 = self.genre_box.currentText()
        self.genre2 = self.genre_line.text()
        self.shelf = self.shelf_box.currentText()
        if not self.book_name:
            self.error_label.setText('Ошибка! Введите название книги.')
        elif not self.shelf:
            self.error_label.setText('Ошибка! Выберите полку.')
        else:
            self.author, self.genre = test_data(self.author_name1, self.author_name2, self.genre1, self.genre2)
            self.book_shelf = self.bookshelf_box.currentText()
            add_book(self.book_name, self.author, self.genre, self.book_shelf, self.shelf)
            self.mainWin.loadTable()
            self.close()

    def cancel(self):
        self.mainWin.loadTable()
        self.close()


class Ui_Deletebook(object):
    def setupUi(self, Deleteshelf):
        Deleteshelf.setObjectName("Deleteshelf")
        Deleteshelf.resize(400, 240)
        self.label = QtWidgets.QLabel(Deleteshelf)
        self.label.setGeometry(QtCore.QRect(120, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.error_label = QtWidgets.QLabel(Deleteshelf)
        self.error_label.setGeometry(QtCore.QRect(10, 170, 381, 17))
        self.error_label.setObjectName("error_label")
        self.widget = QtWidgets.QWidget(Deleteshelf)
        self.widget.setGeometry(QtCore.QRect(10, 50, 381, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.bookshelf_box = QtWidgets.QComboBox(self.widget)
        self.bookshelf_box.setObjectName("bookshelf_box")
        self.horizontalLayout.addWidget(self.bookshelf_box)
        self.widget1 = QtWidgets.QWidget(Deleteshelf)
        self.widget1.setGeometry(QtCore.QRect(10, 90, 381, 27))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.shelf_box = QtWidgets.QComboBox(self.widget1)
        self.shelf_box.setObjectName("shelf_box")
        self.horizontalLayout_2.addWidget(self.shelf_box)
        self.widget2 = QtWidgets.QWidget(Deleteshelf)
        self.widget2.setGeometry(QtCore.QRect(10, 130, 381, 27))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.book_box = QtWidgets.QComboBox(self.widget2)
        self.book_box.setObjectName("book_box")
        self.horizontalLayout_3.addWidget(self.book_box)
        self.widget3 = QtWidgets.QWidget(Deleteshelf)
        self.widget3.setGeometry(QtCore.QRect(220, 190, 168, 41))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cancel_btn = QtWidgets.QPushButton(self.widget3)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_4.addWidget(self.cancel_btn)
        self.ok_btn = QtWidgets.QPushButton(self.widget3)
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout_4.addWidget(self.ok_btn)

        self.retranslateUi(Deleteshelf)
        QtCore.QMetaObject.connectSlotsByName(Deleteshelf)

    def retranslateUi(self, Deleteshelf):
        _translate = QtCore.QCoreApplication.translate
        Deleteshelf.setWindowTitle(_translate("Deleteshelf", "Dialog"))
        self.label.setText(_translate("Deleteshelf", "Удалить книгу"))
        self.error_label.setText(_translate("Deleteshelf", "  "))
        self.label_2.setText(_translate("Deleteshelf", "Выберите шкаф"))
        self.label_3.setText(_translate("Deleteshelf", "Выберите полку"))
        self.label_4.setText(_translate("Deleteshelf", "Выберите книгу"))
        self.cancel_btn.setText(_translate("Deleteshelf", "Отмена"))
        self.ok_btn.setText(_translate("Deleteshelf", "ОК"))


class DeleteBook(QDialog, Ui_Deletebook):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ok_btn.clicked.connect(self.run)
        self.cancel_btn.clicked.connect(self.cancel)
        self.bookshelf_box.addItems(all_bookshelves())
        self.bookshelf_box.currentTextChanged.connect(self.load_shelves)
        self.shelf_box.currentTextChanged.connect(self.load_books)

    def load_shelves(self, name):
        self.shelf_box.clear()
        self.shelf_box.addItems(all_shelves(get_storage_id(name)))

    def load_books(self):
        self.book_box.clear()
        self.shelf_id = get_storage_id(self.bookshelf_box.currentText(), self.shelf_box.currentText())
        self.book_box.addItems(all_books_on_shelf(self.shelf_id))

    def setMainWin(self, win):
        self.mainWin = win

    def run(self):
        self.bs_name = self.bookshelf_box.currentText()
        self.s_name = self.shelf_box.currentText()
        self.book_name = self.book_box.currentText()
        self.s_id = get_storage_id(self.bs_name, self.s_name)
        delete_book(self.book_name, self.s_id)
        self.mainWin.loadTable()
        self.close()

    def cancel(self):
        self.mainWin.loadTable()
        self.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HomeWindow()
    ex.show()
    sys.exit(app.exec_())