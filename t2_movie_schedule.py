from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


def get_days(date_ranges):
    current_date, end_date = date_ranges.pop(0)
    while True:
        yield current_date
        current_date += timedelta(days=1)
        if current_date > end_date:
            if not date_ranges:
                return
            current_date, end_date = date_ranges.pop(0)


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        return get_days(self.dates)


if __name__ == '__main__':
    m = Movie('sw', [
            (datetime(2020, 1, 1), datetime(2020, 1, 7)),
            (datetime(2020, 1, 15), datetime(2020, 2, 7))
        ])
    for i, d in enumerate(m.schedule(), start=1):
        print('{}) {}'.format(i, d))