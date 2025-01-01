#importing libraries which will be referenced later
import time 
from Patient import Patient #enables the patient class file to be linked to the main file
import matplotlib.pyplot as plt #enables the creation of the scattergraph
from datetime import datetime 
from collections import Counter 
import tkinter as tk
from tkinter import *
#from functools import partial
#import os
#import re
import os.path

global delimiter
delimiter = ","  #sets the delimiter in the patient file, which will be referenced later on

existenceOfFile = os.path.isfile("Patients.csv")  #determines if the patient file exists
if existenceOfFile == False:
    with open("Patients.csv", "w") as patientFile:
        string = "NHS ID, Forename, Surname, Age, Gender, Ethnicity, Allergies, Number of COVID-19 Vaccines, Number of COVID-19 Cases, Address Line One, Address Line Two, Town/City, Postcode"  #sets the first line of the patient file
        patientFile.write(string)  #writes the first line to file
else:
  global numberOfLines
  numberOfLines = 0  #setting the initial number of lines to 0
  with open("Patients.csv","r") as file:  #opens the patient file for reading
    for i in file:  #reads each line of the patient file
      numberOfLines += 1  #adds one to the variable each time there is an additional number of lines

def deleteUserNotFoundScreen():
  userNotFoundScreen.destroy()

# Designing popup for value not found 
def userNotFound(value): 
  global userNotFoundScreen
  userNotFoundScreen = Toplevel(loginScreen) #uses the same screen defined in the 'loginScreen' subroutine
  if value == 1: #displays message if login details are not valid
    title = "Invalid Entry" #sets title
    message = "Incorrect Username or Password" #sets output text
  else: #displays message if co-ordinates haven't been found
    title = "Error" #sets title
    if value == 0: #displays message if co-ordinates haven't been found
      message = "No Co-Ordinates Found" #sets output text
    else: #displays message if records haven't been found
      message = "No Records Found" #sets output text
  userNotFoundScreen.title(title) #sets title
  userNotFoundScreen.geometry("150x100") #sets dimensions
  Label(userNotFoundScreen, text=message).pack() #displays error message
  Button(userNotFoundScreen, text="OK", command=deleteUserNotFoundScreen).pack() #deletes the popup once the button is pressed
  
def plot(value): #creates scatter diagram
  if value == 1: #performs if statment if specific values are being plotted
    fieldChoice1 = fieldChoice #stores field choice
    operatorChoice1 = operatorChoice #stores operator choice
    inputValue1 = inputValue #stores input value
    if fieldChoice1 == "Forename":
      comparisonValue = 1 #sets element to be checked
    elif fieldChoice1 == "Surname":
      comparisonValue = 2 #sets element to be checked
    elif fieldChoice1 == "Date of Birth":
      comparisonValue = 3 #sets element to be checked
      inputValue1 = time.strptime(inputValue, "%d/%m/%Y")
    elif fieldChoice1 == "Gender":
      comparisonValue = 4 #sets element to be checked
    elif fieldChoice1 == "Ethnicity Number":
      comparisonValue = 5 #sets element to be checked
      inputValue1 = inputValue2.strip() #stores input value
    elif fieldChoice1 == "Allergies":
      comparisonValue = 6 #sets element to be checked
      if inputValue1 == '0':
        inputValue1 = "N/A" #replaces input value to whats stored in database
      else:
        inputValue1 = inputValue2 #stores input value
    elif fieldChoice1 == "Number of COVID-19 Vaccines":
      comparisonValue = 7 #sets element to be checked
    elif fieldChoice1 == "Number of COVID-19 Cases": 
      comparisonValue = 8 #sets element to be checked
    elif fieldChoice1 == "Town/City":
      comparisonValue = 11 #sets element to be checked
    elif fieldChoice1 == "Postcode":
      comparisonValue = 12 #sets element to be checked
  plt.figure(figsize=(3,3)) #sets dimensions of scatter diagram 
  column = 0
  noOfVaccines = [] #sets an empty array for the number of covid vaccines
  noOfCovidCases = [] #sets an empty array for the number of covid cases
  with open("Patients.csv") as file: #opens the patient file
    record = [line.split(delimiter) for line in file] #splits the record each time a delimiter is encountered
    for element in record: #reads each element in the record
      column+=1 
      if column == 1:
        continue #ignore header row
      if value == 1:
        element[comparisonValue] = element[comparisonValue].strip() #removes new line statement
        if fieldChoice1 == "Date of Birth":
          element[comparisonValue] = time.strptime(element[comparisonValue], "%d/%m/%Y") #makes date variable comparable
        if operatorChoice1 == "=":
          if element[comparisonValue] == inputValue1:
            noOfVaccines.append(element[7]) #adds the element number of vaccines to the array 
            noOfCovidCases.append(element[8]) #adds the element number of covid cases to the array 
        elif operatorChoice1 == "!=":
          if element[comparisonValue] != inputValue1:
            noOfVaccines.append(element[7]) #adds the element number of vaccines to the array 
            noOfCovidCases.append(element[8]) #adds the element number of covid cases to the array
        elif operatorChoice1 == "<":
          if element[comparisonValue] < inputValue1:
            noOfVaccines.append(element[7]) #adds the element number of vaccines to the array 
            noOfCovidCases.append(element[8]) #adds the element number of covid cases to the array
        elif operatorChoice1 == "<=":
          if element[comparisonValue] <= inputValue1:
            noOfVaccines.append(element[7]) #adds the element number of vaccines to the array 
            noOfCovidCases.append(element[8]) #adds the element number of covid cases to the array
        elif operatorChoice1 == ">":
          if element[comparisonValue] > inputValue1:
            noOfVaccines.append(element[7]) #adds the element number of vaccines to the array 
            noOfCovidCases.append(element[8]) #adds the element number of covid cases to the array
        elif operatorChoice1 == ">=":
          if element[comparisonValue] >= inputValue1:
            noOfVaccines.append(element[7]) #adds the element number of vaccines to the array 
            noOfCovidCases.append(element[8]) #adds the element number of covid cases to the array
      else:
        noOfVaccines.append(element[7]) #adds the element number of vaccines to the array 
        noOfCovidCases.append(element[8]) #adds the element number of covid cases to the array 
  combinedLists = zip(noOfVaccines,noOfCovidCases)  #combines the two lists
  convertToList = list(combinedLists) #converts variable to list
  repetitions = Counter(convertToList) #determines how many times coordinates are repeated
  combinedLists = list(repetitions.keys()) #returns the values in order of insertion
  noOfVaccines = [] #creating a new array
  noOfCovidCases = [] #creating a new array
  for i in combinedLists: #goes through each pair 
    noOfVaccines.append(i[0]) #adds the value in the zeroth position to the number of vaccines
    noOfCovidCases.append(i[1]) #adds the value in the zeroth position to the number of covid cases
  if not noOfVaccines: #determines if list is empty
    userNotFound(0) #points to subroutine
    return #exits subroutine
  repetitions = list(repetitions.values()) #determines the number of coordinates for each coordinate
  x = [noOfVaccines]; y = [noOfCovidCases]; s = [repetitions] #sets scatter values
  plt.scatter(x,y,s) #adds plots to diagram
  plt.title("Relationship Between The Number of COVID-19 Vaccines and The Number of COVID-19 Cases") #setting title
  plt.xlabel("Number of COVID-19 Vaccines") #setting x axis
  plt.ylabel("Number of COVID-19 Cases") #setting y axis
  plt.show() #displays scatter diagram

