# Activity Date Management Module
class EventDate:
    def __init__(self):
        self.events = []

    # Add Activity
    def add_event(self, title, date, detail):
        event = {
            "title": title,
            "date": date,
            "detail": detail
        }
        self.events.append(event)

    # Show All Activities
    def show_all_events(self):
        return self.events

    # Search Activities by Date
    def find_event_by_date(self, target_date):
        result = []
        for event in self.events:
            if event["date"] == target_date:
                result.append(event)
        return result