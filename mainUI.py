from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from _mainUI import Ui_MainWindow
import boxUI
import public


class MainWindow(object):
    """主窗口封装类"""

    def __init__(self):

        self.dialog = QtWidgets.QMainWindow()
        window = Ui_MainWindow()
        window.setupUi(self.dialog)
        self.dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        self.indexLabel = window.indexLabel
        self.nameLabel = window.nameLabel
        self.sexLabel = window.sexLabel
        self.birthLabel = window.birthLabel
        self.majorLabel = window.majorLabel
        self.gradeLabel = window.gradeLabel
        self.classLabel = window.classLabel

        self.actionSearch = window.actionSreach
        self.searchButton = window.searchButton
        self.actionSearch.triggered.connect(self.onSearch)
        self.searchButton.clicked.connect(self.onSearch)

        self.newButtton = window.newButton
        self.actionAdd = window.actionAdd
        self.newButtton.clicked.connect(self.onAddStudent)
        self.actionAdd.triggered.connect(self.onAddStudent)

        self.searchEdit = window.searchEdit
        self.searchEdit.textChanged['QString'].connect(self.onQuickSearch)

        self.editButton = window.editButton
        self.actionEdit = window.actionEdit
        self.editButton.clicked.connect(self.onEdit)
        self.actionEdit.triggered.connect(self.onEdit)

        self.deleteButton = window.DeleteButton
        self.actionDelete = window.actionDelete
        self.deleteButton.clicked.connect(self.onDelete)
        self.actionDelete.triggered.connect(self.onDelete)

        # 视图
        self.viewMenu = window.viewMenu
        from student import attributeList as attrs
        for i in range(0, len(attrs)):
            action = QtWidgets.QAction(attrs[i][1], self.dialog)
            action.setCheckable(True)
            action.setChecked(True)
            self.viewMenu.addAction(action)

        self.studentTable = window.studentTable
        self.tableList = []  # Student
        self.tableIndex = {}  # Student -> Item
        self.studentTable.itemSelectionChanged.connect(self.onSelectStudent)
        self.studentTable.activated.connect(self.onEdit)

        self.searchMode = 0  # 0不搜索 1快速搜索 2高级搜索

        self.dialog.closeEvent = self.onQuit

    def onQuickSearch(self):
        key = self.searchEdit.text()
        key = ' '.join(key.split())

    def onQuit(self, _):
        public.studentManager.save()

    def onSearch(self):
        print("onSearch!")

    def onAddStudent(self):
        def _onAddStudent(_student):
            student = _student.copy()
            public.studentManager.add(student)
            self.tableSet(student)
        self._newBox = boxUI.NewBox(_onAddStudent)
        self._newBox.show()

    def onDelete(self):
        student = self.selection
        if not student:
            return
        confirm = QMessageBox.information(QtWidgets.QWidget(),
                                          "删除档案", "确认删除此档案?",
                                          QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            item = self.tableIndex[student]
            n = self.studentTable.topLevelItemCount()
            for i in range(0, n):
                if self.studentTable.topLevelItem(i) == item:
                    self.studentTable.takeTopLevelItem(i)
                    self.tableList.remove(student)
                    self.tableIndex.pop(student)
                    break
            public.studentManager.delete(student)

    def onEdit(self):
        student = self.selection
        if not student:
            return

        def _onEdit(student):
            if student in self.tableIndex:
                self.tableSet(student, self.tableIndex[student])
        self._editBox = boxUI.EditBox(student, _onEdit)
        self._editBox.show()

    def setStudentInfo(self, student=None):
        student = student or public.studentManager.emptyStudent
        self.indexLabel.setText(student.index)
        self.nameLabel.setText(student.name)
        self.sexLabel.setText(student.getSex())
        self.birthLabel.setText(student.birth)
        self.majorLabel.setText(student.major)
        self.gradeLabel.setText(student.grade)
        self.classLabel.setText(student.classname)

    def show(self):
        self.dialog.show()

    def tableShow(self, studentList):
        self.tableClear()
        for student in studentList:
            self.tableAdd(student)
        self.onSelectStudent()

    def tableAdd(self, student):
        item = QtWidgets.QTreeWidgetItem(self.studentTable)
        self.tableSet(student, item)
        self.tableList.append(student)
        self.tableIndex[student] = item

    def tableSet(self, student, item=None):
        if item:
            item.setText(0, student.index)
            item.setText(1, student.name)
            item.setText(2, student.getSex())
            item.setText(3, student.birth)
            item.setText(4, student.major)
            item.setText(5, student.grade)
            item.setText(6, student.classname)
        elif self.searchMode == 0:
            self.tableAdd(student)

    def tableClear(self):
        self.studentTable.clear()
        self.tableList.clear()
        self.tableIndex.clear()

    def tableUpdate(self):
        pass

    def onSelectStudent(self):
        item = self.studentTable.selectedItems()
        selected = True if item else False
        selection = None
        if selected:
            for k, v in self.tableIndex.items():
                if v == item[0]:
                    selection = k
                    break
            else:
                selected = False
        self.selection = selection
        self.setStudentInfo(selection)
        self.editButton.setEnabled(selected)
        self.actionEdit.setEnabled(selected)
        self.deleteButton.setEnabled(selected)
        self.actionDelete.setEnabled(selected)
