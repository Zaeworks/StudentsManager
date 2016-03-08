
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

    def __init__(self):
        # 用于存储所有学生对象
        self.studentList = []
        # 学号 -> 学生对象
        self.studentIndex = {}


class Student(object):
    """学生类, 用于存储操作"""

    def __init__(self):
        self.index = 0
        self.name = ""
        self.birth = ""
        self.major = ""
        self.grade = 0
        self.classname = ""
