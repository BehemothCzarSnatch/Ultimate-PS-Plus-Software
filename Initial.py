from datetime import datetime


class Event:
    def __init__(self, name, date, location):
        self.name = name
        self.date = datetime.strptime(date, "%Y-%m-%d %H:%M")
        self.location = location


class EventPlanner:
    def __init__(self):
        self.events = []

    def add_event(self, name, date, location):
        self.events.append(Event(name, date, location))

    def print_schedule(self):
        self.events.sort(key=lambda event: event.date)

        print("Event Schedule")
        print("==============")

        for event in self.events:
            print(
                f"{event.date.strftime('%Y-%m-%d %H:%M')} | "
                f"{event.name} | {event.location}"
            )


planner = EventPlanner()

planner.add_event("Team Meeting", "2026-09-15 10:00", "Office")
planner.add_event("Project Demo", "2026-09-12 14:30", "Conference Room")
planner.add_event("Workshop", "2026-09-18 09:00", "Training Center")
planner.add_event("Company Party", "2026-09-20 19:00", "City Hall")

planner.print_schedule()
