from event_date import EventDate
from suggestion import Suggestion

def main():
    # Instantiate an object（Initialize only once to avoid adding demo data repeatedly）
    event_system = EventDate()
    suggestion_system = Suggestion()

    # Preload demo activities（only execute once）
    event_system.add_event("Graduation Photo Shoot", "2026-05-20", "10:00 a.m., Playground")
    event_system.add_event("Final Review Lecture", "2026-04-25", "Library Lecture Hall")

    # core：add while True loop，let the menu keep showing
    while True:
        print("\n===== Student Mobile =====")
        print("1. Activity Date Management")
        print("2. Suggestions and Proposals")
        print("3. Exit")
        print("============================")

        # Put the input prompt inside the loop and display it again after each selection
        choice = input("Please enter the function number: ")

        if choice == "1":
            print("\n→ Activity Date Management")
            # Display all activitie
            all_events = event_system.show_all_events()
            for e in all_events:
                print(f"[{e['date']}] {e['title']} - {e['detail']}")

        elif choice == "2":
            print("\n→ Suggestions and Proposals")
            sid = input("Please enter your student ID: ")
            content = input("Please Enter suggestion content: ")
            suggestion_system.submit_suggestion(sid, content)
            print(f"Submitted successfully! The current total is {suggestion_system.get_suggestion_count()}")

        elif choice == "3":
            print("Exiting program... Goodbye!")
            break  # A break is only valid inside a while loop.

        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()