def mainScreen(): #creates mainscreen
  global accessLevel
  global mainScreen
  mainScreen = Tk() #creates screen
  mainScreen.geometry("300x250") #sets geometry of screen
  mainScreen.title("Hospital Database") #sets screen name 
  Label(text="Select Access Level", width="300", height="2", font=("Calibri", 13)).pack() #screen title
  Label(text="").pack() #creates a space between labels
  #creating buttons for user access level options
  Button(text="Patient", height="2", width="30", command = patientLogin).pack() #creates button
  Label(text="").pack() #creates a space between labels
  Button(text="Nurse", height="2", width="30", command = lambda accessLevel = "Nurse":login(accessLevel)).pack() #creates button
  Label(text="").pack()#creates a space between labels
  Button(text="Doctor", height="2", width="30", command = lambda accessLevel = "Doctor":login(accessLevel)).pack() #creates button
  Label(text="").pack()#creates a space between labels
  Button(text="Scientist", height="2", width="30", command = lambda accessLevel = "Scientist":login(accessLevel)).pack() #creates button
  Label(text="").pack()#creates a space between labels
  Button(text="Government Official", height="2", width="30", command = lambda accessLevel = "Government Official":login(accessLevel)).pack() #creates button
  Label(text="").pack()#creates a space between labels
  Button(text="Register", height="2", width="30", command = register).pack() #displays register button
  mainScreen.mainloop() #keeps screen open until user clicks 'X'


def mainMenu1(accessLevel): #creates first main menu
  global mainMenu
  mainMenu = Toplevel(mainScreen) #creates screen using the one defined in the subroutine 'mainScreen'
  mainMenu.geometry("300x250") #sets dimesnison
  mainMenu.title("Options") #sets title
  Label(mainMenu, text="Select Function", width="300", height="2", font=("Calibri", 13)).pack() #sets screen title
  Label(mainMenu,text="").pack() #creates empty space between labels
  #creating buttons for user options
  Button(mainMenu,text="Enter Patient Details", height="2", width="30", command = patientDetails).pack() #creates button for function
  Label(mainMenu,text="").pack() #creates empty space between labels
  Button(mainMenu,text="Access Patient Record", height="2", width="30", command = patientLogin).pack() #creates button for function 
  Label(mainMenu,text="").pack() #creates empty space between labels
  Button(mainMenu,text="Access Multiple Values", height="2", width="30", command = multipleValues).pack() #creates button for function 
  Label(mainMenu,text="").pack() #creates empty space between labels
  Button(mainMenu,text="Access Entire Database", height="2", width="30", command=entireDatabase).pack() #creates button for function
  Label(mainMenu,text="").pack() #creates empty space between labels
  if accessLevel != "Nurse": #does not show this button if the access level is 'Nurse'
    Button(mainMenu,text="Scatter Diagram", height="2", width="30", command=lambda: plot(0)).pack() #creates button for function


def register(): #creates register screen
    global register_screen
    register_screen = Toplevel(mainScreen) 
    register_screen.title("Register") 
    register_screen.geometry("300x250")
    global username
    global password
    global usernameEntry
    global passwordEntry
    username = StringVar() #stores username input provided by user
    password = StringVar() #stores password input provided by user
    usernameLabel = Label(register_screen, text="Username * ").grid(row = 0, column = 0, sticky = 'w') #sets title of user input
    usernameEntry = tk.Entry(register_screen, textvariable=username) #enables user to enter data
    usernameEntry.grid(row = 0, column = 1) #sets position of entry bar
    passwordLabel = Label(register_screen, text="Password * ").grid(row = 1, column = 0, sticky = 'w')
    passwordEntry = tk.Entry(register_screen, textvariable=password, show='*')
    passwordEntry.grid(row = 1, column = 1)
    Button(register_screen, text="Register", width=10, height=1,command = registerValidation).grid(row = 2, column = 0) #enables inputs to be validated

def registerValidation(): #validates register input
  usernameInfo = username.get() #returns username input
  passwordInfo = password.get() #returns password input
  validDetails = True #initialises register inputs as true
  with open("LoginDetails.csv") as file: #opens login details file
    for line in file: #reads each line in the file
      line = line.strip("\n").split(delimiter) #removes "\n" from each line and splits it so each element in the line can be accessed separately
      if usernameInfo == line[0]: #checks if the username is in the line
        Label(register_screen, text="                                       ").grid(row = 2, column = 1) #overwrites previous messages
        Label(register_screen, text="Username Taken", fg="red", font=("calibri", 11)).grid(row = 2, column = 1) #outputs error message
        usernameEntry.delete(0, END) #clears username entry box for re-entry
        passwordEntry.delete(0, END) #clears password entry box for re-entry
        validDetails = False #sets details as invalid
  containsSpaces = usernameInfo.isspace() #checks if username contains spaces
  containsSpaces1 = passwordInfo.isspace() #checks if password contains spaces
  if usernameInfo == "" or containsSpaces == True or passwordInfo == "" or containsSpaces1 == True: #checks if entry boxes are empty
    Label(register_screen, text="                                       ").grid(row = 2, column = 1)
    invalidRegistrationOutput() #outputs error message
    validDetails = False
  if validDetails == True: #performs operations if the inputs are valid
    with open("LoginDetails.csv", "a") as file: #opens login details file for appending
      file.write("\n") #writes a new line to the file
      file.write(usernameInfo + delimiter + passwordInfo) #writes the username and password to file
      usernameEntry.delete(0, END)
      passwordEntry.delete(0, END)
      Label(register_screen, text="                        ").grid(row = 2, column = 1) #overwrites previous messages
      Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).grid(row = 2, column = 1) #prints success message for user

