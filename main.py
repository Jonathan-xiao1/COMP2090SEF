# main.py
from CircularQueue import CircularQueue
from tools import tools
from Classes import Instructor, Course, Student

def main():
    # 1. Initialize the course pool & teacher
    prof_lee = Instructor(user_id="T001", name="Prof. Lee", department="Computer Science")

    course_list = [
        Course(course_id="CS101", name="Python programming ", credits=3, start_time="09:00", end_time="11:00",
               class_date="Monday", capacity=2),
        Course(course_id="CS102", name="Fundamentals of Algorithms", credits=4, start_time="10:00", end_time="12:00", class_date="Monday",
               capacity=30),
        Course(course_id="CS103", name="web design", credits=2, start_time="14:00", end_time="16:00", class_date="Monday",
               capacity=30),
        Course(course_id="CS104", name="database", credits=4, start_time="09:00", end_time="11:00", class_date="Tuesday",
               capacity=30)
    ]

    # Assign a course to the teacher and display the teacher's information.(Polymorphism)
    prof_lee.assign_course(course_list[0])
    print("--- Teacher Information ---")
    prof_lee.show_info()
    print("\n")

    # 2. Simulate course selection by students（The order of invocation represents the speed of hand operation.）
    s1 = Student(user_id="202601", name="Alam")
    s2 = Student(user_id="202602", name="alex")
    s3 = Student(user_id="202603", name="jeremy")

    print("--- Course selection system activated  ---")
    # Create a buffer queue with a capacity of 5
    request_queue = CircularQueue(5)#call the class

    # Simulating Everyone Scrambling for Python Programming (CS101)
    target = course_list[0]
    print(f"Target course: {target.get_name()}, capacity: {target.get_capacity()}")

    # Join the queue in sequential order
    request_queue.enqueue(s1)  # the fastest
    request_queue.enqueue(s2)  # second
    request_queue.enqueue(s3)  # the slowest

    # processing queue
    while True:
        student = request_queue.dequeue()#Call the function defined in the class
        if student is None:
            break

        if target.get_enrolled_count() < target.get_capacity():#At this time, the target is an object with specific properties.
            if target.increment_enrolled():
                student.add_to_schedule(target)#Call the function method of student
                print(f"successfully！ [{student.name}] ")
        else:
            print(f"failure！ [{student.name}] Course selection failed: The quota is full。")


    #  3. Score Entry and GPA Calculation Display
    print("\n--- Processing Historical Grades for Alam ---")
    # 模拟 Alam 之前学期的成绩
    s1.add_past_grade("MATH101", credits=4, score=92)  # 4.0
    s1.add_past_grade("ENG101", credits=2, score=78)  # 2.0
    s1.add_past_grade("PHYS101", credits=3, score=85)  # 3.0

    # Invoke the GPA calculation and printing logic (using Hash Table and Binary Search)
    s1.show_transcript()



    # 4. Course Recommendation Form (Based on Alam Schedule)
    print("\nGenerate a non-conflicting recommended schedule for [Alam] (sorted by credits)")#The variable name of Alam is s1

    # Retrieve all courses that the student has already selected.
    student_selected_courses = s1.get_schedule()

    recommend_pool = []

    #Determine whether there is a conflict between each course and the already selected schedule.
    for course in course_list:
        # Skip courses that students have already selected
        if course in student_selected_courses:
            continue

        # By default, there is no conflict for this course.
        has_conflict = False


        for selected in student_selected_courses:
            if tools.check_conflict(course, selected):
                # If it conflicts with any selected course ， marking as conflicting
                has_conflict = True
                break

        # If there is no conflict ， add to the recommendation pool
        if not has_conflict:
            recommend_pool.append(course)

    # Use Shell Sort
    sorted_recommend = tools.shell_sort_recommendation(recommend_pool)
    for r in sorted_recommend:
        r.display()


if __name__ == "__main__":
    main()