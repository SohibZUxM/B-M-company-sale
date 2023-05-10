import os
import pickle
import tkinter as tk
from tkinter import *
from tkinter import PhotoImage, messagebox, ttk

from Employee import Employee
from Car import Car
from Sale import Sale


root = tk.Tk()
root.title("Sales & Employees Management")
root['padx'] = 100

title_label = tk.Label(root, text="B&M Company", font=("Arial", 16, "bold"))
title_label.grid(row=0, columnspan=4, pady=20)

# Editable Prefilled Dialogs

def employee_editing_dialog( employeeIndexInDatabase, defaultEmployee: Employee):
    # Create a new dialog window
    dialog = Toplevel()

    # Set the title of the dialog window
    dialog.title("Edit Employee")

    # Set the minimum size of the dialog window
    dialog.minsize(width=300, height=300)

    # Set the padding of the dialog window
    dialog['padx'] = 20
    dialog['pady'] = 20

    # print("Editing employee by Name: " + eName)

    # Create the labels and entry boxes for each field
    name_label = ttk.Label(dialog, text="Name:")
    name_label.grid(column=0, row=0, sticky="W", pady=1)
    name_entry = ttk.Entry(dialog)
    name_entry.insert(0,defaultEmployee.name)
    name_entry.grid(column=1, row=0, pady=1)

    id_label = ttk.Label(dialog, text="ID:")
    id_label.grid(column=0, row=1, sticky="W", pady=1)
    id_entry = ttk.Entry(dialog)
    id_entry.insert(0,defaultEmployee.id)
    id_entry.grid(column=1, row=1, pady=1)

    department_label = ttk.Label(dialog, text="Department:")
    department_label.grid(column=0, row=2, sticky="W", pady=1)
    department_entry = ttk.Entry(dialog)
    department_entry.insert(0,defaultEmployee.department)
    department_entry.grid(column=1, row=2, pady=1)

    job_title_label = ttk.Label(dialog, text="Job Title:")
    job_title_label.grid(column=0, row=3, sticky="W", pady=1)
    job_title_entry = ttk.Entry(dialog)
    job_title_entry.insert(0,defaultEmployee.jobTitle)
    job_title_entry.grid(column=1, row=3, pady=1)

    basic_salary_label = ttk.Label(dialog, text="Basic Salary:")
    basic_salary_label.grid(column=0, row=4, sticky="W", pady=1)
    basic_salary_entry = ttk.Entry(dialog)
    basic_salary_entry.insert(0,defaultEmployee.basicSalary)
    basic_salary_entry.grid(column=1, row=4, pady=1)

    dob_label = ttk.Label(dialog, text="Date of Birth (DD.MM.YYYY):")
    dob_label.grid(column=0, row=5, sticky="W", pady=1)
    dob_entry = ttk.Entry(dialog)
    dob_entry.insert(0,defaultEmployee.dateOfBirth)
    dob_entry.grid(column=1, row=5, pady=1)

    passport_details_label = ttk.Label(dialog, text="Passport Details:")
    passport_details_label.grid(column=0, row=6, sticky="W", pady=1)
    passport_details_entry = ttk.Entry(dialog)
    passport_details_entry.insert(0,defaultEmployee.passportDetails)
    passport_details_entry.grid(column=1, row=6, pady=1)

    manager_id_label = ttk.Label(dialog, text="Manager ID (for sales person only):")
    manager_id_label.grid(column=0, row=7, sticky="W", pady=1)
    manager_id_entry = ttk.Entry(dialog)
    manager_id_entry.insert(0,defaultEmployee.managerId)
    manager_id_entry.grid(column=1, row=7, pady=1)

    # Create a frame to hold the buttons
    button_frame = ttk.Frame(dialog)
    button_frame.grid(column=0, row=8, columnspan=2, pady=10)

    # Create the Add and Cancel buttons
    add_button = ttk.Button(button_frame, text="Delete", command=lambda: deleteEmployeeDataByIndex(dialog, employeeIndexInDatabase) )
    add_button.pack(side=LEFT, padx=5)

    add_button = ttk.Button(button_frame, text="Save", command=lambda:updateEmployeeDataByIndex( dialog,employeeIndexInDatabase, Employee(
        name_entry.get(),
        id_entry.get(),
        department_entry.get(),
        job_title_entry.get(),
        basic_salary_entry.get(),
        dob_entry.get(),
        passport_details_entry.get(),
        manager_id_entry.get()
    )) )
    add_button.pack(side=LEFT, padx=5)

    cancel_button = ttk.Button(button_frame, text="Cancel", command=dialog.destroy)
    cancel_button.pack(side=LEFT, padx=5)

    # Set the focus to the name entry box
    name_entry.focus()

    # Wait for the dialog window to be closed
    dialog.wait_window()
