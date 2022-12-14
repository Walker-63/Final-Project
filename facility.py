# Facility class

class Facility:

    def __init__(self, facilName):
        self.facilName = facilName

    def __str__(self):
        return f"Facility Name: {self.facilName}"

    def formatFacilityInfo(self):
        return f"{self.facilName}"

