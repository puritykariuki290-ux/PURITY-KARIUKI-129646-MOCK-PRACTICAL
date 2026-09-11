# Input employee details
employee_id = input("Enter Employee ID: ")
employee_name = input("Enter Employee Name: ")

basic_salary = float(input("Enter Basic Salary: "))
transport_allowance = float(input("Enter Transport Allowance: "))
housing_allowance = float(input("Enter Housing Allowance: "))

deductions = float(input("Enter Other Deductions: "))
tax_rate = float(input("Enter Tax Rate (%):10 "))

# Calculate total allowance
total_allowance = transport_allowance + housing_allowance

# Calculate gross salary
gross_salary = basic_salary + total_allowance

# Calculate tax
tax = gross_salary * (tax_rate / 100)

# Calculate total deductions
total_deductions = tax + deductions

# Calculate net salary
net_salary = gross_salary - total_deductions

# Display employee payroll
print("Employee ID:", employee_id)
print("Employee Name:", employee_name)

print("Basic Salary:       ", basic_salary)
print("Transport Allowance:", transport_allowance)
print("Housing Allowance:  ", housing_allowance)
print("Total Allowance:    ", total_allowance)
print("Gross Salary:       ", gross_salary)
print("Tax:                ", tax)
print("Other Deductions:   ", deductions)
print("Total Deductions:   ", total_deductions)
print("Net Salary:         ", net_salary)