def car_editing_dialog( carIndexInDatabase, defaultCar: Car ):
    # Create a new dialog window
    dialog = Toplevel()

    # Set the title of the dialog window
    dialog.title("Edit Car")

    # Set the minimum size of the dialog window
    dialog.minsize(width=300, height=300)

    # Set the padding of the dialog window
    dialog['padx'] = 20
    dialog['pady'] = 20

    # Create the labels and entry boxes for each field
    name_label = ttk.Label(dialog, text="Name:")
    name_label.grid(column=0, row=0, sticky="W", pady=1)
    name_entry = ttk.Entry(dialog)
    name_entry.insert(0, defaultCar.name)
    name_entry.grid(column=1, row=0, pady=1)

    id_label = ttk.Label(dialog, text="ID:")
    id_label.grid(column=0, row=1, sticky="W", pady=1)
    id_entry = ttk.Entry(dialog)
    id_entry.insert(0, defaultCar.id)
    id_entry.grid(column=1, row=1, pady=1)

    price_label = ttk.Label(dialog, text="Price:")
    price_label.grid(column=0, row=2, sticky="W", pady=1)
    price_entry = ttk.Entry(dialog)
    price_entry.insert(0, defaultCar.price)
    price_entry.grid(column=1, row=2, pady=1)

    type_label = ttk.Label(dialog, text="Type:")
    type_label.grid(column=0, row=3, sticky="W", pady=1)
    type_entry = ttk.Entry(dialog)
    type_entry.insert(0, defaultCar.type)
    type_entry.grid(column=1, row=3, pady=1)

    fuelCapacity_label = ttk.Label(dialog, text="Fuel Capacity:")
    fuelCapacity_label.grid(column=0, row=4, sticky="W", pady=1)
    fuelCapacity_entry = ttk.Entry(dialog)
    fuelCapacity_entry.insert(0, defaultCar.fuelCapacity)
    fuelCapacity_entry.grid(column=1, row=4, pady=1)

    maxSpeed_label = ttk.Label(dialog, text="Max Speed:")
    maxSpeed_label.grid(column=0, row=5, sticky="W", pady=1)
    maxSpeed_entry = ttk.Entry(dialog)
    maxSpeed_entry.insert(0, defaultCar.maxSpeed)
    maxSpeed_entry.grid(column=1, row=5, pady=1)

    color_label = ttk.Label(dialog, text="Color:")
    color_label.grid(column=0, row=6, sticky="W", pady=1)
    color_entry = ttk.Entry(dialog)
    color_entry.insert(0, defaultCar.color)
    color_entry.grid(column=1, row=6, pady=1)

    # Create a frame to hold the buttons
    button_frame = ttk.Frame(dialog)
    button_frame.grid(column=0, row=7, columnspan=2, pady=10)

    # Create the Add and Cancel buttons
    add_button = ttk.Button(button_frame, text="Delete", command=lambda: deleteCarDataByIndex(dialog, carIndexInDatabase))
    add_button.pack(side=LEFT, padx=5)

    add_button = ttk.Button(button_frame, text="Save", command=lambda: updateCarDataByIndex(dialog, carIndexInDatabase, Car (
            name_entry.get(),
            id_entry.get(),
            price_entry.get(),
            type_entry.get(),
            fuelCapacity_entry.get(),
            maxSpeed_entry.get(),
            color_entry.get()
        ))
    )
    add_button.pack(side=LEFT, padx=5)

    cancel_button = ttk.Button(button_frame, text="Cancel", command=dialog.destroy)
    cancel_button.pack(side=LEFT, padx=5)

    # Set the focus to the name entry box
    name_entry.focus()

    # Wait for the dialog window to be closed
    dialog.wait_window()

