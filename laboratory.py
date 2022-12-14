# Laboratory class

class Laboratory:

    def __init__(self, labName, cost):
        self.labName = labName
        self.cost = cost

    def __str__(self):
        return (f"Lab Name: {self.labName}"
                f"Cost: {self.cost}")

    def formatLabInfo(self):
        return f"{self.labName}_{self.cost}"
        