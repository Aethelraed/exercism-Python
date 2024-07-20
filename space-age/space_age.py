class SpaceAge:
    sec_per_year = 60 * 60 * 24 * 365.25

    def __init__(self, seconds):
        self.e_year = seconds / SpaceAge.sec_per_year

    def on_earth(self):
        return round(self.e_year / 1, 2)

    def on_mercury(self):
        return round(self.e_year / 0.2408467, 2)

    def on_venus(self):
        return round(self.e_year / 0.61519726, 2)

    def on_mars(self):
        return round(self.e_year / 1.8808158, 2)

    def on_jupiter(self):
        return round(self.e_year / 11.862615, 2)

    def on_saturn(self):
        return round(self.e_year / 29.447498, 2)

    def on_uranus(self):
        return round(self.e_year / 84.016846, 2)

    def on_neptune(self):
        return round(self.e_year / 164.79132, 2)
