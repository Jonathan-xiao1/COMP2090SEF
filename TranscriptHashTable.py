
class TranscriptHashTable:

    #new data structure：(Hash Table)
    #Used to store students' historical report cards. Python's built-in dict is not used.


    def __init__(self, size=6):

        self._size = size
        #Use an outermost [] to store a fixed number of inner []. The inner [] can hold multiple pieces of data.
        self._score_list = [[] for _ in range(size)]

    def _hash_function(self, course_id):
        #Use Python's built-in hash() to convert a string into a random integer. Then take the remainder of dividing it by size as the index.
        return hash(course_id) % self._size

    def add_grade(self, course_id, credits, score):
        #Add or update grades
        index = self._hash_function(course_id)
        score_list_small = self._score_list[index] #score_list_small is a specific inner list

        # If the course already exists, update the grade。 The credits will not change, so it doesn't matter.
        for x in score_list_small:
            if x['course_id'] == course_id:
                x['score'] = score
                return

        # If it does not exist, store the relevant information of this course in the specified internal list.
        score_list_small.append({'course_id': course_id, 'credits': credits, 'score': score})

    def get_all_records(self):
        #get all grade records
        all_records = []  #Since the inner [] in the hash table may contain multiple pieces of data, resulting in a structure like [[], [1, 2]], it is necessary to store all valid data in a new list.
        for score_list_small in self._score_list:
            for item in score_list_small:#If an inner list has no data, this inner loop will be skipped directly
                all_records.append(item)
        return all_records