def invalidRegistrationOutput(): #outputs error message
    global userNotFoundScreen
    userNotFoundScreen = Toplevel(register_screen)
    userNotFoundScreen.title("Error")
    userNotFoundScreen.geometry("150x100")
    Label(userNotFoundScreen, text="Invalid Entry").pack() #outputs error message to user
    Button(userNotFoundScreen, text="OK", command=deleteUserNotFoundScreen).pack() #closes screen when button is pressed


def login(accessLevel): #creates login screen
  global loginScreen
  loginScreen = Toplevel(mainScreen) #uses the same login screen defined in the mainScreen subroutine
  loginScreen.title("Login") #sets title
  loginScreen.geometry("300x250") #sets dimensions
  global usernameVerify
  global passwordVerify
  usernameVerify = StringVar() #stores username input
  passwordVerify = StringVar() #stores password input 
  global usernameLoginEntry
  global passwordLoginEntry
  Label(loginScreen, text="Username * ").grid(row = 0, column = 0, sticky = 'w') #sets username label
  usernameLoginEntry = tk.Entry(loginScreen, textvariable=usernameVerify) #creates entry box
  usernameLoginEntry.grid(row = 0, column = 1) #positions entry box
  Label(loginScreen, text="Password * ").grid(row = 1, column = 0, sticky = 'w') #sets password label
  passwordLoginEntry = tk.Entry(loginScreen, textvariable=passwordVerify, show= '*') #creates entry box and displays input as asterisk
  passwordLoginEntry.grid(row = 1, column = 1) #sets entry box position
  Button(loginScreen, text="Login", width=10, height=1, command = lambda accessLevel = accessLevel:loginVerify(accessLevel)).grid(row = 2, column = 0) #creates button which onece pressed, enables user inputs to be verified

def patientLogin(): #creates login screen for patients
    global loginScreen
    loginScreen = Toplevel(mainScreen) #uses the same screen defined in the mainscreen
    loginScreen.title("Login") #sets title
    loginScreen.geometry("300x250") #sets dimensions
    Label(loginScreen, text="Enter the details below") #enables user to input NHS ID
    global usernameVerify
    usernameVerify = StringVar() #stores user input
    global usernameLoginEntry
    Label(loginScreen, text="NHS ID *").grid(row = 0, column = 0) #creates label
    usernameLoginEntry = tk.Entry(loginScreen, textvariable=usernameVerify) #creates entry bod
    usernameLoginEntry.grid(row = 0, column = 1) #positions entry box
    Button(loginScreen, text="Login", width=9, height=1, command = nhsIdEntry).grid(row = 0, column= 2) #creates button which points to validation

def nhsIdEntry(): #checks whether NHS ID is valid
  username1 = usernameVerify.get()
  usernameLoginEntry.delete(0, END)
  with open('Patients.csv') as file: #opens patient file for reading
    found = False #sets nhsId found as false
    for i in range(numberOfLines):
      line = file.readline() #reads each line in the patient file
      lineSplit = line.split(delimiter) #splits the line each time a delimited is identified
      if lineSplit[0] == username1: #if the first item in the line is the NHS ID
        global lineNumber
        lineNumber = i #print the record in the patient file
        found = True #changes found to true as nhsId has been found
        outputRecord(lineNumber,2,1) #prints record
        break
  if found != True:
    nhsIdNotFound() #displays error message