def sale_viewing_dialog( sales=[] ):
    # Create a new dialog window
    dialog = Toplevel()


    #Getting employee name
    allEmployees = []
    if os.path.exists("Employees.pickle"):
        with open("Employees.pickle", "rb") as handle:
            allEmployees = pickle.load(handle)

    employeeName = ""
    for employee in allEmployees:
        if ( employee.id == sales[0].salesPersonId ):
            employeeName = employee.name
            break


    # Set the title of the dialog window
    dialog.title("Sales by " + employeeName)

    treeview_frame = tk.Frame(dialog)
    treeview_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    treeview_scrollbar = tk.Scrollbar(treeview_frame)
    treeview_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    treeview = ttk.Treeview(treeview_frame, columns=("carName", "salePrice", "personName", "carId"),
                                    yscrollcommand=treeview_scrollbar.set)
    treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    treeview_scrollbar.config(command=treeview.yview)

    treeview.heading("#0", text="N0", anchor="w")
    treeview.column("#0", anchor="w")
    treeview.heading("carName", text="Car Name", anchor="w")
    treeview.column("carName", anchor="w")
    treeview.heading("salePrice", text="Sale Price", anchor="w")
    treeview.column("salePrice", anchor="w")
    treeview.heading("personName", text="Person Name", anchor="w")
    treeview.column("personName", anchor="w")
    treeview.heading("carId", text="Car ID", anchor="w")
    treeview.column("carId", anchor="w")

    saleIndex = 0
    for sale in sales:
        saleIndex += 1
        car = getCarById(sale.carId)
        if ( car != None ):
            treeview.insert("", tk.END, text=saleIndex, values=(car.name, sale.salePrice, employeeName, sale.carId) )
        else:
            treeview.insert("", tk.END, text=saleIndex, values=("Unknown", sale.salePrice, employeeName, sale.carId) )

    # Wait for the dialog window to be closed
    dialog.wait_window()

def salaries_viewing_dialog():
    # Create a new dialog window
    dialog = Toplevel()

    
     


    # Getting all employees
    allEmployees = []
    isEmployeeManager = [0] * 99999999
    if os.path.exists("Employees.pickle"):
        with open("Employees.pickle", "rb") as handle:
            allEmployees = pickle.load(handle)
    
    for employee in allEmployees:
        if ( not("manager" in str(employee.jobTitle).lower()) ):
            isEmployeeManager[int(employee.id)] = False
        else:
            isEmployeeManager[int(employee.id)] = True

    # Getting all sales
    allSales = []
    if os.path.exists("Sales.pickle"):
        with open("Sales.pickle", "rb") as handle:
            allSales = pickle.load(handle)

    
    allSalesEarningsSumByEmployee = [0] * 99999999
    
    # Setting to 0
    for sale in allSales:
        allSalesEarningsSumByEmployee[int(sale.salesPersonId)] = 0

    # Sum for SalesPersons
    for sale in allSales:
        if ( not isEmployeeManager[int(sale.salesPersonId)] ):
            allSalesEarningsSumByEmployee[int(sale.salesPersonId)] += int(sale.salePrice)

    # Sum for Managers
    for employee in allEmployees:
        if ( isEmployeeManager[int(employee.id)] ):
            for empl in allEmployees:
                if ( empl.managerId == employee.id ):
                    allSalesEarningsSumByEmployee[int(employee.id)] += allSalesEarningsSumByEmployee[int(empl.id)]
                


    # Set the title of the dialog window
    dialog.title("Salaries of employees")

    treeview_frame = tk.Frame(dialog)
    treeview_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    treeview_scrollbar = tk.Scrollbar(treeview_frame)
    treeview_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    treeview = ttk.Treeview(treeview_frame, columns=("empName", "baseSalary", "salesMade", "finalSalary"),
                                    yscrollcommand=treeview_scrollbar.set)
    treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    treeview_scrollbar.config(command=treeview.yview)

    treeview.heading("#0", text="N0", anchor="w")
    treeview.column("#0", anchor="w")
    treeview.heading("empName", text="Employee Name", anchor="w")
    treeview.column("empName", anchor="w")
    treeview.heading("baseSalary", text="Base Salary", anchor="w")
    treeview.column("baseSalary", anchor="w")
    treeview.heading("salesMade", text="Made Sales", anchor="w")
    treeview.column("salesMade", anchor="w")
    treeview.heading("finalSalary", text="Final Salary", anchor="w")
    treeview.column("finalSalary", anchor="w")

    saleIndex = 0
    for employee in allEmployees:
        saleIndex += 1
        
        finalSalary = int(employee.basicSalary)

        if ( not ("manager" in str(employee.jobTitle).lower() ) ):
            finalSalary += allSalesEarningsSumByEmployee[int(employee.id)] * 0.065
        else:
            finalSalary += allSalesEarningsSumByEmployee[int(employee.id)] * 0.035
        
        treeview.insert("", tk.END, text=saleIndex, values=(employee.name, employee.basicSalary, allSalesEarningsSumByEmployee[int(employee.id)], finalSalary) )
        
    # Wait for the dialog window to be closed
    dialog.wait_window()
    
