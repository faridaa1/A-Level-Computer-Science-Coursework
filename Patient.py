#importing library which can be referenced later
import random 

class Patient: #creates a class for each patient 
  def __init__(self, record): #creates a record where each field is derived from the record variable decleared in the main program
    self.forename = record[0] #stores forename input
    self.surname = record[1] #stores surename input
    self.dateOfBirth = record[2] #stores date of birth input
    self.gender = record[3] #stores gender input
    self.ethnicity = record[4] #stores ethnicity input
    self.allergies = record[5] #stores allergies input
    self.numberOfCovidVaccines = record[6] #stores number of COVID-19 vaccines input
    self.numberOfCovidCases = record[7] #stores number of COVID-19 cases input
    self.addressLineOne = record[8] #stores address line one input
    self.addressLineTwo = record[9] #stores address line two input
    self.addressLineTown = record[10] #stores town/city name input 
    self.postcode = record[11] #stores postcode input

  
  #generates unique 10 digit ID
  def generateNHSId(self): 
    nhsId = [] #creates an empty array for the NHS ID
    for x in range (0,10): #generates a 10 digit number
      number_generator = random.randint(0,9) #generates a random number from 0 to 9
      nhsId.append(number_generator) #adds the value to the array
    newNhsId = "" #creates an empty string
    self.delimiter = "," #sets a delimiter
    for element in nhsId: #goes through each element in the nhs id
     newNhsId += str(element) #converts each element into a string as the value does not need to be treated as an integer
    with open("Patients.csv") as file: #opens patient file
      for line in file: #reads each line (record)
        line = line.split(self.delimiter) #splits the line upon an occurence of a delimiter so each element can be treated as a separate value
        if line[0] == newNhsId: #if the first element is equal to the NHS ID generated
          self.generateNHSId() #generates new nhs id if it has been taken
        else:
          continue
    return newNhsId #returns the nhs id as a field value for the record
  

  #save record
  def saveRecord(self):
    self.nhsID = self.generateNHSId() #collects NHS ID from a separate subroutine
    self.delimiter = "," #sets a delimiter
    self.record = self.nhsID + self.delimiter + self.forename + self.delimiter + self.surname + self.delimiter + self.dateOfBirth + self.delimiter + self.gender + self.delimiter + self.ethnicity + self.delimiter + self.allergies + self.delimiter + self.numberOfCovidVaccines + self.delimiter + self.numberOfCovidCases + self.delimiter + self.addressLineOne +  self.delimiter + self.addressLineTwo + self.delimiter + self.addressLineTown + self.delimiter + self.postcode #adds each field to create a record
    with open ("Patients.csv", "a") as patientFile: #opens the patient file for appending
      patientFile.write("\n") #writes a new line to the file
      patientFile.write(self.record) #writes the record to the file