def outputRecord(c,a,b): #displays record
  with open("Patients.csv") as file:
    lines = file.readlines() #reads each line of the file
    header = lines[0].strip("\n") #uses first line as header
    if a == 2: #performs selection for outputting multiple records
      record = lines[c].strip("\n") #finds record containing NHS ID
    else:
      recordsToBeDisplayed = [] #empty list for records to be displayed
      recordsToBeDisplayed.append(lines[0].strip("\n").split(delimiter)) #adds fieldname line to list
      for line in lines[1:]: #reads each line of the database
        line = line.strip("\n")
        line = line.split(delimiter)
        fieldChoice1 = fieldChoice #stores field choice
        operatorChoice1 = operatorChoice #stores operator choice
        inputValue1 = inputValue #stores input value
        if fieldChoice1 == "Forename":
          comparisonValue = line[1] #sets element to be checked
        elif fieldChoice1 == "Surname":
          comparisonValue = line[2] #sets element to be checked
        elif fieldChoice1 == "Date of Birth":
          comparisonValue = line[3] #sets element to be checked
          inputValue1 = time.strptime(inputValue, "%d/%m/%Y")
        elif fieldChoice1 == "Gender":
          comparisonValue = line[4] #sets element to be checked
        elif fieldChoice1 == "Ethnicity Number":
          comparisonValue = line[5] #sets element to be checked
          inputValue1 = inputValue2.strip() #stores input value
        elif fieldChoice1 == "Allergies":
          comparisonValue = line[6] #sets element to be checked
          if inputValue1 == '0':
            inputValue1 = "N/A" #replaces input value to whats stored in database
          else:
            inputValue1 = inputValue2 #stores input value
        elif fieldChoice1 == "Number of COVID-19 Vaccines":
          comparisonValue = line[7] #sets element to be checked
        elif fieldChoice1 == "Number of COVID-19 Cases": 
          comparisonValue = line[8] #sets element to be checked
        elif fieldChoice1 == "Town/City":
          comparisonValue = line[11] #sets element to be checked
        elif fieldChoice1 == "Postcode":
          comparisonValue = line[12] #sets element to be checked
        if fieldChoice1 == "Date of Birth":
          comparisonValue = time.strptime(comparisonValue, "%d/%m/%Y") #makes date variable comparable
        if operatorChoice1 == "=": #determines operator which compares data
          if comparisonValue == inputValue1: #compares values
            recordsToBeDisplayed.append(line) #adds record to records to be displayed
        elif operatorChoice1 == "!=": #determines operator which compares data
          if comparisonValue != inputValue1: #compares values
            recordsToBeDisplayed.append(line) #adds record to records to be displayed
        elif operatorChoice1 == "<": #determines operator which compares data
          if comparisonValue < inputValue1: #compares values
            recordsToBeDisplayed.append(line) #adds record to records to be displayed
        elif operatorChoice1 == "<=": #determines operator which compares data
          if comparisonValue <= inputValue1: #compares values
            recordsToBeDisplayed.append(line) #adds record to records to be displayed
        elif operatorChoice1 == ">": #determines operator which compares data
          if comparisonValue > inputValue1: #compares values
            recordsToBeDisplayed.append(line) #adds record to records to be displayed
        elif operatorChoice1 == ">=": #determines operator which compares data
          if comparisonValue >= inputValue1: #compares values
            recordsToBeDisplayed.append(line) #adds record to records to be displayed
  header = header.split(delimiter) #separates line upon each instance of a delimiter
  if a == 2: #performs selection for outputting multiple records
    record = record.split(delimiter)  #separates line upon each instance of a delimiter
    columns = 2 #sets record columns
  else:
    columns = len(recordsToBeDisplayed)  #determines number of columns
    if columns == 1: 
      userNotFound(2) #produces error if no records were added
      return #exits subroutine
  screen = Tk() #creates a new screen
  screen.geometry("300x250") #sets screen dimensions
  if a == 2: #performs selection for outputting multiple records
    screen.title("{0}, {1}".format(record[2],record[1])) #sets the title of the screen to the users surname and forename
    outputValues = [(header),(record)] #sets output values
  else:
    screen.title("Records") #sets the title of the screen to 'Records'
  for i in range(columns): #reads each record
    for j in range(13): #reads each field
      if i == 0:
        addingValues = Entry(screen, width=26, fg='black',font=('Calibri',9,'bold')) #sets display design
      else:
        addingValues = Entry(screen, width=26, fg='black',font=('Calibri',9)) #sets display design
      addingValues.grid(row=i, column=j) #positions each field + record
      if a == 2:
        addingValues.insert(END, outputValues[i][j]) #adds values to grid
      else:
        addingValues.insert(END, recordsToBeDisplayed[i][j]) #adds values to grid


def loginVerify(accessLevel): #verifies login details
  username1 = usernameVerify.get() #gets username input
  password1 = passwordVerify.get() #gets password input
  usernameLoginEntry.delete(0, END) #clears username entry box
  passwordLoginEntry.delete(0, END) #clears password entry box
  found = False #states that the login has not been found
  with open("LoginDetails.csv") as file: #opens file for reading
    for line in file: #reads each line in the file
      line = line.strip("\n").split(delimiter) #removes "\n" from line
      if username1 == line[0] and password1 == line[1]: #checks if username and password inputs are in the file
        found = True #login credentials have been found
        break
  if found == False:
      userNotFound(1) #displays error message
  else:
    loginSuccess(accessLevel) #points to a success screen

def loginSuccess(accessLevel): #displays success message if login details are valid
  global loginSuccessScreen
  loginSuccessScreen = Toplevel(loginScreen) #uses the same screen as 'loginScreen'
  loginSuccessScreen.title("Success") #sets title
  loginSuccessScreen.geometry("150x100") #sets dimensions
  Label(loginSuccessScreen, text="Login Success").pack() #displays success message
  Button(loginSuccessScreen, text="OK", command=deleteLoginSuccess).pack() #closes screen when button is pressed
  mainMenu1(accessLevel)
 
def nhsIdNotFound(): #displays message if NHS ID is not valid
    global userNotFoundScreen
    userNotFoundScreen = Toplevel(loginScreen) #uses the same screen as 'loginScreen'
    userNotFoundScreen.title("Error") #sets title
    userNotFoundScreen.geometry("150x100") #sets dimensions
    Label(userNotFoundScreen, text="Patient Not Found").pack() #displays error message
    Button(userNotFoundScreen, text="OK", command=deleteUserNotFoundScreen).pack() #closes screen when button is pressed


 
#deleting popups
def deleteLoginSuccess():
    loginSuccessScreen.destroy()


def entireDatabase(): #displaying database
  database = [] #creates an empty list
  with open("Patients.csv") as file: #opens file for reading
    lines = file.readlines() #reads all records in file
  for record in lines: #goes through each record
    record = record.strip("\n")
    database.append(record.split(delimiter))#adds each record to the separate file
  root = Tk() #creates screen
  root.geometry("300x250") #sets dimensions
  root.title("Database") #sets title 
  for i in range(numberOfLines): #loops for the amount of record in the file
    for j in range(13): #loops for the number of fields in the file
      if i == 0:
        addingValues = Entry(root, width=26, fg='black',font=('Arial',8,'bold')) #makes header bold
      else:
        addingValues = Entry(root, width=26, fg='black',font=('Arial',9))
      addingValues.grid(row=i, column=j) #determines position of values
      addingValues.insert(END, database[i][j]) #adds values to screen