# Finding Dialogs
def find_employee_dialog():
    # Create a new dialog window
    dialog = Toplevel()

    # Set the title of the dialog window
    dialog.title("Search for an employee")

    # Set the minimum size of the dialog window
    dialog.minsize(width=300, height=100)

    # Set the padding of the dialog window
    dialog['padx'] = 20
    dialog['pady'] = 20

    id_label = ttk.Label(dialog, text="Employee ID:")
    id_label.grid(column=0, row=1, sticky="W", pady=1)
    id_entry = ttk.Entry(dialog)
    id_entry.grid(column=1, row=1, pady=1)

    # Create a frame to hold the buttons
    button_frame = ttk.Frame(dialog)
    button_frame.grid(column=0, row=5, columnspan=2, pady=10)

    # Create the Add and Cancel buttons
    add_button = ttk.Button(button_frame, text="FIND", command=lambda:findEmployeeById(id_entry.get()))
    add_button.pack(side=LEFT, padx=5)

    # cancel_button = ttk.Button(button_frame, text="Cancel", command=dialog.destroy)
    # cancel_button.pack(side=LEFT, padx=5)

    # Set the focus to the name entry box
    id_entry.focus()

    # Wait for the dialog window to be closed
    dialog.wait_window()

def find_car_dialog():
    # Create a new dialog window
    dialog = Toplevel()

    # Set the title of the dialog window
    dialog.title("Search for a car")

    # Set the minimum size of the dialog window
    dialog.minsize(width=300, height=100)

    # Set the padding of the dialog window
    dialog['padx'] = 20
    dialog['pady'] = 20

    id_label = ttk.Label(dialog, text="Car ID:")
    id_label.grid(column=0, row=1, sticky="W", pady=1)
    id_entry = ttk.Entry(dialog)
    id_entry.grid(column=1, row=1, pady=1)

    # Create a frame to hold the buttons
    button_frame = ttk.Frame(dialog)
    button_frame.grid(column=0, row=5, columnspan=2, pady=10)

    # Create the Add and Cancel buttons
    add_button = ttk.Button(button_frame, text="FIND", command=lambda:findCarById(id_entry.get()))
    add_button.pack(side=LEFT, padx=5)

    # cancel_button = ttk.Button(button_frame, text="Cancel", command=dialog.destroy)
    # cancel_button.pack(side=LEFT, padx=5)

    # Set the focus to the name entry box
    id_entry.focus()

    # Wait for the dialog window to be closed
    dialog.wait_window()

def find_sales_dialog():
    # Create a new dialog window
    dialog = Toplevel()

    # Set the title of the dialog window
    dialog.title("Search for employees sales")

    # Set the minimum size of the dialog window
    dialog.minsize(width=300, height=100)

    # Set the padding of the dialog window
    dialog['padx'] = 20
    dialog['pady'] = 20

    id_label = ttk.Label(dialog, text="Employee ID:")
    id_label.grid(column=0, row=1, sticky="W", pady=1)
    id_entry = ttk.Entry(dialog)
    id_entry.grid(column=1, row=1, pady=1)

    # Create a frame to hold the buttons
    button_frame = ttk.Frame(dialog)
    button_frame.grid(column=0, row=5, columnspan=2, pady=10)

    # Create the Add and Cancel buttons
    add_button = ttk.Button(button_frame, text="FIND", command=lambda:findSalesByEmployeeId(id_entry.get()))
    add_button.pack(side=LEFT, padx=5)

    # cancel_button = ttk.Button(button_frame, text="Cancel", command=dialog.destroy)
    # cancel_button.pack(side=LEFT, padx=5)

    # Set the focus to the name entry box
    id_entry.focus()

    # Wait for the dialog window to be closed
    dialog.wait_window()

def getCarById(carId):
    allCars = []
    if os.path.exists("Cars.pickle"):
        with open("Cars.pickle", "rb") as handle:
            allCars = pickle.load(handle)

    for car in allCars:
        if ( car.id == carId ):
            return car
        
    else:
        return None


