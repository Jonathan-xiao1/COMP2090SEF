from TranscriptHashTable import TranscriptHashTable
from tools import tools
class TranscriptPrinter:
    @staticmethod
    def print_transcript(student_name, transcript, func):

        #Print transcript independently (static method)，Avoid placing it in the class Student to prevent the code from becoming too long.
        #func: class binary_search_gpa_point

        records = transcript.get_all_records()
        print(f" {student_name} detailed transcript ")

        # 无成绩记录
        if len(records) == 0:
            print("No score records available！")
            return

        total_credit_points = 0.0
        total_credits = 0

        # 打印表头
        print(f"{'course':<10} | {'score':<5} | {'GPA':<8} | {'credit':<5} | {'weighted score'}")
        print("-" * 100)
        print("-" * 100)

        # 遍历成绩
        for record in records:
            course = record['course_id']
            score = record['score']
            credits = record['credits']

            # 调用外部传入的二分查找函数
            gpa = func(score)
            weighted_score = gpa * credits

            total_credit_points += weighted_score
            total_credits += credits

            print(f"{course:<10} | {score:<5} | {gpa:<8} | {credits:<5} | {weighted_score}")

        # 计算最终GPA
        final_gpa = round(total_credit_points / total_credits, 2)
        print(f"Total credits: {total_credits}")
        print(f"Total weighted score: {total_credit_points}")
        print(f"Final GPA: {final_gpa} ")