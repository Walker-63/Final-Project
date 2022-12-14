import patient as p
import os
import facility as fa
import doctor as d
import laboratory as l


# doctor section

# Doctor menu options

# Display Doctors List
def displayDoctorsList():
    doctorfile = open('doctors.txt', "r")
    for lines in doctorfile:
        lines = lines.replace('_', ' ')
        print(lines)
    doctorfile.close()


# Search Doctor by ID
def searchDoctorById():
    check = False
    doctordID = str(input("Enter Doctor ID: "))
    doctorfile = open("doctors.txt", "r")

    for line in doctorfile:
        if doctordID in line:
            line = line.replace('_', ' ')
            print(line)
            check = True
    if check == False:
        print("Doctor with ID: ", doctordID, "not in doctor file")

# Search Doctor by Name
def searchDoctorByName():
    check = False
    doctorName = str(input("Enter Doctor Name: "))
    doctorfile = open("doctors.txt", "r")

    for line in doctorfile:
        if doctorName in line:
            line = line.replace('_', ' ')
            print(line)
            check = True
    if check == False:
        print("Doctor with Name: ", doctorName, "not in patient file")

# Add doctor to list
def addDrToList():
    id = str(input("Enter doctor ID:"))
    name = str(input("Enter doctor name:"))
    specialty = str(input("Enter doctor specialty:"))
    schedule = str(input("Enter doctor schedule:"))
    qualifications = str(input("Enter doctor qualifications:"))
    roomNumber = str(input("Enter doctor room number"))

    x = d.Doctor(id, name, specialty, schedule, qualifications, roomNumber)

    writeDoctorsListToFile(x)

# Write Doctor List to File
def writeDoctorsListToFile(bob):
    lines = bob.formatDoctorInfo()
    with open('doctors.txt', 'a') as f:
        f.writelines(lines)

# Edit Doctor Info
def editDoctorInfo():
    doctorfile= open("doctors.txt", "r")
    doctorfile1 = open ("temp.txt", "w")

    print ("\n")
    docID = input("Enter the doctor id: ")
    print ("\n")

    lines = ' '
    while (lines):
        lines =doctorfile.readline()
        line1 = lines.replace ("_", "  ")
        position = lines.split("_")
        if len(lines)>0:
            if (position[0]) == docID:
                print(line1)
                name = input ("Enter new Name: ")
                specialty = input ("Enter new specialty: ")
                schedule = input ("Enter new schedule: ")
                qualifications = input ("Enter new qualifications: ")
                roomNumber = input ("Enter new room number:")

                myCoxLong = d.Doctor(docID, name, specialty, schedule, qualifications, roomNumber)

                doctorfile1.write(myCoxLong.formatDoctorInfo()+"\n")
            else:
                doctorfile1.write(lines)

    doctorfile.close()
    doctorfile1.close()
    os.remove("doctors.txt")
    os.rename("temp.txt", "doctors.txt")
    displayDoctorsList()


# Doctor Menu
def doctorsMenu():
    menuNum = 1

    while menuNum != 0:
        print("Doctor's Menu")
        print("0 - Return to Main Menu")
        print("1 - Display Doctors List")
        print("2 - Search For Doctor By ID")
        print("3 - Search For Doctor By Name")
        print("4 - Add Doctor")
        print("5 - Edit Doctor Info")
        menuNum = int(input("Enter Option:"))

        if (menuNum == 1):
            displayDoctorsList()

        elif (menuNum == 2):
            searchDoctorById()

        elif (menuNum == 3):
            searchDoctorByName()

        elif (menuNum == 4):
            addDrToList()

        elif (menuNum == 5):
            editDoctorInfo()


def displayFacilitesList():
    file = open("facilities.txt")
    for lines in file:
        lines = lines.replace("_", " ")
        print(lines)
    file.close()

def addfacilityToList():
    name = str(input("Enter Facility Name:"))
    fac = fa.Facility(name)
    writeFacilityListToFile(fac)

def writeFacilityListToFile(fuc):
    with open('facilities.txt', 'a') as f:
        f.writelines(fuc.formatFacilityInfo())

# Facility section
def facilitiesMenu():
    menuNum = 1

    while menuNum != 0:
        print("Facility Menu")
        print("0 - Return to Main Menu")
        print("1 - Diplays Facilities List")
        print("2 - Add Facility")
        menuNum = int(input("Enter Option:"))

        if (menuNum == 1):
            displayFacilitesList()

        elif (menuNum == 2):
            addfacilityToList()




