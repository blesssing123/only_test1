class School:
    def __init__(self, name, address):  # 建立学校
        self.name = name
        self.address = address
        self.number_of_people = 0
        self.__balance = 0
        self.staff_list = []
        self.s_student_list = []
        print(f'初始化校区[{self.name}],地址:{self.address}...')

    def pay_salary(self, staff_obj):  # 支付工资
        self.__balance -= int(staff_obj.salary)
        print(self.name + "向" + staff_obj.name + "支付了工资" + staff_obj.salary)

    def count_staff_num(self):  # 统计学校员工数
        print(f"[{self.name}]的总员工数:{len(self.staff_list)}")

    def count_student_num(self):  # 统计学习学生数
        print(f"校区[{self.name}]的学生总数:{len(self.s_student_list)}")

    def new_staff(self, staff_obj, time):  # 新员工入职
        print(
            f"校区【{self.name}】的【{staff_obj.dept}部门】在【{time}】入职了一名新同事【{staff_obj.name}】,职位是【{staff_obj.position}】")
        self.staff_list.append(staff_obj)

    def new_class(self, class_name, time):  # 学校开设新班级
        print(f"校区[{self.name}]开设了新班级[{class_name}]，开课时间是{time}")

    def pay_study(self, student_obj):  # 支付学费
        self.__balance += student_obj.class_obj.all_prise()
        print(f'学生{student_obj.name}向校区[{self.name}]支付了学费{student_obj.class_obj.all_prise()}元')

    def school_new_student(self, student_obj):  # 报名入学
        self.s_student_list.append(student_obj)
        student_obj.school_obj = self
        print(f'学生[{student_obj.name}]入学[{self.name}]')

    def display_balance(self):  # 显示账户余额
        print(f'校区[{self.name}]的账户余额:{self.__balance}')

    def drop_out(self, student_obj):  # 学生退学
        if student_obj in self.s_student_list:
            self.s_student_list.remove(student_obj)
            student_obj.class_obj.c_student_list.remove(student_obj)
            print(f"学生[{student_obj.name}]退学了")
        else:
            print('没有该学生信息记录')


class BranchSchool(School):
    def __init__(self, name, address, headquarter):  # 建立分校
        School.__init__(self, name, address)
        self.headquarter = headquarter


class Class:
    c_student_list = []

    def __init__(self, class_name, school_obj, start_time):  # 开设班级
        self.class_name = class_name
        self.school_obj = school_obj
        self.start_time = start_time
        self.course_list = []
        self.c_student_list = []
        print(f"初始化班级:校区[{self.school_obj.name}]在{start_time}开设了新班级[{self.class_name}]")

    def class_new_student(self, student_obj):  # 学生加入班级
        self.c_student_list.append(student_obj)
        student_obj.class_obj = self
        print(f'学生[{student_obj.name}]加入了班级[{self.class_name}]')

    def add_course(self, course_obj):  # 添加课程
        self.course_list.append(course_obj)
        print(f"[{self.class_name}]开设了新课程[{course_obj.name}]")

    def list_course(self):  # 展示课程信息
        for i in self.course_list:
            print(f"班级{self.class_name}包括课程[{i.name}],该课程价格为:{i.price}")

    def all_prise(self):  # 计算课程总价格
        p = 0
        for pr in self.course_list:
            p += float(pr.price)
        return p

    def count_student_class(self):  # 统计班级学生总数
        print(f"班级[{self.class_name}的学生数量:{len(self.c_student_list)}]")

    def class_student_name(self):  # 查看所有学生姓名
        student_name = [i.name for i in self.c_student_list]
        print(student_name)


class Course:
    def __init__(self, name, price):  # 建立课程
        self.name = name
        self.price = price
        print(f"初始化课程:生成新的课程[{self.name}],价格为{self.price}")


class Staff:
    def __init__(self, name, age, position, salary, dept):  # 创建员工
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.dept = dept
        self.school_obj = None


class Teacher(Staff):  # 创建老师
    def __init__(self, name, age, position, salary, dept):
        Staff.__init__(self, name, age, position, salary, dept)
        self.class_obj = []
        self.teaching_list = []

    def teaching_class(self, class_obj):  # 老师添加授课班级
        self.class_obj.append(class_obj)


class Student:
    def __init__(self, name, age):  # 创建学生
        self.name = name
        self.age = age
        self.school_obj = None
        self.class_obj = None

    def transfer(self, new_class):  # 转校
        self.class_obj.c_student_list.remove(self)
        self.school_obj.s_student_list.remove(self)
        self.class_obj = new_class
        self.school_obj = new_class.school_obj
        self.class_obj.c_student_list.append(self)
        self.class_obj.school_obj.s_student_list.append(self)
        print(f"学生[{self.name}]转校至[{new_class.school_obj.name}的[{new_class.class_name}]")

    def student_info(self):
        print(f'姓名:{self.name} 年龄:{self.age} 所属学校:{self.school_obj.name} 班级:{self.class_obj.class_name}')


a = School('python上海总部', '上海虹桥')
class_a = Class('python基础1班', a, '2022-09-04')
staff_1 = Teacher('张三', '25', '讲师', '20000', '教学')
staff_2 = Staff('李四', '28', 'HR', '10000', '人事')
a.new_staff(staff_1, '2022-09-04')
a.new_staff(staff_2, '2022-09-05')
b = BranchSchool('python上海1号分校', '上海张江', a.name, )
a.count_staff_num()
a.count_student_num()
print(a.staff_list)
course_math = Course('数学', '5000')
course_python = Course('python', '10000')
class_a.add_course(course_python)
class_a.add_course(course_math)
print(class_a.all_prise())
class_b = Class('linux基础1班', b, '2022-09-04')
class_b.add_course(course_math)
print(class_a.course_list)
student_1 = Student('王五', '20')
a.school_new_student(student_1)
a.count_student_num()
class_a.class_new_student(student_1)
a.pay_study(student_1)
a.display_balance()
class_a.count_student_class()
a.drop_out(student_1)
a.drop_out(student_1)
class_a.count_student_class()
a.pay_salary(staff_2)
a.display_balance()
staff_1.teaching_class(course_math)
a.count_student_num()
student_2 = Student('赵六', '22')
b.school_new_student(student_2)
class_b.class_new_student(student_2)
print(student_2.class_obj.class_name, student_2.school_obj.name)
student_2.transfer(class_a)
a.pay_study(student_2)
a.count_student_num()
a.count_staff_num()
class_a.count_student_class()
class_b.count_student_class()
print(student_2.class_obj.class_name, student_2.school_obj.name)
print(a.s_student_list)
print(class_b.c_student_list)
print(student_2.__dict__)
student_2.student_info()
class_a.class_student_name()
class_a.list_course()
print([i.name for i in class_a.course_list])