#Searching 
def findEmployeeById(employeeID):
    allEmployees = []
    if os.path.exists("Employees.pickle"):
        with open("Employees.pickle", "rb") as handle:
            allEmployees = pickle.load(handle)
    
    if ( len(allEmployees) <= 0 ):
        show_message_dialog("There are not any added employes. \nPlease add at least one employee")
    else:
        employeeIndex = 0
        for employee in allEmployees:
            if ( str(employee.id) == str(employeeID) ):
                employee_editing_dialog(
                    employeeIndex,
                    employee
                )
                return
            employeeIndex += 1
        show_message_dialog("There are not any employees with this id!")

def findCarById(carId):
    allCars = []
    if os.path.exists("Cars.pickle"):
        with open("Cars.pickle", "rb") as handle:
            allCars = pickle.load(handle)
    
    if ( len(allCars) <= 0 ):
        show_message_dialog("There are not any added cars. \nPlease add at least one car!")
    else:
        carIndex = 0
        for car in allCars:
            if ( str(car.id) == str(carId) ):
                car_editing_dialog(
                    carIndex,
                    car
                )
                return
            carIndex += 1
        show_message_dialog("There are not any employees with this id!")

def findSalesByEmployeeId(salesPersonId):
    allSales = []
    if os.path.exists("Sales.pickle"):
        with open("Sales.pickle", "rb") as handle:
            allSales = pickle.load(handle)
    
    if ( len(allSales) <= 0 ):
        show_message_dialog("There are not any added sales. \nPlease add at least one sale!")
    else:
        salesOfEmployee = []
        for sale in allSales:
            if ( str(sale.salesPersonId) == str(salesPersonId) ):
                salesOfEmployee.append(sale)

        if ( len(salesOfEmployee) > 0 ):
            sale_viewing_dialog(salesOfEmployee)
            return
        
        show_message_dialog("There are not any sales with this employee id!")

# Updating
def updateEmployeeDataByIndex(dialog, employeeIndex, employeeNewData:Employee):
    allEmployees = []
    if os.path.exists("Employees.pickle"):
        with open("Employees.pickle", "rb") as handle:
            allEmployees = pickle.load(handle)
    
    allEmployees[employeeIndex] = employeeNewData

    with open("Employees.pickle", 'wb') as f:
        pickle.dump(allEmployees, f)

    show_message_dialog("Successfully updated employee data!")
    dialog.destroy()

def updateCarDataByIndex(dialog, carIndex, carNewData:Car):
    allCars = []
    
    if os.path.exists("Cars.pickle"):
        with open("Cars.pickle", "rb") as handle:
            allCars = pickle.load(handle)

    allCars[carIndex] = carNewData

    with open("Cars.pickle", 'wb') as f:
        pickle.dump(allCars, f)

    show_message_dialog("Successfully updated car data!")
    dialog.destroy()

# Deleting
def deleteEmployeeDataByIndex(dialog, employeeIndex):
    allEmployees = []
    if os.path.exists("Employees.pickle"):
        with open("Employees.pickle", "rb") as handle:
            allEmployees = pickle.load(handle)
    
    newEmployeesData = []
    empIndex = 0
    for employee in allEmployees:
        if ( empIndex != employeeIndex ):
            newEmployeesData.append(employee)
        empIndex += 1

    with open("Employees.pickle", 'wb') as f:
        pickle.dump(newEmployeesData, f)

    show_message_dialog("Successfully deleted employee data!")
    dialog.destroy()

def deleteCarDataByIndex(dialog, carIndex):
    allCars = []
    
    if os.path.exists("Cars.pickle"):
        with open("Cars.pickle", "rb") as handle:
            allCars = pickle.load(handle)

    newCars = []
    cIndex = 0
    for car in allCars:
        if ( cIndex != carIndex ):
            newCars.append(car)
        cIndex += 1

    with open("Cars.pickle", 'wb') as f:
        pickle.dump(newCars, f)

    show_message_dialog("Successfully deleted car data!")
    dialog.destroy()

