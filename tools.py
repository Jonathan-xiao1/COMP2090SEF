
class tools:
    @staticmethod
    def shell_sort_recommendation(courses):
        #The variable course will be defined in the subsequent main program and is a list of all optional subjects.
        #New Algorithm: Shell Sort
        #Sort the recommended courses in ascending order of credits.

        n = len(courses)
        gap = n // 2#Group the data
        while gap > 0:
            # perform insertion sort for each group
            for i in range(gap, n):
                temp = courses[i]#Temporarily store the course object to be inserted and sorted currently
                j = i#Record the current location
                # Ascending sorting
                while j >= gap and courses[j - gap].get_credits() < temp.get_credits():
                    courses[j] = courses[j - gap]#The previous element is moved backward by gap positions
                    j -= gap
                courses[j] = temp#Insert the original data back into the new position
            gap //= 2
        return courses

    @staticmethod
    def check_conflict(c1, c2):#course1 & course2
        #Time Conflict Detection
        if c1.get_class_date() != c2.get_class_date():
            return False

        #Convert time such as "09:00" to 900 for easy comparison
        t1_start = int(c1.get_start_time().replace(":", ""))
        t1_end = int(c1.get_end_time().replace(":", ""))
        t2_start = int(c2.get_start_time().replace(":", ""))
        t2_end = int(c2.get_end_time().replace(":", ""))

        # There is a conflict as long as the start time of one falls within the range of the other.
        return not (t1_end <= t2_start or t2_end <= t1_start)


    @staticmethod
    def binary_search_gpa_point(score):

        # Calculate GPA
        # New Algorithm: Interval Binary Search
        # Convert percentage-based scores to grade points (e.g., 90-100 -> 4.0, 80-89 -> 3.0)

        # Rule: (Minimum Score, Corresponding Grade Point)。Sort from smallest to largest！
        boundaries = [(0, 0.0), (60, 1.0), (70, 2.0), (80, 3.0), (90, 4.0)]

        low = 0  # minimum index
        high = len(boundaries) - 1  # maximum index
        result_gpa = 0.0

        while low <= high:
            mid = (low + high) // 2
            # If the current score is greater than or equal to the lower limit of this interval
            if score >= boundaries[mid][0]:
                result_gpa = boundaries[mid][1]  # Save this GPA temporarily
                low = mid + 1  # Try looking further to the right
            else:
                high = mid - 1  # If the score is insufficient, look for a lower interval on the left.

        return result_gpa