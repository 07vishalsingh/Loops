'''
You are given a list of employee records. Each record is represented as a dictionary containing the employee's name and their monthly work hours. Write a Python function to calculate and return the average monthly work hours of all the employees in the list.
'''

def average_work_hours(employees):
    total_hours = 0
    num_employees = len(employees)
    
    # Iterate through each employee record in the list
    for employee in employees:
        # Add the monthly work hours of the employee to the total
        total_hours += employee['hours']
    
    # Calculate the average work hours
    if num_employees > 0:
        average_hours = total_hours / num_employees
        return average_hours
    else:
        return 0  # Return 0 if the list is empty

# Example usage
employee_records = [
    {'name': 'Alice', 'hours': 160},
    {'name': 'Bob', 'hours': 175},
    {'name': 'Charlie', 'hours': 145},
    {'name': 'David', 'hours': 180}
]

print("Average Monthly Work Hours:", average_work_hours(employee_records))  # Output: 165.0
