from PyQt5 import QtWidgets, QtCore
from _mainUI import Ui_MainWindow
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
        self.birthLabel = window.birthLabel
        self.majorLabel = window.majorLabel
        self.gradeLabel = window.gradeLabel
        self.classLabel = window.classLabel

        self.statusBar = window.statusbar

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

        self.studentTable = window.studentTable
        self.tableList = []  # Student
        self.tableIndex = {}  # Student -> Item

        self.searchMode = 0  # 0不搜索 1快速搜索 2高级搜索

    def onQuickSearch(self):
        key = self.searchEdit.text()
        key = ' '.join(key.split())

    def onSearch(self):
        print("onSearch!")

    def onAddStudent(self):
        print("onAddStudent!")

    def onDelete(self):
        print("onDelete!")

    def onEdit(self):
        print("onEdit!")

    def setStudentInfo(self, student=None):
        student = student or public.studentManager.emptyStudent
        self.indexLabel.setText(student.index)
        self.nameLabel.setText(student.name)
        self.birthLabel.setText(student.birth)
        self.majorLabel.setText(student.major)
        self.gradeLabel.setText(student.grade)
        self.classLabel.setText(student.classname)

    def show(self):
        self.dialog.show()

    def tableShow(self, studentList):
        pass

    def tableAdd(self, student):
        item = QtWidgets.QTreeWidgetItem(self.studentTable)
        self.tableSet(student, item)
        self.tableList.append(item)
        self.tableIndex[student] = item

    def tableSet(self, student, item=None):
        if item:
            item.setText(0, student.index)
            item.setText(1, student.name)
            item.setText(2, student.birth)
            item.setText(3, student.major)
            item.setText(4, student.grade)
            item.setText(5, student.classname)
        elif self.searchMode == 0:
            self.tableAdd(student)

    def tableClear(self):
        self.studentTable.clear()
        self.tableList.clear()
        self.tableIndex.clear()

    def tableUpdate(self):
        pass

    def onSelectStudent(self):
        item = self.searchList.selectedItems()
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
