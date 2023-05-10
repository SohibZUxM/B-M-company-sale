class Employee:
    def __init__(self, name, id, department, jobTitle, basicSalary, dateOfBirth, passportDetails, managerId):
        self.name = name
        self.id = id
        self.department = department
        self.jobTitle = jobTitle
        self.basicSalary = basicSalary
        self.dateOfBirth = dateOfBirth
        self.passportDetails = passportDetails
        self.managerId = managerId


#root.grid_rowconfigure(4, minsize=100)