# Laboratory section

# Display Laboratory List
def displayLabsList():
    LabFile = open('laboratories.txt', "r")
    for lines in LabFile:
        lines = lines.replace('_', ' ')
        print(lines)
    LabFile.close()

# Write Lab List to File
def writeLabListToFile(lab):
    lines = lab.formatLabInfo()
    with open('laboratories.txt', 'a') as f:
        f.writelines(lines)

# Add Lab To list
def addlaboratoryToList():
    lab = str(input("Enter Lab Name: "))
    labcost = str(input("Enter Lab Cost: "))

    x = l.Laboratory(lab, labcost)

    writeLabListToFile(x)




#Laboratory Menu
def laboratoriesMenu():
    menuNum = 1

    while menuNum != 0:
        print("Patient Menu")
        print("0 - Return to Main Menu ")
        print("1 - Display Labratories List")
        print("2 - Add Labratory")
        menuNum = int(input("Enter Option:"))

        if (menuNum == 1):
            displayLabsList()

        elif (menuNum == 2):
            addlaboratoryToList()


# Patient section
def searchPatientById():
    check = False
    patientID = str(input("Enter Patient ID: "))
    patientfile = open("patients.txt", "r")

    for line in patientfile:
        if patientID in line:
            line = line.replace('_', ' ')
            print(line)
            check = True
    if check == False:
        print("Patient with ID ", patientID, "not in patient file")


def editPatientInfo():
    patientfile = open("patients.txt", "r")
    patientfile1 = open("temp.txt", "w")

    print("\n")
    patID = (input("Enter the patient id: "))
    print("\n")

    lines = ' '
    while (lines):
        lines = patientfile.readline()
        line1 = lines.replace("_", "  ")
        position = lines.split("_")
        if len(lines) > 0:
            if (position[0]) == patID:
                print(line1)
                patName = input("Enter new Name: ")
                patDiag = input("Enter new diagnosis: ")
                patGen = input("Enter new gender: ")
                patAge = input("Enter new age: ")

                ravjeet = p.Patient(patID, patName, patDiag, patGen, patAge)

                patientfile1.write(ravjeet.formatPatientInfo()+"\n")
            else:
                patientfile1.write(lines)

    patientfile.close()
    patientfile1.close()
    os.remove("patients.txt")
    os.rename("temp.txt", "patients.txt")
    displayPatientsList()


def displayPatientsList():
    patientfile = open('patients.txt', "r")
    for lines in patientfile:
        lines = lines.replace('_', ' ')
        print(lines)
    patientfile.close()


def addPatientToList():
    id = str(input("Enter patient ID:"))
    name = str(input("Enter patient name:"))
    diagnosis = str(input("Enter patient diagnosis:"))
    gender = str(input("Enter patient gender:"))
    age = str(input("Enter patient age:"))

    mary = p.Patient(id, name, diagnosis, gender, age)

    writePatientsListToFile(mary)


def writePatientsListToFile(marytwo):
    lines = marytwo.formatPatientInfo()
    with open('patients.txt', 'a') as f:
        f.writelines(lines)


def patientMenu():
    menuNum = 1

    while menuNum != 0:
        print("\nPatient Menu")
        print("0 - Return to Main Menu ")
        print("1 - Display Patient's List")
        print("2 - Search for Patient by UID")
        print("3 - Add Patient")
        print("4 - Edit Patient ")
        menuNum = int(input("Enter Option:"))

        if (menuNum == 1):
            displayPatientsList()

        elif (menuNum == 2):
            searchPatientById()

        elif (menuNum == 3):
            addPatientToList()

        elif (menuNum == 4):
            editPatientInfo()


def mainMenu():
    menuNum = 1

    while menuNum != 0:
        print("Welcome to the Alberta Rural Patient Care Management System")
        print("Main Menu")
        print("0 - Close Application")
        print("1 - Doctors")
        print("2 - Facilities")
        print("3 - Laboratories")
        print("4 - Patients")
        menuNum = int(input("Enter Option: "))
        print()

        if (menuNum == 1):
            doctorsMenu()

        elif (menuNum == 2):
            facilitiesMenu()

        elif (menuNum == 3):
            laboratoriesMenu()

        elif (menuNum == 4):
            patientMenu()


mainMenu()
