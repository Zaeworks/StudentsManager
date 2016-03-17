from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
from functools import partial
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

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dialog.setWindowIcon(icon)

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

        self.studentTable = window.studentTable
        self.tableList = []  # Student
        self.tableIndex = {}  # Student -> Item
        self.studentTable.itemSelectionChanged.connect(self.onSelectStudent)
        self.studentTable.activated.connect(self.onEdit)

        width = [125, 82, 50, 100, 202, 87, 113]
        [self.studentTable.setColumnWidth(i, width[i]) for i in range(7)]

        # 视图
        self.viewMenu = window.viewMenu
        from student import attributeList as attrs
        for i in range(0, len(attrs)):
            action = QtWidgets.QAction(attrs[i][1], self.dialog)
            action.setCheckable(True)
            action.setChecked(True)
            self.viewMenu.addAction(action)
            action.triggered.connect(partial(self.onSetView, i))

        self.searchMode = 0  # 0不搜索 1快速搜索 2高级搜索

        window.exportSelected.triggered.connect(partial(self.onExport, True))
        window.exportAll.triggered.connect(partial(self.onExport, False))

        self.dialog.closeEvent = self.onQuit
        window.actionSave.triggered.connect(public.studentManager.save)
        window.actionSaveAs.triggered.connect(self.onSaveAs)

        window.actionExit.triggered.connect(self.dialog.close)
        window.actionUrl.triggered.connect(self.onVisitWeb)
        window.actionAbout.triggered.connect(self.onAbout)

        window.searchBox.currentTextChanged['QString'].connect(self.onSearchBy)

        self.onSearchBy("学号")

    def onAbout(self):
        import version
        QMessageBox.information(QtWidgets.QDialog(), "关于", '\n'.join([
            "学生学籍管理系统 Build %03d" % version.build,
            "扎易作品@Zaeworks\n",
            "本作品仅供学习交流使用, 禁止用于商业用途!"
        ]))

    def onVisitWeb(self):
        import webbrowser
        webbrowser.open("https://github.com/Zaeworks/StudentsManager")

    def onSaveAs(self):
        path, ok = QFileDialog.getSaveFileName(
            self.dialog, "另存学籍表", "C:/", "学生档案文件(*.stu)")
        if not path:
            return
        public.studentManager.save(path)

    def onExport(self, part):
        name = "导出选中档案..." if part else "导出所有档案..."
        path, ok = QFileDialog.getSaveFileName(
            self.dialog, name, "C:/", "Excel表格(*.xls)")
        if not path:
            return
        studentList = self.tableList.copy() if part else None
        public.studentManager.exportAsExcel(path, studentList)

    def onSetView(self, index, checked):
        self.studentTable.setColumnHidden(index, not checked)

    def onQuit(self, _):
        public.studentManager.save()

    def onSearchBy(self, searchBy):
        from student import attributeList as attrs
        for attr, translate in attrs:
            if searchBy == translate:
                self.quickSearchBy = attr
        self.onQuickSearch()

    def onQuickSearch(self):
        key = self.searchEdit.text()
        key = ' '.join(key.split())
        result = public.studentManager.search(self.quickSearchBy, key)
        self.tableShow(result)

    def onSearch(self):
        def _onSaerch(keyList):
            result = public.studentManager.multiSearch(keyList)
            self.tableShow(result)
        self._saerchBox = boxUI.SearchBox(_onSaerch)
        self._saerchBox.show()

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
        confirm = QMessageBox.warning(QtWidgets.QWidget(),
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

        def _onEdit(_student):
            if _student.index != student.index:
                public.studentManager.delete(student)
                _student.copyTo(student)
                public.studentManager.add(student)
            else:
                _student.copyTo(student)
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
