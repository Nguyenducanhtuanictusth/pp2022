
class student:
    def __init__(self):
        self.option = 0
        self.student = {}
        self.id_name = {}
        self.add_course = {}
        self.student_mark = {}
        self.student_list = []

    #create option choice
    def option(self):
        print('we can choice this options here: ')
        print('Add new student: 1')
        print('Add new course: 2')
        print('Add mark: 3')
        print('Show student mark: 4')
        print('exit: 5')
        self.option = int(input('Enter your option: '))
        
        if self.option == 1 :
            self.add_student()
        elif self.option == 2 :
            self.add_course()
        elif self.option == 3 :
            self.add_mark()        
        elif self.option == 4 :
            self.show_mark()
        elif self.option == 5:
            print('thanks')
            return    
    #add number student and infor student
    def add_student(self):
        students = input('How many student to add: ')
        for i in range(int(students)):
            print(f'Enter student {i+1}')
            name = input('Name student is: ')
            student_id = input('Student ID is: ')
            DoB = input('student DoB: ')
            self.name_id[f'{name}'] = student_id
            self.student['Name'] = name
            self.student['Student ID'] = student_id
            self.student['Dob student'] = DoB
            self.student_list.append(self.student)
        print(self.student_list)
        self.option()
    #add number course and infor of course
    def add_course(self):         
        input_id = input('course have ID is: ')
        for number, student_id in self.name.id.items():
            if input_id == student_id:
                number_course = int(input('number of course to add : '))
                for number in range(number_course):
                    course_name = input('course is: ')
                    self.course_mark[f'{course_name}'] = None
                    self.student_course_mark[f'{student_id}'] = self.course_mark
                    self.option()
    #add mark into Course
    def add_mark(self):
        input_id = input('student ID you want add mark: ')
        for student_id, course_mark in self.student_course_mark.items():
            if input_id == student_id :
                course_name = input('the course is: ')
                for Course_name, number in course_mark.items():
                    if course_name == Course_name:
                        new_mark = input('new mark is: ')
                        course_mark[f'{Course_name}'] = new_mark
        self.option()                    
    #show infor and mark        
    def show_student_info(self):
        print(self.student_list)   
    def show_student_mark(self):
        input_id = input('student ID: ')
        course_list = list()
        mark.list = list()
        for student_id, course_mark in self.student_mark.items():
            if input_id == student_id:
                for Course,mark in course_mark.items():
                    course_list.append(Course)
                    course_mark.append(mark)
        print(course_list)
        print(course_mark)           
        self.option()
    student = show_student_mark        
