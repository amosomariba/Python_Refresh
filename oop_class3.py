class Room:
    length = 0.0
    breadth = 0.0

    def calculate_area(self):
        print(f"Area of Room = {self.length * self.breadth}")


study_room = Room()

study_room.length = 25.4
study_room.breadth = 34.5

study_room.calculate_area()
