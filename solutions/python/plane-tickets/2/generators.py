"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    seats = ['A', 'B', 'C', 'D']
    for i in range(number):
        yield seats[i % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    row_no = 1
    seat_count = 0

    for seat_letter in generate_seat_letters(number):
        if row_no == 13:
            row_no = 14
        yield f"{row_no}{seat_letter}"

        seat_count += 1

        if seat_count == 4:
            seat_count = 0
            row_no += 1


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    assignment = {}
    seat = generate_seats(len(passengers))
    for i in passengers:
        assignment[i] = next(seat)
    return assignment 


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    for i in seat_numbers:
        yield (i + flight_id + '0' * (12 - len(i + flight_id)))
