#   handler.py
#   python 2.7

#   Handles a sqlite3 (Python) single-file Database.

#   Chris Bugg
#   Created: 5/10/17

# Imports
from employee import Employee
import sqlite3
import os


class Handler:

    # Boolean check if table exists
    database_exists = os.path.exists('database.db')

    # Create Connection object (database)
    conn = sqlite3.connect('database.db')

    # Create Cursor object to navigate database
    curs = conn.cursor()

    # If there is no table
    if not database_exists:
        # Create table
        curs.execute('''CREATE TABLE employees
                             (ein integer, ssn text, first text, last text, payrate integer)''')

    # Save (commit) the changes
    conn.commit()

    # Constructor
    def __init__(self):

        # Save (commit) the changes
        self.conn.commit()

    # Function to search the database
    def search(self, column, query):

        # Execute the search
        # Using different placeholders for columns and data due to sqlite3 qwerks
        self.curs.execute("SELECT * FROM employees WHERE {}=?".format(column), (query,))

        # Get the list of all resulting rows
        results_list = self.curs.fetchall()

        # A list to hold our matched employees
        employees = []

        # While there are employees in the row list
        while results_list:

            # Remove the row from the list
            employee = results_list.pop()

            # Build an employee from the row
            emp = Employee()
            emp.ein = employee[0]
            emp.ssn = employee[1]
            emp.first_name = employee[2]
            emp.last_name = employee[3]
            emp.payrate = employee[4]

            # Add employee to list
            employees.append(emp)

        # Reverse ordering of employees since it's backwards
        employees.reverse()

        # Returns list of matching employees
        return employees

    # Function to search the whole database
    def search_all(self):

        # Execute the search
        self.curs.execute("SELECT * FROM employees")

        # Get the list of all resulting rows
        results_list = self.curs.fetchall()

        # A list to hold our matched employees
        employees = []

        # While there are employees in the row list
        while results_list:
            # Remove the row from the list
            employee = results_list.pop()

            # Build an employee from the row
            emp = Employee()
            emp.ein = employee[0]
            emp.ssn = employee[1]
            emp.first_name = employee[2]
            emp.last_name = employee[3]
            emp.payrate = employee[4]

            # Add employee to list
            employees.append(emp)

        # Reverse ordering of employees since it's backwards
        employees.reverse()

        # Returns list of matching employees
        return employees

    # Function to add employee to database
    def add(self, employee):

        # Extract info from employee object
        ein = int(employee.ein)
        ssn = employee.ssn
        first_name = employee.first_name
        last_name = employee.last_name
        payrate = int(employee.payrate)

        # Build a tuple from the extracted information
        employee_tuple = (ein, ssn, first_name, last_name, payrate)

        # Insert a row of data
        self.curs.execute("INSERT INTO employees VALUES (?,?,?,?,?)", employee_tuple)

        # Save (commit) the changes
        self.conn.commit()

    # Function to update employee in the database
    def update(self, employee):

        # Extract info from employee object
        ein = int(employee.ein)
        ssn = employee.ssn
        first_name = employee.first_name
        last_name = employee.last_name
        payrate = int(employee.payrate)

        # Build a tuple from the extracted information
        employee_tuple = (ssn, first_name, last_name, payrate, ein)

        # Update a row of data
        self.curs.execute("UPDATE employees SET ssn=?, first=?, last=?, payrate=? WHERE ein=?",
                          employee_tuple)

        # Save (commit) the changes
        self.conn.commit()

    # Function to remove employee from database
    def remove(self, ein):

        # Build a tuple from the ein
        ein_tuple = (int(ein),)

        # Update a row of data
        self.curs.execute("DELETE FROM employees WHERE ein = ?", ein_tuple)

        # Save (commit) the changes
        self.conn.commit()

    # Closes connection when done
    def close(self):

        # Save (commit) the changes
        self.conn.commit()

        # Close connection
        self.conn.close()