# Adding Dialogs
def add_employee_dialog():
    # Create a new dialog window
    dialog = Toplevel()

    # Set the title of the dialog window
    dialog.title("Add New Employee")

    # Set the minimum size of the dialog window
    dialog.minsize(width=300, height=300)

    # Set the padding of the dialog window
    dialog['padx'] = 20
    dialog['pady'] = 20

    # Create the labels and entry boxes for each field
    name_label = ttk.Label(dialog, text="Name:")
    name_label.grid(column=0, row=0, sticky="W", pady=1)
    name_entry = ttk.Entry(dialog)
    name_entry.grid(column=1, row=0, pady=1)

    id_label = ttk.Label(dialog, text="ID:")
    id_label.grid(column=0, row=1, sticky="W", pady=1)
    id_entry = ttk.Entry(dialog)
    id_entry.grid(column=1, row=1, pady=1)

    department_label = ttk.Label(dialog, text="Department:")
    department_label.grid(column=0, row=2, sticky="W", pady=1)
    department_entry = ttk.Entry(dialog)
    department_entry.grid(column=1, row=2, pady=1)

    job_title_label = ttk.Label(dialog, text="Job Title:")
    job_title_label.grid(column=0, row=3, sticky="W", pady=1)
    job_title_entry = ttk.Entry(dialog)
    job_title_entry.grid(column=1, row=3, pady=1)

    basic_salary_label = ttk.Label(dialog, text="Basic Salary:")
    basic_salary_label.grid(column=0, row=4, sticky="W", pady=1)
    basic_salary_entry = ttk.Entry(dialog)
    basic_salary_entry.grid(column=1, row=4, pady=1)

    dob_label = ttk.Label(dialog, text="Date of Birth (DD.MM.YYYY):")
    dob_label.grid(column=0, row=5, sticky="W", pady=1)
    dob_entry = ttk.Entry(dialog)
    dob_entry.grid(column=1, row=5, pady=1)

    passport_details_label = ttk.Label(dialog, text="Passport Details:")
    passport_details_label.grid(column=0, row=6, sticky="W", pady=1)
    passport_details_entry = ttk.Entry(dialog)
    passport_details_entry.grid(column=1, row=6, pady=1)

    manager_id_label = ttk.Label(dialog, text="Manager ID (for sales person only):")
    manager_id_label.grid(column=0, row=7, sticky="W", pady=1)
    manager_id_entry = ttk.Entry(dialog)
    manager_id_entry.grid(column=1, row=7, pady=1)

    # Create a frame to hold the buttons
    button_frame = ttk.Frame(dialog)
    button_frame.grid(column=0, row=8, columnspan=2, pady=10)

    # Create the Add and Cancel buttons
    add_button = ttk.Button(button_frame, text="Add", command=lambda:addNewEmployee(dialog, name_entry.get(), id_entry.get(), department_entry.get(), job_title_entry.get(), basic_salary_entry.get(), dob_entry.get(), passport_details_entry.get(), manager_id_entry.get()))
    add_button.pack(side=LEFT, padx=5)

    cancel_button = ttk.Button(button_frame, text="Cancel", command=dialog.destroy)
    cancel_button.pack(side=LEFT, padx=5)

    # Set the focus to the name entry box
    name_entry.focus()

    # Wait for the dialog window to be closed
    dialog.wait_window()

def add_car_dialog():
    # Create a new dialog window
    dialog = Toplevel()

    # Set the title of the dialog window
    dialog.title("Add New Car")

    # Set the minimum size of the dialog window
    dialog.minsize(width=300, height=300)

    # Set the padding of the dialog window
    dialog['padx'] = 20
    dialog['pady'] = 20

    # Create the labels and entry boxes for each field
    name_label = ttk.Label(dialog, text="Name:")
    name_label.grid(column=0, row=0, sticky="W", pady=1)
    name_entry = ttk.Entry(dialog)
    name_entry.grid(column=1, row=0, pady=1)

    id_label = ttk.Label(dialog, text="ID:")
    id_label.grid(column=0, row=1, sticky="W", pady=1)
    id_entry = ttk.Entry(dialog)
    id_entry.grid(column=1, row=1, pady=1)

    price_label = ttk.Label(dialog, text="Price:")
    price_label.grid(column=0, row=2, sticky="W", pady=1)
    price_entry = ttk.Entry(dialog)
    price_entry.grid(column=1, row=2, pady=1)

    type_label = ttk.Label(dialog, text="Type:")
    type_label.grid(column=0, row=3, sticky="W", pady=1)
    type_entry = ttk.Entry(dialog)
    type_entry.grid(column=1, row=3, pady=1)

    fuelCapacity_label = ttk.Label(dialog, text="Fuel Capacity:")
    fuelCapacity_label.grid(column=0, row=4, sticky="W", pady=1)
    fuelCapacity_entry = ttk.Entry(dialog)
    fuelCapacity_entry.grid(column=1, row=4, pady=1)

    maxSpeed_label = ttk.Label(dialog, text="Max Speed:")
    maxSpeed_label.grid(column=0, row=5, sticky="W", pady=1)
    maxSpeed_entry = ttk.Entry(dialog)
    maxSpeed_entry.grid(column=1, row=5, pady=1)

    color_label = ttk.Label(dialog, text="Color:")
    color_label.grid(column=0, row=6, sticky="W", pady=1)
    color_entry = ttk.Entry(dialog)
    color_entry.grid(column=1, row=6, pady=1)

    # Create a frame to hold the buttons
    button_frame = ttk.Frame(dialog)
    button_frame.grid(column=0, row=7, columnspan=2, pady=10)

    # Create the Add and Cancel buttons
    add_button = ttk.Button(button_frame, text="Add", command=lambda:addNewCar(dialog, name_entry.get(), id_entry.get(), price_entry.get(), type_entry.get(), fuelCapacity_entry.get(), maxSpeed_entry.get(), color_entry.get()))
    add_button.pack(side=LEFT, padx=5)

    cancel_button = ttk.Button(button_frame, text="Cancel", command=dialog.destroy)
    cancel_button.pack(side=LEFT, padx=5)

    # Set the focus to the name entry box
    name_entry.focus()

    # Wait for the dialog window to be closed
    dialog.wait_window()