def multipleValues():
  global screen
  screen = tk.Tk() #creates screen
  screen.geometry("300x250") #sets dimensions
  screen.title("Access Multiple Values") #sets title 
  global inputEntry
  global input
  input = StringVar() #stores input value
  inputEntry = tk.Entry(screen, textvariable=input)
  inputEntry.grid(row = 3, column = 3, sticky = 'w')
  selectLabel = Label(screen, text="SELECT:").grid(row = 1, column = 0, sticky = 'w') #designs select label
  fromLabel = Label(screen, text="FROM:").grid(row = 2, column = 0, sticky = 'w') #designs from label
  databaseLabel = Label(screen, text="DATABASE").grid(row = 2, column = 1, sticky = 'w') #designs database label
  whereLabel = Label(screen, text="WHERE:").grid(row = 3, column = 0, sticky = 'w') #designs where label 

  global fieldNames
  fieldNames = [
        "Forename",
        "Surname",
        "Date of Birth",
        "Gender",
        "Ethnicity Number",
        "Allergies",
        "Number of COVID-19 Vaccines",
        "Number of COVID-19 Cases",
        "Town/City",
        "Postcode"
      ] #dropdown menu options
  
  global fieldName
  fieldName = tk.StringVar(screen) #sets datatype of menu text
  fieldName.set("FieldName") #sets initial menu text

  def selected(choice): #determines value chosen by user
    operators = operators1 #stores operator vaue
    global selectChoice
    selectChoice = option.get() #stores option value
    global fieldChoice
    fieldChoice = fieldName.get() #stores fieldname choice 
    if fieldChoice == "Forename" or fieldChoice == "Surname" or fieldChoice == "Gender" or fieldChoice == "Allergies" or fieldChoice == "Town/City" or fieldChoice == "Postcode":
      operators = [
      "=",
      "!="
    ] #dropdown menu options
    if choice == "Ethnicity Number":
      ethnicitiesList1() #displays ethnicites list if ethnicity number field name is chosen
    global operatorChoice
    operatorChoice = operator.get() #stores operator choice
    (OptionMenu(screen , operator , *operators,command=selected)).grid(row = 3, column = 2, sticky = 'w') #replaces previous operator drop-down menu
  
  global option
  option = tk.StringVar(screen) #sets datatype of menu text
  option.set("Options") #sets initial menu text
  
  options = [
  "Record",
  "Scatter Diagram Co-Ordinates"
  #dropdown menu options
] 
  (OptionMenu(screen , option , *options,command=selected)).grid(row = 1, column = 1, sticky = 'w') #positions options menu button
  
  (OptionMenu(screen , fieldName , *fieldNames, command = selected)).grid(row = 3, column = 1, sticky = 'w') #positions fieldnames menu button 
    
  operators1 = [
    "=",
    "!=",
    "<",
    "<=",
    ">",
    ">=",
  ] #sets menu options

  global operator
  operator = tk.StringVar(screen) #sets datatype of menu text
  operator.set("Operator") #sets initial menu text
  
  #creates dropdown menu
  (OptionMenu(screen , operator , *operators1 )).grid(row = 3, column = 2, sticky = 'w') #positions operators menu button

  Button(screen,text="Apply",command=verifyEntry).grid(row=4,column=0,sticky='w') #validates user input

def verifyEntry(): #validates menu/entry values
  global inputValue
  inputValue = inputEntry.get() #stores user input
  error = False #sets flag as false
  try: #stores values
    selectChoice == "Options"
    fieldChoice == "FieldName"
    operatorChoice == "Operator"
  except NameError: #reports error if values have not been changed
    message = "Menu Value Must Be Amended" #sets error message
    error = True #sets error to true
  else:
    if selectChoice == "Options" or fieldChoice == "FieldName" or operatorChoice == "Operator": #checks menu values
      message = "Menu Value Must Be Amended" #reports error if menu values have not been changed
      error = True #sets error to true
    if fieldChoice == "Forename" or fieldChoice == "Surname" or fieldChoice == "Gender" or fieldChoice == "Allergies" or fieldChoice == "Town/City" or fieldChoice == "Postcode":
      if operatorChoice != "=" and operatorChoice != "!=":
        message = "Operator Value Must Be Amended" #reports error if menu values have not been changed
        error = True #sets error to true
    if inputValue == "": #checks if entry box is empty
      message = "Invalid Entry" #sets error message
      error = True #sets error to true
  if error == True: #performs code if error is found
    Label(screen, text="                                                      ").grid(row = 3, column =4) #overwrites previous messages 
    Label(screen, text=message,fg='red').grid(row = 3, column =4) #displays error message
    return False #ends function
  if fieldChoice == "Number of COVID-19 Cases" or fieldChoice == "Number of COVID-19 Vaccines" or fieldChoice == "Ethnicity Number":
    try: #determines if number is integer if specific fieldChoice which requires an integer is chosen
      int(inputValue)
    except ValueError: 
      Label(screen, text="                                                      ").grid(row = 3, column =4) #overwrites previous messages 
      Label(screen, text="Must Be A Whole Number",fg='red').grid(row = 3, column =4) #displays error message
      return False #ends function
    if fieldChoice == "Number of COVID-19 Cases" or fieldChoice == "Number of COVID-19 Vaccines":
      if int(inputValue) < 0: #checks if input is less than 0, which would be invalid
        Label(screen, text="                                                      ").grid(row = 3, column =4) #overwrites previous messages 
        Label(screen, text="Entry Must Be Greater Than One",fg='red').grid(row = 3, column =4) #displays error message
        return False #ends function
    else:
      if int(inputValue) <= 0 or int(inputValue) > numberOfLines-1: #checks if input is within range of list of ethnicites options
        Label(screen, text="                                                      ").grid(row = 3, column =4) #overwrites previous messages 
        Label(screen, text="Entry Must Be Between 1 and "+str(numberOfLines-1),fg='red').grid(row = 3, column =4) #displays error message
        return False #ends function
  global inputValue2
  if fieldChoice == "Ethnicity Number": #performs selection if fieldChoice is ethnicity number
    with open("Ethnicities.txt","r") as file: #opens ethnicities file
      lines = file.readlines() #reads all lines of file
      inputValue2 = lines[int(inputValue)-1] #determines input value (subtracted from 1 due to index starting from 0)
  elif fieldChoice == "Allergies": #performs selection if fieldChoice is allergies
    inputValue = inputValue.title() #sets format of input
    inputValue2 = inputValue.replace(" ,","|").replace(", ","|").replace("  ","") #converts input into format of the value which would be stored in the patients file
  elif fieldChoice == "Date of Birth": #performs selection if fieldChoice is date of birth
    try: 
      datetime.strptime(inputValue, '%d/%m/%Y') #determines if the date of birth given is in the format '%d/%m/%Y'
    except ValueError or UnboundLocalError: #if the input is not in the correct format
      Label(screen, text="                                                      ").grid(row = 3, column =4) #overwrites previous messages 
      Label(screen, text="Invalid Entry", fg="red").grid(row = 3, column =4) #displays error message
      return False #ends function
  if fieldChoice == "Forename" or fieldChoice == "Surname" or fieldChoice == "Town/City": #performs selection dependent on fieldChoice
    inputValue = inputValue.title() #sets format of input
  elif fieldChoice == "Gender" or fieldChoice == "Postcode": #performs selection dependent on fieldChoice
    inputValue = inputValue.upper() #sets format of input
  Label(screen, text="                                                         ").grid(row = 3, column =4) #overwrites previous messages  
  if selectChoice == "Scatter Diagram Co-Ordinates":
    plot(1) #points to subroutine if user wants to see plot values
  else:
    outputRecord(fieldChoice, operatorChoice, inputEntry)
  fieldName.set("FieldName") #sets original menu text
  operator.set("Operator") #sets original menu text
  option.set("Option") #sets original menu text
  inputEntry.delete(0, END) #clears entry box
  
    
