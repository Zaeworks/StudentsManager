# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 582)
        MainWindow.setStyleSheet("#MainWindow{background-color: rgb(255, 255, 255)}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(650, 10, 121, 31))
        self.searchButton.setObjectName("searchButton")
        self.searchBox = QtWidgets.QComboBox(self.centralwidget)
        self.searchBox.setGeometry(QtCore.QRect(550, 10, 91, 31))
        self.searchBox.setWhatsThis("")
        self.searchBox.setObjectName("searchBox")
        self.searchBox.addItem("")
        self.searchBox.addItem("")
        self.searchBox.addItem("")
        self.searchBox.addItem("")
        self.searchBox.addItem("")
        self.searchBox.addItem("")
        self.searchBox.addItem("")
        self.searchEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchEdit.setGeometry(QtCore.QRect(10, 10, 541, 31))
        self.searchEdit.setObjectName("searchEdit")
        self.studentTable = QtWidgets.QTreeWidget(self.centralwidget)
        self.studentTable.setGeometry(QtCore.QRect(10, 50, 761, 481))
        self.studentTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.studentTable.setObjectName("studentTable")
        self.studentTable.header().setVisible(True)
        self.studentTable.header().setSortIndicatorShown(True)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(790, 50, 201, 321))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 72, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 230, 72, 15))
        self.label_6.setObjectName("label_6")
        self.indexLabel = QtWidgets.QLabel(self.groupBox)
        self.indexLabel.setGeometry(QtCore.QRect(100, 50, 91, 16))
        self.indexLabel.setText("")
        self.indexLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.indexLabel.setObjectName("indexLabel")
        self.nameLabel = QtWidgets.QLabel(self.groupBox)
        self.nameLabel.setGeometry(QtCore.QRect(100, 80, 91, 16))
        self.nameLabel.setText("")
        self.nameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.birthLabel = QtWidgets.QLabel(self.groupBox)
        self.birthLabel.setGeometry(QtCore.QRect(100, 140, 91, 16))
        self.birthLabel.setText("")
        self.birthLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.birthLabel.setObjectName("birthLabel")
        self.majorLabel = QtWidgets.QLabel(self.groupBox)
        self.majorLabel.setGeometry(QtCore.QRect(100, 170, 91, 16))
        self.majorLabel.setText("")
        self.majorLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.majorLabel.setObjectName("majorLabel")
        self.gradeLabel = QtWidgets.QLabel(self.groupBox)
        self.gradeLabel.setGeometry(QtCore.QRect(100, 200, 91, 16))
        self.gradeLabel.setText("")
        self.gradeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gradeLabel.setObjectName("gradeLabel")
        self.classLabel = QtWidgets.QLabel(self.groupBox)
        self.classLabel.setGeometry(QtCore.QRect(100, 230, 91, 16))
        self.classLabel.setText("")
        self.classLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.classLabel.setObjectName("classLabel")
        self.editButton = QtWidgets.QPushButton(self.groupBox)
        self.editButton.setGeometry(QtCore.QRect(10, 260, 81, 31))
        self.editButton.setObjectName("editButton")
        self.DeleteButton = QtWidgets.QPushButton(self.groupBox)
        self.DeleteButton.setGeometry(QtCore.QRect(110, 260, 81, 31))
        self.DeleteButton.setObjectName("DeleteButton")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 110, 72, 16))
        self.label_7.setObjectName("label_7")
        self.sexLabel = QtWidgets.QLabel(self.groupBox)
        self.sexLabel.setGeometry(QtCore.QRect(100, 110, 91, 16))
        self.sexLabel.setText("")
        self.sexLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sexLabel.setObjectName("sexLabel")
        self.newButton = QtWidgets.QPushButton(self.centralwidget)
        self.newButton.setGeometry(QtCore.QRect(780, 500, 111, 31))
        self.newButton.setObjectName("newButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setToolTip("")
        self.statusbar.setStatusTip("")
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1010, 26))
        self.menubar.setObjectName("menubar")
        self.sysMenu = QtWidgets.QMenu(self.menubar)
        self.sysMenu.setObjectName("sysMenu")
        self.exportMenu = QtWidgets.QMenu(self.sysMenu)
        self.exportMenu.setToolTip("")
        self.exportMenu.setObjectName("exportMenu")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.helpMenu = QtWidgets.QMenu(self.menubar)
        self.helpMenu.setObjectName("helpMenu")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.exportSelected = QtWidgets.QAction(MainWindow)
        self.exportSelected.setObjectName("exportSelected")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionAdd = QtWidgets.QAction(MainWindow)
        self.actionAdd.setObjectName("actionAdd")
        self.actionSreach = QtWidgets.QAction(MainWindow)
        self.actionSreach.setObjectName("actionSreach")
        self.actionSelected = QtWidgets.QAction(MainWindow)
        self.actionSelected.setObjectName("actionSelected")
        self.actionResult = QtWidgets.QAction(MainWindow)
        self.actionResult.setObjectName("actionResult")
        self.actionAll = QtWidgets.QAction(MainWindow)
        self.actionAll.setObjectName("actionAll")
        self.actionUrl = QtWidgets.QAction(MainWindow)
        self.actionUrl.setObjectName("actionUrl")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.exportAll = QtWidgets.QAction(MainWindow)
        self.exportAll.setObjectName("exportAll")
        self.exportMenu.addAction(self.exportSelected)
        self.exportMenu.addAction(self.exportAll)
        self.sysMenu.addAction(self.actionSave)
        self.sysMenu.addAction(self.actionSaveAs)
        self.sysMenu.addSeparator()
        self.sysMenu.addAction(self.exportMenu.menuAction())
        self.sysMenu.addSeparator()
        self.sysMenu.addAction(self.actionExit)
        self.menu.addAction(self.actionAdd)
        self.menu.addSeparator()
        self.menu.addAction(self.actionSreach)
        self.menu.addAction(self.actionEdit)
        self.menu.addAction(self.actionDelete)
        self.helpMenu.addAction(self.actionUrl)
        self.helpMenu.addAction(self.actionAbout)
        self.menubar.addAction(self.sysMenu.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.helpMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生学籍管理系统"))
        self.searchButton.setStatusTip(_translate("MainWindow", "对多个属性进行检索"))
        self.searchButton.setText(_translate("MainWindow", "高级搜索..."))
        self.searchBox.setStatusTip(_translate("MainWindow", "快速检索项"))
        self.searchBox.setItemText(0, _translate("MainWindow", "学号"))
        self.searchBox.setItemText(1, _translate("MainWindow", "姓名"))
        self.searchBox.setItemText(2, _translate("MainWindow", "性别"))
        self.searchBox.setItemText(3, _translate("MainWindow", "出生日期"))
        self.searchBox.setItemText(4, _translate("MainWindow", "专业"))
        self.searchBox.setItemText(5, _translate("MainWindow", "年级"))
        self.searchBox.setItemText(6, _translate("MainWindow", "班级"))
        self.searchEdit.setStatusTip(_translate("MainWindow", "快速检索信息, 使用空格分隔多个条件"))
        self.studentTable.setStatusTip(_translate("MainWindow", "双击修改信息"))
        self.studentTable.setSortingEnabled(True)
        self.studentTable.headerItem().setText(0, _translate("MainWindow", "学号"))
        self.studentTable.headerItem().setText(1, _translate("MainWindow", "姓名"))
        self.studentTable.headerItem().setText(2, _translate("MainWindow", "性别"))
        self.studentTable.headerItem().setText(3, _translate("MainWindow", "出生日期"))
        self.studentTable.headerItem().setText(4, _translate("MainWindow", "专业"))
        self.studentTable.headerItem().setText(5, _translate("MainWindow", "年级"))
        self.studentTable.headerItem().setText(6, _translate("MainWindow", "班级"))
        self.groupBox.setTitle(_translate("MainWindow", "学生信息"))
        self.label.setText(_translate("MainWindow", "学号"))
        self.label_2.setText(_translate("MainWindow", "姓名"))
        self.label_3.setText(_translate("MainWindow", "出生日期"))
        self.label_4.setText(_translate("MainWindow", "专业"))
        self.label_5.setText(_translate("MainWindow", "年级"))
        self.label_6.setText(_translate("MainWindow", "班级"))
        self.editButton.setStatusTip(_translate("MainWindow", "修改当前学生信息"))
        self.editButton.setText(_translate("MainWindow", "修改..."))
        self.DeleteButton.setStatusTip(_translate("MainWindow", "删除档案, 一旦删除数据不可恢复"))
        self.DeleteButton.setText(_translate("MainWindow", "删除"))
        self.label_7.setText(_translate("MainWindow", "性别"))
        self.newButton.setStatusTip(_translate("MainWindow", "新建学生学籍档案"))
        self.newButton.setText(_translate("MainWindow", "新建档案..."))
        self.sysMenu.setTitle(_translate("MainWindow", "系统"))
        self.exportMenu.setStatusTip(_translate("MainWindow", "转换数据为Excel格式"))
        self.exportMenu.setTitle(_translate("MainWindow", "导出至Excel"))
        self.menu.setTitle(_translate("MainWindow", "学籍"))
        self.helpMenu.setTitle(_translate("MainWindow", "帮助"))
        self.action.setText(_translate("MainWindow", "\\"))
        self.actionSave.setText(_translate("MainWindow", "保存学籍表"))
        self.actionSave.setToolTip(_translate("MainWindow", "保存学籍表"))
        self.actionSave.setStatusTip(_translate("MainWindow", "保存学籍表(系统退出时会自动保存)"))
        self.actionSaveAs.setText(_translate("MainWindow", "另存学籍表..."))
        self.actionSaveAs.setStatusTip(_translate("MainWindow", "保存一份副本"))
        self.exportSelected.setText(_translate("MainWindow", "选中档案..."))
        self.exportSelected.setStatusTip(_translate("MainWindow", "导出当前列表中的档案"))
        self.actionEdit.setText(_translate("MainWindow", "修改"))
        self.actionEdit.setStatusTip(_translate("MainWindow", "修改当前学生信息"))
        self.actionDelete.setText(_translate("MainWindow", "删除"))
        self.actionDelete.setStatusTip(_translate("MainWindow", "删除档案, 一旦删除数据不可恢复"))
        self.actionAdd.setText(_translate("MainWindow", "新建档案..."))
        self.actionAdd.setStatusTip(_translate("MainWindow", "新建学生学籍档案"))
        self.actionSreach.setText(_translate("MainWindow", "搜索"))
        self.actionSreach.setStatusTip(_translate("MainWindow", "对多个属性进行检索"))
        self.actionSelected.setText(_translate("MainWindow", "选中档案..."))
        self.actionResult.setText(_translate("MainWindow", "列表内档案..."))
        self.actionAll.setText(_translate("MainWindow", "所有档案..."))
        self.actionUrl.setText(_translate("MainWindow", "访问网站"))
        self.actionUrl.setStatusTip(_translate("MainWindow", "访问项目Github页面"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))
        self.actionAbout.setStatusTip(_translate("MainWindow", "关于系统"))
        self.actionExit.setText(_translate("MainWindow", "退出系统"))
        self.actionExit.setStatusTip(_translate("MainWindow", "退出学生学籍管理系统"))
        self.exportAll.setText(_translate("MainWindow", "所有档案..."))
        self.exportAll.setStatusTip(_translate("MainWindow", "导出整个学籍表"))

