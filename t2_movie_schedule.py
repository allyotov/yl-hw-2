from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


class DatesGenerator:
    def __init__(self, date_ranges) -> Generator:
        self.start_date, self.end_date = date_ranges.pop(0)
        self.ranges = date_ranges
        self.current_date = self.start_date

    def __iter__(self):
        while True:
            try:
                yield self.current_date
                self.current_date += timedelta(days=1)
                if self.current_date > self.end_date:
                    if not self.ranges:
                        raise StopIteration
                    self.current_date, self.end_date = self.ranges.pop(0)
            except StopIteration:
                break



@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        return DatesGenerator(self.dates)


if __name__ == '__main__':
    m = Movie('sw', [
            (datetime(2020, 1, 1), datetime(2020, 1, 7)),
            (datetime(2020, 1, 15), datetime(2020, 2, 7))
        ])
    for i, d in enumerate(m.schedule(), start=1):
        print('{}) {}'.format(i, d))