class Space:
    def __init__(
        self, number: int, is_occupied: bool, percentage: int, time_remaining: int
    ) -> None:
        self.number: int = number
        self.is_occupied: bool = is_occupied
        self.percentage: int = percentage
        self.time_remaining: int = time_remaining

    def __repr__(self) -> str:
        return f"Space(number={self.number}, is_occupied={self.is_occupied}, percentage={self.percentage}, time_remaining={self.time_remaining})"

    def __str__(self) -> str:
        return f"Space {self.number}: {'Occupied' if self.is_occupied else 'Free'}, Percentage: {self.percentage}%, Time Remaining: {self.time_remaining}s"


if __name__ == "__main__":
    from icecream import ic

    parking_1: list[Space] = [
        Space(1, True, 20, 70),
        Space(2, False, 0, 0),
    ]

    for space in parking_1:
        ic(space)