def add_sale_dialog():
    # Create a new dialog window
    dialog = Toplevel()

    # Set the title of the dialog window
    dialog.title("Add New Sale")

    # Set the minimum size of the dialog window
    dialog.minsize(width=300, height=200)

    # Set the padding of the dialog window
    dialog['padx'] = 20
    dialog['pady'] = 20

    id_label = ttk.Label(dialog, text="ID:")
    id_label.grid(column=0, row=1, sticky="W", pady=1)
    id_entry = ttk.Entry(dialog)
    id_entry.grid(column=1, row=1, pady=1)

    salesPersonId_label = ttk.Label(dialog, text="Sales Person ID:")
    salesPersonId_label.grid(column=0, row=2, sticky="W", pady=1)
    salesPersonId_entry = ttk.Entry(dialog)
    salesPersonId_entry.grid(column=1, row=2, pady=1)

    carId_label = ttk.Label(dialog, text="Car ID:")
    carId_label.grid(column=0, row=3, sticky="W", pady=1)
    carId_entry = ttk.Entry(dialog)
    carId_entry.grid(column=1, row=3, pady=1)

    salePrice_label = ttk.Label(dialog, text="Sale Price:")
    salePrice_label.grid(column=0, row=4, sticky="W", pady=1)
    salePrice_entry = ttk.Entry(dialog)
    salePrice_entry.grid(column=1, row=4, pady=1)

    # Create a frame to hold the buttons
    button_frame = ttk.Frame(dialog)
    button_frame.grid(column=0, row=5, columnspan=2, pady=10)

    # Create the Add and Cancel buttons
    add_button = ttk.Button(button_frame, text="Add", command=lambda:addNewSale(dialog, id_entry.get(), salesPersonId_entry.get(), carId_entry.get(), salePrice_entry.get()))
    add_button.pack(side=LEFT, padx=5)

    cancel_button = ttk.Button(button_frame, text="Cancel", command=dialog.destroy)
    cancel_button.pack(side=LEFT, padx=5)

    # Set the focus to the name entry box
    id_entry.focus()

    # Wait for the dialog window to be closed
    dialog.wait_window()


# Verifying and Adding
def addNewEmployee( dialog, name, id, department, jobTitle, basicSalary, dob, passportDetails, managerId):
    print("Adding new employee, Name: " + str(name))
    if ( len(str(name)) == 0 or len(str(id)) == 0 or len(str(department)) == 0 or len(str(jobTitle)) == 0 or len(str(basicSalary)) == 0 or len(str(dob)) == 0 or len(str(passportDetails)) == 0 or (  ("manager" in str(jobTitle).lower()) and len(str(managerId)) == 0) ):
        show_message_dialog("You left some entries empty.\nFill them all!")
    else:
        newEmployee = Employee(name, id, department, jobTitle, basicSalary, dob, passportDetails, managerId)
        SaveEmployee(newEmployee)
        show_message_dialog("New Employee added successfully!")
        dialog.destroy()

def addNewCar( dialog, name, id, price, type, fuelCapacity, maxSpeed, color):
    print("Adding new Car, Name: " + str(name))
    if ( len(str(name)) == 0 or len(str(id)) == 0 or len(str(price)) == 0 or len(str(type)) == 0 or len(str(fuelCapacity)) == 0 or len(str(maxSpeed)) == 0 or len(str(color)) == 0 ):
        show_message_dialog("You left some entries empty.\nFill them all!")
    else:
        newCar = Car(name, id, price, type, fuelCapacity, maxSpeed, color)
        SaveCar(newCar)
        show_message_dialog("New Car added successfully!")
        dialog.destroy()

