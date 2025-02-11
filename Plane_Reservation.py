class Seat:
    def __init__(self, row, place):
        self.row = row
        self.place = place
        self.reserved = False
        self.passenger_name = None

    def reservation_action(self, passenger_name):
        if self.reserved:
            return False
        self.reserved = True
        self.passenger_name = passenger_name
        return True

    def cancel_reservation_action(self):
        self.reserved = False
        self.passenger_name = None

class Airplane:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.places = ["A", "B", "C", "D", "E", "F"][:cols]
        self.seats = [[Seat(row, col) for col in self.places] for row in range(1, rows + 1)]

    def seatmap(self):
        print("\nSeat Map:")
        print("    " + "   ".join(self.places)) 
        for row_num, row in enumerate(self.seats, start=1):
            row_display = " ".join("|X|" if seat.reserved else "|0|" for seat in row)
            print(f"{row_num:2} {row_display}")

    def reserve(self, row, col, passenger_name):
        if self.seats[row][col].reservation_action(passenger_name):
            print(f"Seat {row + 1}{self.places[col]} reserved successfully")
        else:
            print(f"Seat {row + 1}{self.places[col]} reservation failed! This seat has already been reserved.")

    def cancel_reserve(self, row, col, passenger_name):
        if not self.seats[row][col].reserved:
            print(f"Seat {row + 1}{self.places[col]} hasn't been reserved.")
        else:
            self.seats[row][col].cancel_reservation_action()
            print(f"Seat {row + 1}{self.places[col]} reservation cancelled successfully!")

plane = Airplane(32, 6)

start = True
while start:

    print("\nThis is a plane seat reservation app!"
        "\n Choose the operation you want to perform (1-3):"
        "\n(1) - Display plane seat map;"
        "\n(2) - Reserve a seat;"
        "\n(3) - Cancel reserved seat;")

    n = int(input("Enter operation number: "))

    if n == 1:
        plane.seatmap()

    elif n == 2:
        row_num = int(input("Enter a row number: "))
        row = row_num - 1
        seat_letter = input("Enter a seat letter (A-G): ").upper()
        if seat_letter in plane.places:
            col = plane.places.index(seat_letter)
            passenger_name = input("Enter passenger's name: ")
            plane.reserve(row, col, passenger_name)
        else:
            print("Invalid seat letter! Try again.")

    elif n == 3:
        row_num = int(input("Enter a row number: "))
        row = row_num - 1
        seat_letter = input("Enter a seat letter (A-G): ").upper()
        if seat_letter in plane.places:
            col = plane.places.index(seat_letter)
            passenger_name = input("Enter passenger's name: ")
            plane.cancel_reserve(row, col, passenger_name)
        else:
            print("Invalid seat letter! Try again.")



