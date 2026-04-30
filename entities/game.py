from typing import Tuple, overload
from datetime import datetime

class Game:
    name: str
    shots: int = 0
    goals: int = 0
    date: str = datetime.now().strftime("%Y-%m-%d")

    @overload
    def __init__(self, name: str): ...

    def __init__(self, record: Tuple[str]):
        if isinstance(record, str):
            self.name = record
            return
        self.name = record[0]
        self.shots = int(record[1])
        self.goals = int(record[2])
        self.date = record[3]

    def __str__(self):
        return self.name
    
    def getSaves(self) -> int:
        return max(self.shots - self.goals, 0)
    
    def getSavePct(self) -> float:
        if self.shots == 0:
            return 0
        return (self.shots - self.goals) / self.shots