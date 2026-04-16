# Suggestions & Proposals Module
class Suggestion:
    def __init__(self):
        self.suggestion_list = []

    # Submit Suggestions
    def submit_suggestion(self, student_id, content):
        item = {
            "student_id": student_id,
            "content": content
        }
        self.suggestion_list.append(item)

    # View All Suggestions
    def get_all_suggestions(self):
        return self.suggestion_list

    # Get the total number of suggestions
    def get_suggestion_count(self):
        return len(self.suggestion_list)