def patientDetails(): #gathering patient detials
  global patientDetails
  patientDetails = Toplevel(mainScreen) #creates screen using screen from subroutine 'mainScreen'
  patientDetails.geometry("300x250") #sets dimensions
  patientDetails.title("Enter Patient Details") #sets title
  global forename
  forename = StringVar() #stores input
  Label(patientDetails, text="Forename:").grid(row = 0, column = 0, sticky = 'w') #creates label
  forename = tk.Entry(patientDetails, textvariable=forename) #creates entry box
  forename.grid(row = 0, column = 1) #sets position of entry box
  global surname
  surname = StringVar() #stores input 
  Label(patientDetails, text="Surname:").grid(row =1, column =0, sticky = 'w') #creates label
  surname = tk.Entry(patientDetails, textvariable=surname) #creates entry box
  surname.grid(row = 1, column = 1) #sets position of entry box
  global dateOfBirth
  dateOfBirth = StringVar() #stores input
  Label(patientDetails, text="Date of Birth (DD/MM/YYYY):").grid(row =2, column = 0, sticky = 'w') #creates label
  dateOfBirth = tk.Entry(patientDetails, textvariable=dateOfBirth) #creates entry box
  dateOfBirth.grid(row = 2, column = 1) #sets position of entry box
  global gender
  gender = StringVar() #stores input
  Label(patientDetails, text="Gender (M/F):").grid(row = 3, column = 0, sticky = 'w') #creates label
  gender = tk.Entry(patientDetails, textvariable=gender) #creates entry box
  gender.grid(row =3, column = 1) #sets position of entry box
  global ethnicity
  ethnicity = StringVar() #stores input
  Label(patientDetails, text="Enter Number Relating To Ethnicity:").grid(row = 4, column = 0, sticky = 'w') #creates label
  Button(patientDetails, text="List of Ethnicities", width="12", height="1", command = ethnicitiesList1).grid(row = 5, column = 0, sticky = 'w') #creates button to display ehtnicies to choose from
  ethnicity = tk.Entry(patientDetails, textvariable=ethnicity) #creates entry box
  ethnicity.grid(row = 4, column = 1) #sets position of entry box
  global allergies
  allergies = StringVar() #stores input
  Label(patientDetails, text="Allergies (Enter 0 If N/A):").grid(row = 6, column = 0, sticky = 'w') #creates label
  allergies = tk.Entry(patientDetails, textvariable=allergies) #creates entry box 
  allergies.grid(row =6, column = 1) #sets position of entry box
  global numberOfCovidVaccines
  numberOfCovidVaccines = StringVar() #stores input
  Label(patientDetails, text="Number Of COVID-19 Vaccines:").grid(row = 7, column = 0, sticky = 'w') #creates label
  numberOfCovidVaccines = tk.Entry(patientDetails, textvariable=numberOfCovidVaccines) #creates entry box
  numberOfCovidVaccines.grid(row = 7, column = 1) #sets position of entry box
  global numberOfCovidCases
  numberOfCovidCases = StringVar() #stores input
  Label(patientDetails, text="Number of COVID-19 Cases:").grid(row =8, column = 0, sticky = 'w') #creates label
  numberOfCovidCases = tk.Entry(patientDetails, textvariable=numberOfCovidCases) #creates entry box
  numberOfCovidCases.grid(row = 8, column = 1) #sets position of entry box
  global addressLineOne
  addressLineOne = StringVar() #stores input
  Label(patientDetails, text="Address Line One:").grid(row = 9, column = 0, sticky = 'w') #creates label
  addressLineOne = tk.Entry(patientDetails, textvariable=addressLineOne) #creates entry box
  addressLineOne.grid(row = 9, column = 1) #sets position of entry box
  global addressLineTwo
  addressLineTwo = StringVar() #stores input
  Label(patientDetails, text="Address Line Two:").grid(row = 10, column = 0, sticky = 'w') #creates label
  addressLineTwo = tk.Entry(patientDetails, textvariable=addressLineTwo) #creates entry box
  addressLineTwo.grid(row = 10, column = 1) #sets position of entry box
  global addressLineTown
  addressLineTown = StringVar() #stores input
  Label(patientDetails, text="Town/City:").grid(row = 11, column = 0, sticky = 'w') #creates label
  addressLineTown = tk.Entry(patientDetails, textvariable=addressLineTown) #creates entry box
  addressLineTown.grid(row = 11, column = 1) #sets position of entry box
  global postcode
  postcode = StringVar() #stores input
  Label(patientDetails, text="Postcode:").grid(row = 12, column = 0, sticky = 'w') #creates label
  postcode = tk.Entry(patientDetails, textvariable=postcode) #creates entry box
  postcode.grid(row = 12, column = 1) #sets position of entry box
  buttonRefresh = Button(patientDetails, text="Done", width=10, height=1, command = detailsVerify).grid(row = 13, column = 0, sticky = 'w') #creates button which verifies details once pressed

