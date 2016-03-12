import os
import public
import pickle

attributeList = [
    ("index", "学号"),
    ("name", "姓名"),
    ("sex", "性别"),
    ("birth", "出生日期"),
    ("major", "专业"),
    ("grade", "年级"),
    ("classname", "班级"),
]


class StudentManager(object):
    """学生管理类, 单例"""

    def __init__(self, path=None):
        # 用于存储所有学生对象
        self.studentList = []
        # 学号 -> 学生对象
        self.studentIndex = {}

        self.load(path)

        self.emptyStudent = Student()

    def add(self, student):
        self.studentList.append(student)
        self.studentIndex[student.index] = student

    def delete(self, student):
        if isinstance(student, Student):
            pass
        elif isinstance(student, int) and student in self.studenIndex:
            student = self.studentIndex[student]
        else:
            return False

        self.studentIndex.pop(student.index)
        self.studentList.remove(student)
        return True

    def multiSearch(self, keyList):
        result = self.studentList.copy()
        for searchBy, keyText in keyList:
            if keyText:
                result = self.search(searchBy, keyText, result)
        return result

    def search(self, searchBy, keyList, searchList=None):
        result = []
        searchList = searchList or self.studentList
        if not keyList:
            return searchList.copy()
        else:
            keyList = keyList.split()
            if len(keyList) > 1:
                [keyList.pop(i) if not i else None for i in keyList]
            for student in searchList:
                target = getattr(student, searchBy)
                for key in keyList:
                    if key in target:
                        result.append(student)
                        break
            return result

    def exportAsExcel(self, path, studentList=None):
        studentList = studentList or self.studentList
        import xlwt
        xls = xlwt.Workbook(encoding='utf-8')
        xlss = xls.add_sheet("学生学籍档案")
        attrs = []
        width = [100, 80, 50, 100, 200, 80, 80]
        for header in range(0, len(attributeList)):
            xlss.write(0, header, attributeList[header][1])
            xlss.col(header).width = width[header] * 256 // 9
            attrs.append(attributeList[header][0])
        for row in range(0, len(studentList)):
            student = studentList[row]
            for column in range(0, len(attrs)):
                if column == 2:
                    value = student.getSex()
                else:
                    value = getattr(student, attrs[column])
                xlss.write(row + 1, column, value)
        xls.save(path)

    def save(self, path=None):
        path = path or self.path
        f = None
        try:
            f = open(path, 'wb')
            pickle.dump(self.studentList, f)
            pickle.dump(self.studentIndex, f)
            result = True
        except:
            result = False
        finally:
            if f:
                f.close()
            return result

    def load(self, path=None):
        path = path or public.defaultDataPath
        self.path = path
        f = None
        try:
            f = open(path, 'rb')
            studentList = pickle.load(f)
            studentIndex = pickle.load(f)
            result = True
        except:
            result = False
            studentList = []
            studentIndex = {}
        finally:
            if f:
                f.close()
            self.studentList = studentList
            self.studentIndex = studentIndex
        return result


class Student(object):
    """学生类, 用于存储学生基本信息"""

    def __init__(self, index="", name="", sex=0, birth="", major="", grade="", classname=""):
        self.index = index
        self.name = name
        self.sex = sex
        self.birth = birth
        self.major = major
        self.grade = grade
        self.classname = classname

    def getSex(self):
        return ["", "男", "女"][self.sex]

    def copy(self):
        student = Student()
        self.copyTo(student)
        return student

    def copyTo(self, student):
        student.index = self.index
        student.name = self.name
        student.sex = self.sex
        student.birth = self.birth
        student.major = self.major
        student.grade = self.grade
        student.classname = self.classname

    def checkInfo(self, new=False):
        '''检查自身信息是否完整合法'''
        # 空值检测
        for attr, text in attributeList:
            if not getattr(self, attr):
                return (False, "%s不能为空" % text)
        # 重复性检测
        if new and self.index in public.studentManager.studentIndex:
            return (False, "学号重复")

        return (True, "")
