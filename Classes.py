from TranscriptHashTable import TranscriptHashTable
from TranscriptPrinter import TranscriptPrinter
from tools import tools

class User:
    #class User is a parent class
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def get_role(self):#Parent class method, to be overridden by subclasses (polymorphism)
        return " general user"


class Instructor(User):
    # Teachers
    def __init__(self, user_id, name, department):
        super().__init__(user_id, name)
        self._department = department
        self._teaching_courses = []

    def get_role(self):
         #Override the method of the parent class
        return f"Instructor from {self._department}"

    def assign_course(self, course):
        self._teaching_courses.append(course)

    def show_info(self):
        print(f"[{self.get_role()}] Name: {self.name} (ID: {self.user_id})")
        print(f"Teaching Courses: {[c.get_name() for c in self._teaching_courses]}")


class Student(User):
    # The Student class is a subclass inherited from the User class.
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        #Use encapsulation for properties to prevent direct external modification
        self._my_schedule = [] #Personal courses schedule

        self._transcript = TranscriptHashTable(size=6)#store the grades of each subject using a hash table，instead of using dict
                                                       #a class defined in subsequent classes

    def get_schedule(self):
        return self._my_schedule

    def get_role(self):#Override the parent class method
        return "Student!"


    def add_to_schedule(self, course):
        self._my_schedule.append(course)

    def add_past_grade(self, course_id, credits, score):
        #Enter a new course score
        if score < 0 or score > 100:
            raise ValueError(" Score must be between 0 and 100!")#An error will be reported if an invalid score is entered.
        self._transcript.add_grade(course_id, credits, score) #_transcript is a private attribute of the Student class
                                                              #add_grade() is a function defined in the TranscriptHashTable class


    def show_transcript(self):

        TranscriptPrinter.print_transcript(
            student_name=self.name,
            transcript=self._transcript,
            func=tools.binary_search_gpa_point#Classes newly defined in subsequent code
        )

    def show_info(self):
        print(f"Student name: {self.name} (ID: {self.user_id})")
        print(f"Selected Courses: {[c.get_name() for c in self._my_schedule]}")#Use list comprehensions


class Course:
    #course class
    def __init__(self, course_id, name, credits, start_time, end_time, class_date, capacity):
        self._course_id = course_id
        self._name = name
        self._credits = credits
        self._start_time = start_time
        self._end_time = end_time
        self._class_date = class_date
        self._capacity = capacity
        self._enrolled_count = 0 # Number of registered applicants

    def get_course_id(self):
        return self._course_id

    def get_name(self):
        return self._name

    def get_credits(self):
        return self._credits

    def get_start_time(self):
        return self._start_time

    def get_end_time(self):
        return self._end_time

    def get_class_date(self):
        return self._class_date

    def get_capacity(self):
        return self._capacity

    def get_enrolled_count(self):
        return self._enrolled_count

    def increment_enrolled(self):
        if self._enrolled_count < self._capacity:
            self._enrolled_count += 1
            return True
        return False

    def display(self):
        print(f"{self._course_id} {self._name}  credit: {self._credits} | "
              f"time: {self._class_date} {self._start_time}-{self._end_time} | "
              f"remaining spots: {self._capacity - self._enrolled_count}")
