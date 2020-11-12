from enum import Enum


class PeriodType(Enum):

    MONTHLY = 1
    YEARLY = 2

    def __str__(self):
        return "months" if self.value == self.MONTHLY.value else "years"
