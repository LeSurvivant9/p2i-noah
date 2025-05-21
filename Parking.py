from Space import Space


class Parking:
    def __init__(self) -> None:
        self._spaces: list[Space] = []

    def add_space(self, space: Space) -> None:
        self._spaces.append(space)

    def get_spaces(self) -> list[Space]:
        return self._spaces
