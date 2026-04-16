



class CircularQueue:


    #New data structure：Circular Queue
    #Simulate students' course selection rush, following the principle of first-come, first-served.


    def __init__(self, size):
        self._size = size
        self._queue = [None] * (size + 1) #An additional seat needs to be reserved, but it will not be used.
        self._head = 1                    #Its function is to help determine whether the quota is full
        self._tail = 1

    def enqueue(self, student):
        current = self._head
        # Determine whether students have selected the same course repeatedly
        while current != self._tail:
            queue_item = self._queue[current]
            #If the current student is already in the queue, it indicates a duplicate course selection.
            if queue_item is not None and queue_item.user_id == student.user_id:
                print("You have already selected this course, cannot select repeatedly!")
                return False
            current = (current + 1) % len(self._queue)

        #Students join the course selection queue
        if ((self._tail + 1) % len(self._queue) == self._head):#This requires the content mentioned above (reserve an additional position)
                                                               #If it is exactly full, (tail + 1) % (size + 1) == 1. If it is not full, the remainder result will be tail or 0.
            print("too many people are competing for courses. Please try again later.")
            return False
        self._queue[self._tail] = student
        self._tail = (self._tail + 1) % len(self._queue)#Get the position of the next tail
        return True

    def dequeue(self):
        #Process student course selection in the order of their submission speed.
        if (self._head == self._tail):#No students are competing to enroll in this course
            return None
        result = self._queue[self._head]
        self._head = (self._head + 1) % len(self._queue)#The next student
        return result
