from PyQt5 import QtWidgets, QtCore
from _studentBox import Ui_StudentBox

from student import Student


class StudentBox(object):
    """学生信息编辑盒 - 基类"""

    def __init__(self):

        self.dialog = QtWidgets.QDialog()
        window = Ui_StudentBox()
        window.setupUi(self.dialog)

        self.dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        self.indexEdit = window.indexEdit
        self.nameEdit = window.nameEdit
        self.birthEdit = window.birthEdit
        self.majorEdit = window.majorEdit
        self.gradeEdit = window.gradeEdit
        self.classEdit = window.classEdit

        self.msgLabel = window.msg

        self.okButton = window.okButton
        self.cancelButton = window.cancelButton
        self.okButton.clicked.connect(self.onOkButtonClicked)
        self.cancelButton.clicked.connect(self.dialog.close)

        self.maleButton = window.maleButton
        self.famaleButton = window.famaleButton

    def getSex(self):
        if self.maleButton.isChecked():
            return 1
        elif self.famaleButton.isChecked():
            return 2
        else:
            return 0

    def setSex(self, value):
        if value == 1:
            self.maleButton.setChecked(True)
        elif value == 2:
            self.famaleButton.setChecked(True)

    def onOkButtonClicked(self):
        if self.onFinished():
            self.dialog.close()

    def show(self):
        self.dialog.show()

    def setTitle(self, title):
        self.dialog.setWindowTitle(title)

    def setMsg(self, text):
        self.msgLabel.setText(text)

    def setButton(self, ok, cancel=None):
        self.okButton.setText(ok)
        self.cancelButton.setText(cancel) if cancel is not None else None

    def applyToStudent(self, student):
        student.index = self.indexEdit.text()
        student.name = self.nameEdit.text()
        student.sex = self.getSex()
        student.birth = self.birthEdit.text()
        student.major = self.majorEdit.text()
        student.grade = self.gradeEdit.text()
        student.classname = self.classEdit.text()

    def onFinished(self):
        return False


class EditBox(StudentBox):
    """编辑学生信息 - 继承StudentBox"""

    def __init__(self, student, callback):
        super(EditBox, self).__init__()
        self.callback = callback

        self.setTitle("修改信息...")
        self.setMsg("")
        self.setButton("修改")

        self.indexEdit.setText(student.index)
        self.nameEdit.setText(student.name)
        self.setSex(student.sex)
        self.birthEdit.setText(student.birth)
        self.majorEdit.setText(student.major)
        self.gradeEdit.setText(student.grade)
        self.classEdit.setText(student.classname)

        self._student = Student()

    def onFinished(self):
        self.applyToStudent(self._student)
        check, info = self._student.checkInfo()
        if check:
            self.callback(self._student)
        else:
            self.setMsg(info)
        return check


class NewBox(StudentBox):
    """新建学生档案 - 继承StudentBox"""

    def __init__(self, callback):
        super(NewBox, self).__init__()
        self.callback = callback

        self.setTitle("新建档案...")
        self.setMsg("")
        self.setButton("新建")

        self.student = Student()

    def onFinished(self):
        student = self.student
        self.applyToStudent(student)
        check, info = student.checkInfo(True)
        self.callback(self.student) if check else self.setMsg(info)
        return check


class SearchBox(StudentBox):
    """高级搜索框 - 继承StudentBox"""

    def __init__(self, callback):
        super(SearchBox, self).__init__()
        self.callback = callback

        self.setTitle("高级搜索...")
        self.setMsg("请输入关键词, 多个条件用空格分隔")
        self.setButton("搜索")

        self.maleButton.setEnabled(False)
        self.famaleButton.setEnabled(False)

    def onFinished(self):
        keyList = [
            ("index", ' '.join(self.indexEdit.text().split())),
            ("name", ' '.join(self.nameEdit.text().split())),
            ("birth", ' '.join(self.birthEdit.text().split())),
            ("major", ' '.join(self.majorEdit.text().split())),
            ("grade", ' '.join(self.gradeEdit.text().split())),
            ("classname", ' '.join(self.classEdit.text().split()))
        ]
        self.callback(keyList)
        return True