def detailsVerify(): #validating patient details
  validateForename = nameValidate(forename.get().title(),1) #stores results of input validation
  validateSurname = nameValidate(surname.get().title(),2) #stores results of input validation
  validateDateOfBirth = dateOfBirthValidate(dateOfBirth.get()) #stores results of input validation
  validateGender = genderValidate(gender.get().capitalize()) #stores results of input validation
  validateEthnicity = ethnicityValidate(ethnicity.get()) #stores results of input validation
  validateAllergies = allergiesValidate(allergies.get().title()) #stores results of input validation
  validateNumberOfCovidVaccines = numberValidate(numberOfCovidVaccines.get(),1) #stores results of input validation
  validateNumberOfCovidCases = numberValidate(numberOfCovidCases.get(),2) #stores results of input validation
  validateAddressLineOne = nameValidate(addressLineOne.get().title(),3) #stores results of input validation
  validateAddressLineTwo = nameValidate(addressLineTwo.get().title(),4) #stores results of input validation
  validateAddressLineTown = nameValidate(addressLineTown.get().title(),5) #stores results of input validation
  validatePostcode = postcodeValidate(postcode.get().upper()) #stores results of input validation
  if validateForename == False or validateSurname == False or validateDateOfBirth == False or validateGender == False or validateEthnicity == False or validateAllergies == False or validateNumberOfCovidVaccines == False or validateNumberOfCovidCases == False or validateAddressLineOne == False or validateAddressLineTwo == False or validateAddressLineTown == False or validatePostcode == False: #if any of the inputs aren't valid
    Label(patientDetails, text="                        ").grid(row = 13, column = 1) #overwrites prior messages
  else:
   record = [validateForename,validateSurname,validateDateOfBirth,validateGender,validateEthnicity,validateAllergies,validateNumberOfCovidVaccines, validateNumberOfCovidCases,validateAddressLineOne,validateAddressLineTwo,validateAddressLineTown,validatePostcode] #creating record
   Label(patientDetails, text="Record Added", fg="green", font=("calibri", 10)).grid(row = 13, column = 1) #displaying success message
   submitDetails(record) #passing details to patient class to sdd to csv file
   forename.delete(0, END) #clears entry box
   surname.delete(0, END) #clears entry box
   dateOfBirth.delete(0, END) #clears entry box
   gender.delete(0, END) #clears entry box
   ethnicity.delete(0, END) #clears entry box
   allergies.delete(0, END) #clears entry box
   numberOfCovidVaccines.delete(0, END) #clears entry box
   numberOfCovidCases.delete(0, END) #clears entry box
   addressLineOne.delete(0, END) #clears entry box
   addressLineTwo.delete(0, END) #clears entry box
   addressLineTown.delete(0, END) #clears entry box
   postcode.delete(0, END) #clears entry box
   
def nameValidate(variableBeingValidated,numberOfVariableBeingValidated): #validating the inputs: forename, surname, addressLineOne, addressLineTwo and addressLineTown 
  messsage = "Too Short" #error message
  if len(variableBeingValidated) < 2: #while the variable being validated has less than two characters
    if numberOfVariableBeingValidated == 1: #forename
     Label(patientDetails, text=messsage, fg="red", font=("calibri", 10)).grid(row = 0, column =3) #error message outputted
    elif numberOfVariableBeingValidated == 2: #surname
     Label(patientDetails, text=messsage, fg="red", font=("calibri", 10)).grid(row = 1, column =3) #error message outputted
    elif numberOfVariableBeingValidated == 3: #addressLineOne
     Label(patientDetails, text=messsage, fg="red", font=("calibri", 10)).grid(row = 9, column =3) #error message outputted
    elif numberOfVariableBeingValidated == 4: #addressLineTwo
     Label(patientDetails, text=messsage, fg="red", font=("calibri", 10)).grid(row = 10, column =3) #error message outputted
    elif numberOfVariableBeingValidated == 5: #Town/City name
     Label(patientDetails, text=messsage, fg="red", font=("calibri", 10)).grid(row = 11, column =3) #error message outputted
    return False
  if numberOfVariableBeingValidated == 1: #forename
    Label(patientDetails, text="                       ").grid(row = 0, column = 3) #overwrites previous messages
  elif numberOfVariableBeingValidated == 2: #surname
    Label(patientDetails, text="                       ").grid(row = 1, column = 3) #overwrites previous messages
  elif numberOfVariableBeingValidated == 3: #addressLineOne
    Label(patientDetails, text="                       ").grid(row = 9, column = 3) #overwrites previous messages
  elif numberOfVariableBeingValidated == 4: #addressLineTwo
    Label(patientDetails, text="                       ").grid(row = 10, column = 3) #overwrites previous messages
  elif numberOfVariableBeingValidated == 5: #Town/City name
    Label(patientDetails, text="                       ").grid(row = 11, column = 3) #overwrites previous messages
  return variableBeingValidated #returns the value of the validated variable as an element in the record  

def dateOfBirthValidate(dateOfBirth): #validating date of birth input
  try: 
    datetime.strptime(dateOfBirth, '%d/%m/%Y') #determines if the date of birth given is in the format '%d/%m/%Y'
  except ValueError or UnboundLocalError: #if the input is not in the correct format
    Label(patientDetails, text="Invalid Entry", fg="red", font=("calibri", 10)).grid(row = 2, column = 3) #displays and positions error message
    return False #the input is not valid 
  Label(patientDetails, text="                       ").grid(row = 2, column = 3) #overwrites previous message
  return dateOfBirth #returns the value of the validated variable as an field in the record

def genderValidate(gender): #validate gender input
  if gender != "M" and gender != "F": #while the gender is not equal to male or female
    Label(patientDetails, text="Invalid Entry", fg="red", font=("calibri", 10)).grid(row = 3, column = 3) #displays and positions error message
    return False  #returns the value of the gender variable as an element in the record
  Label(patientDetails, text="                       ").grid(row = 3, column = 3) #overwrites previous message
  return gender #returns the value of the validated variable as a field in the record 
  
def allergiesValidate(allergies): #validate allergy input
  numbers = ["1","2","3","4","5","6","7","8","9","0"] #creating a list to store numbers
  number = False #initialising number in allergy input as false
  for element in allergies: #reads each element in the input
    if element in numbers: #checks if the element is a number
      number = True #returns true if allergy input contains a number
      break
  if allergies == "0": #if the patient has no allergies
    Label(patientDetails, text="                       ").grid(row = 6, column = 3) #overwrites previus error message
    return "N/A" #the value in the allergy filed should be set to not applicable
  elif number == True or allergies == "" or len(allergies) < 2: #checks if entry is blank, contains a number or has a length of less than 2
    Label(patientDetails, text="Invalid Entry", fg="red", font=("calibri", 10)).grid(row = 6, column = 3) #displays error message
    return False #indicates that the value is invalid
  allergies = allergies.replace(" ,","|").replace(", ","|").replace("  ","") #replacing delimiter so the allergy input takes up one element in the list
  Label(patientDetails, text="                       ").grid(row = 6, column = 3) #overwrites previus error message
  return allergies #returns the value of the validated variable as a field in the record