def addNewSale ( dialog, id, salesPersonId, carId, salePrice):
    print("Adding new Sale, salesPersonId: " + str(salesPersonId))
    if ( len(str(id)) == 0 or len(str(salesPersonId)) == 0 or len(str(carId)) == 0 or len(str(salePrice)) == 0 ):
        show_message_dialog("You left some entries empty.\nFill them all!")
    else:
        newSale = Sale(id, salesPersonId, carId, salePrice)
        SaveSale(newSale)
        show_message_dialog("New Sale added successfully!")
        dialog.destroy()


# Saving
def SaveEmployee(employee: Employee):
    allEmployees = []
    
    if os.path.exists("Employees.pickle"):
        with open("Employees.pickle", "rb") as handle:
            allEmployees = pickle.load(handle)

    allEmployees.append(employee)

    # save database using Pickle
    with open("Employees.pickle", 'wb') as f:
        pickle.dump(allEmployees, f)

def SaveCar(car: Car):
    allCars = []
    
    if os.path.exists("Cars.pickle"):
        with open("Cars.pickle", "rb") as handle:
            allCars = pickle.load(handle)

    allCars.append(car)

    # save database using Pickle
    with open("Cars.pickle", 'wb') as f:
        pickle.dump(allCars, f)

def SaveSale(sale: Sale):
    allSales = []
    
    if os.path.exists("Sales.pickle"):
        with open("Sales.pickle", "rb") as handle:
            allSales = pickle.load(handle)

    allSales.append(sale)

    # save database using Pickle
    with open("Sales.pickle", 'wb') as f:
        pickle.dump(allSales, f)


def show_message_dialog(message):
    messagebox.showinfo("Message", message)

# Define the function to be called when a button is clicked
def button_clicked(btn_num):
    print(f"Button {btn_num} was clicked!")

# Create the 6 buttons in a 2x3 grid with icons and titles
icon1 = PhotoImage(file="Icons/add_user.png").subsample(3)
button1 = tk.Button(root, image=icon1, text="New Employee", compound="left", width=300, padx=20, pady=20, command=add_employee_dialog)
button1.grid(row=1, column=0, padx=2, pady=2)

icon2 = PhotoImage(file="Icons/add_car.png").subsample(3)
button2 = tk.Button(root, image=icon2, text="New Car", compound="left", width=300, padx=20, pady=20, command=add_car_dialog)
button2.grid(row=1, column=1, padx=2, pady=2)

icon3 = PhotoImage(file="Icons/add_sale.png").subsample(3)
button3 = tk.Button(root, image=icon3, text="New Sale", compound="left", width=300, padx=20, pady=20, command=add_sale_dialog)
button3.grid(row=1, column=2, padx=2, pady=2)

icon4 = PhotoImage(file="Icons/edit_employee.png").subsample(3)
button4 = tk.Button(root, image=icon4, text="Edit Employee", compound="left", width=300, padx=20, pady=20, command=find_employee_dialog)
button4.grid(row=2, column=0, padx=2, pady=2)

icon5 = PhotoImage(file="Icons/edit_car.png").subsample(3)
button5 = tk.Button(root, image=icon5, text="Edit Car", compound="left", width=300, padx=20, pady=20, command=find_car_dialog)
button5.grid(row=2, column=1, padx=2, pady=2)

icon6 = PhotoImage(file="Icons/edit_cart.png").subsample(3)
button6 = tk.Button(root, image=icon6, text="View Employee Sales", compound="left", width=300, padx=20, pady=20, command=find_sales_dialog)
button6.grid(row=2, column=2, padx=2, pady=2)

icon7 = PhotoImage(file="Icons/moneyBag.png").subsample(3)
button7 = tk.Button(root, image=icon7, text="Calculate Salaries", compound="left", width=300, padx=20, pady=20, command=salaries_viewing_dialog)
button7.grid(row=3, column=1, padx=2, pady=2)

# Add a label for the footer text
footer_label = tk.Label(root, text="\u00A9 2023 SOHIBJON AVGONOV", font=("Arial", 14), fg="gray")
footer_label.grid(row=4, columnspan=4, pady=10)

# Start the main event loop
root.mainloop()
