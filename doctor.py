# Doctor Class

class Doctor:

    def __init__(self, id, name, specialty, schedule, qualification, roomNum):
        self.id = id
        self.name = name
        self.specialty = specialty
        self.schedule = schedule
        self.qualification = qualification
        self.roomNum = roomNum

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Specialty: {self.specialty}\n"
                f"Schedule: {self.schedule}\n"
                f"Qualification: {self.qualification}"
                f"Room Number: {self.roomNum}")

    def formatDoctorInfo(self):
        return f"{self.id}_{self.name}_{self.specialty}_{self.schedule}_{self.qualification}_{self.roomNum}"