def determiningEthnicities():
  global validEthnicity
  validEthnicity = [] #sets the ethnicity as an array
  with open("Ethnicities.txt") as f: #opens the ethncities file
    for line in f: #reads through each line in the ethnicities file
      validEthnicity.append(line.replace("\n","")) #adds each line to the array declared earlier, and replaces the new line (at the end of each line) with empty string to remove prevent "\n" from being added to the array
  global lengthEthnicity
  lengthEthnicity = len(validEthnicity) #finds the length of the array
  return lengthEthnicity, validEthnicity #returns two values for use in 'ethnicityValidate' function
 
def ethnicitiesList1(): #displays list of ethnicities
  global ethnicitiesList
  ethnicitiesList = Toplevel(mainScreen) #creates screen using the one defined in 'mainScreen'
  ethnicitiesList.geometry("300x250") #sets timensions
  ethnicitiesList.title("List of Ethnicities") #sets title
  determiningEthnicities()
  for i in range(lengthEthnicity): #continues to iterate for the length of the the ethnicity list
    Label(ethnicitiesList, text=(str(i+1)+". "+validEthnicity[i])).pack() #prints each line in validEthnicity, with a number and fulvaluesop before it

def ethnicityValidate(ethnicity): #validating ethnicity
  if ethnicity == "":
    Label(patientDetails, text="Invalid Entry", fg="red", font=("calibri", 10)).grid(row = 4, column = 3) #displays error message if ethnicity is an empty string
    return False
  for character in ethnicity: #goes through each character in the ethnciity input
    if character.isalpha() == True: #checks if character is an alphabetical character
      Label(patientDetails, text="Invalid Entry", fg="red", font=("calibri", 10)).grid(row = 4, column = 3) #displays error message
      return False #indicates that the value is invalid
  lastDigit = int(repr(float(ethnicity))[-1]) #determines the last digit of the float number
  lengthEthnicity, validEthnicity = determiningEthnicities() #stores ethnicityLength and validated 
  if lastDigit != 0 or int(ethnicity) < 1 or int(ethnicity) > lengthEthnicity: 
    Label(patientDetails, text="Invalid Entry", fg="red", font=("calibri", 10)).grid(row = 4, column = 3) #error message
    return False #returns false if the input is not equal to one of the values specified in 'List of Ethnicities'
  validatedEthnicity = validEthnicity[int(ethnicity)-1] #returns ethnicity value
  Label(patientDetails, text="                       ").grid(row = 4, column = 3) #overwrites previous error messages
  return validatedEthnicity #returns the value of the validated variable as a field in the record
   
def postcodeValidate(postcode): #validate postcode
  postcode = postcode.replace(" ","") #removes spaces in postcode
  if len(postcode) < 2  or len(postcode) > 7: #continues the loop until the postcode has a standard length
    Label(patientDetails, text="Invalid Length", fg="red", font=("calibri", 10)).grid(row = 12, column = 3) #displays error message
    return False #indicates that the value is invalid
  for x in range (len(postcode)): #goes through each value in the postcode
    if x == 0: #if the value is the first value
      isAlpha = postcode[x].isalpha() #determines if the first value is in the alphabet
      if isAlpha == False: #loops until the first value of the postcode is in the alpahbet
        Label(patientDetails, text="Invalid Format", fg="red", font=("calibri", 10)).grid(row = 12, column = 3) #displays error message
        return False #indicates that the value is invalid
  Label(patientDetails, text="                       ").grid(row = 12, column = 3)
  return postcode #returns the value of the validated variable as a field in the record

def numberValidate(variableBeingValidated,numberOfVariableBeingValidated): #validating the inputs: numberOfCovidVaccines and numberOfCovidCases
  string = False #sets string occurences as false
  if variableBeingValidated == "":
    if numberOfVariableBeingValidated == 1: #numberOfCovidVaccines
      Label(patientDetails, text="Invalid Entry", fg="red",font= ("calibri", 10)).grid(row = 7, column = 3) #displays error message
    else: #numberOfCovidVaccines
      Label(patientDetails, text="Invalid Entry", fg="red", font=("calibri", 10)).grid(row = 8, column = 3) #displays error message
    return False #returns false if input is empty
  for index in range (len(variableBeingValidated)):
    if variableBeingValidated[index].isalpha() == True:
      string = True #sets string equal to true if input contains an alphabetical character
      if numberOfVariableBeingValidated == 1: #numberOfCovidVaccines
        Label(patientDetails, text="Invalid Entry", fg="red",font= ("calibri", 10)).grid(row = 7, column = 3) #displays error message
      else: #numberOfCovidCases
        Label(patientDetails, text="Invalid Entry", fg="red", font=("calibri", 10)).grid(row = 8, column = 3) #displays error message
      return False #returns false if the input contains a string
  lastDigit = int(repr(float(variableBeingValidated))[-1]) #provides gives the last digit of the variable "validatedNumber" 
  if lastDigit != 0 or int(variableBeingValidated) < 0: #checks if input is a float or greater than 1
    if numberOfVariableBeingValidated == 1: #numberOfCovidVaccines
      Label(patientDetails, text="Invalid Entry", fg="red", font=("calibri", 10)).grid(row = 7, column = 3) #displays error message
    else: #numberOfCovidCases
      Label(patientDetails, text="Invalid Entry", fg="red", font=("calibri", 10)).grid(row = 8, column = 3) #displays error message
    return False #indicates that the value is invalid
  if numberOfVariableBeingValidated == 1:#numberOfCovidVaccines
    Label(patientDetails, text="                       ").grid(row = 7, column = 3) #overwrites previous error message
  else: #numberOfCovidCases
    Label(patientDetails, text="                        ").grid(row = 8, column = 3) #overwrites previous error message
  return variableBeingValidated #returns the value of the validated variable as a field in the record

def submitDetails(detailsVerify): #enables user to submit the details of a new patient
  record = detailsVerify #jumps to another subroutine in order to collect inputs which will form the record
  patient = Patient(record) #provides the record to the Patient class, which will then combine the NHS ID with the other elements in the record
  patient.saveRecord() #jumps to a subroutine in the Patient class where the record is written to file
  
mainScreen() #starts program