from __future__ import annotations


class Distance:	class Distance:
    # Write your code here	    def __init__(self, km: float | int) -> None:
    pass	        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            raise TypeError("Cannot multiply two Distance instances.")
        return Distance(self.km * other)

    def __truediv__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            raise TypeError("Cannot divide two Distance instances.")
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | float | int) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km < other_km

    def __gt__(self, other: Distance | float | int) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km > other_km

    def __eq__(self, other: Distance | float | int) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return round(self.km, 2) == round(other_km, 2)

    def __le__(self, other: Distance | float | int) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km <= other_km

    def __ge__(self, other: Distance | float | int) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km >= other_km
