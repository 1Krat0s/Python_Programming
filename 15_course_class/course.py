class Course:
    """
        course_name (private)
        list of students (private)

        addStudent(self, student) shouldn't enroll the same student twice

        getCourseName
        getStudents
        getNumberOfStudents

        dropStudent(self, student) should provide a message with a dropped student name.
        Should check is the student present in the course (print message)

        __str__ info about the course
    """
    def __init__(self, course_name, list_of_students):
            self.__course_name = course_name
            self.__list_of_students = list_of_students
    
    def addStudent(self, student):
        y = 0
        for x in self.__list_of_students:
            if x == student:
                y = y + 1
        if y < 1:
            self.__list_of_students.append(student)

    def getCourseName(self):
        return self.__course_name

    def getStudents(self):
        return self.__list_of_students

    def getNumberOfStudents(self):
        return len(self.__list_of_students)

    def dropStudent(self, student):
        for x in self.__list_of_students:
            if x == student:
                self.__list_of_students.remove(student)
                return f"The student: {student} was removed from the course."
        
        return f"The student: {student} was not apart of the course."

    def __str__(self):
        return f"Course name: {self.getCourseName()}, Number of students in course: {self.getNumberOfStudents()}, Names of students in course: {self.getStudents()}"


class InPersonCourse(Course):
    """
        private - room_number
        private - schedule (MWF 11 am - 11:50 am)
        private - max_seats

        Override addStudent method (check are there available seats) print appropriate message

        Override __str__ 
    """
    def __init__(self, course_name, list_of_students, room_number, schedule, max_seats):
        super().__init__(course_name, list_of_students)
        self.__room_number = room_number
        self.__schedule = schedule
        self.__max_seats = max_seats

    def addStudent(self, student):
        if self.getNumberOfStudents() < self.__max_seats:
            super().addStudent(student)

    def __str__(self):
        return super().__str__() + f", Room number: {self.__room_number}, Schedule: {self.__schedule}, Max seats: {self.__max_seats}"
        
if __name__ == "__main__":
    COP3337 = Course("COP3337", ["George Washington"])
    COP3337.addStudent("James Harden")

    print(COP3337.getCourseName())
    print(COP3337.getNumberOfStudents())
    print(COP3337.getStudents())

    print(COP3337)

    COP3337.dropStudent("George Washington")

    print(COP3337)

    print(" ")

    COP2080 = InPersonCourse("COP2080", ["Abraham Lincoln"], "IST 1032", "MW 11:00am - 11:50am", 36)
    COP2080.addStudent("Justin Bryant")

    print(COP2080.getCourseName())
    print(COP2080.getNumberOfStudents())
    print(COP2080.getStudents())

    print(COP2080)

    COP2080.dropStudent("Abraham Lincoln")
    print(COP2080)