from typing import Tuple, overload

class Game:
    name: str
    shots = 0
    goals = 0

    @overload
    def __init__(self, name: str): ...

    def __init__(self, record: Tuple[str]):
        if isinstance(record, str):
            self.name = record
            return
        self.name = record[0]
        self.shots = int(record[1])
        self.goals = int(record[2])

    def __str__(self):
        return self.name