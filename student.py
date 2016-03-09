import os
import public
import pickle

attributeList = [
    ("index", "学号"),
    ("name", "姓名"),
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

    def new(self, index, name, birth, major, grade, classname):
        if index in self.studentIndex:
            return False
        student = Student(index, name, birth, major, grade, classname)
        self.studentList.append(student)
        self.studenIndex[index] = student
        return True

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
        if searchBy in ["index", "name", "birth", "major", "grade", "classname"]:
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

    def export(self, path):
        pass

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

    def __init__(self, index="", name="", birth="", major="", grade="", classname=""):
        self.index = index
        self.name = name
        self.birth = birth
        self.major = major
        self.grade = grade
        self.classname = classname

    def copy(self):
        student = Student()
        self.copyTo(student)
        return student

    def copyTo(self, student):
        student.index = self.index
        student.name = self.name
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
