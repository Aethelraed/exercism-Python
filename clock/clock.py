class Clock:
    def __init__(self, hour, minute):
        self.h, self.m = (minute // 60 + hour) % 24, minute % 60

    def __repr__(self):
        return f"Clock({self.h}, {self.m})"

    def __str__(self):
        return (
            f"{'0' if self.h <10 else ''}{self.h}:{'0' if self.m <10 else ''}{self.m}"
        )

    def __eq__(self, other):
        return self.m == other.m and self.h == other.h

    def __add__(self, minutes):
        self.__init__(self.h, self.m + minutes)
        return self

    def __sub__(self, minutes):
        return self.__add__(-minutes)
