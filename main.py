#   main.py
#   python 2.7

#   Handy Employee Management System (HEMS)
#   Basic CLI Employee Management System that interfaces with
#       a database.

#   Chris Bugg
#   Created: 5/10/17

# Imports
import os
import re
import sys
from handler import Handler
from employee import Employee


# Main Class
class HEMS:

    # Handles Database interaction
    database_handler = Handler()

    # Constructor
    def __init__(self):

        # Main loop
        while True:

            # Clear Screen
            os.system('cls' if os.name == 'nt' else 'clear')

            print
            print "Handy IT Employee Management System [HEMS]"
            print
            print "(S)earch"
            print "(A)dd"
            print "(U)pdate"
            print "(R)emove"
            print
            print "(E)xit"
            print

            choice = raw_input('Selection: ')

            # Input Sanitation
            good_choices = {"s", "S", "a", "A", "u", "U", "r", "R", "e", "E"}

            while choice not in good_choices:

                print "Input Error!"

                choice = raw_input("Selection: ")

            # Search
            if (choice == "s") or (choice == "S"):

                self.search_screen()

            # Add
            elif (choice == "a") or (choice == "A"):

                self.add_screen()

            # Update
            elif (choice == "u") or (choice == "U"):

                self.update_screen()

            # Remove
            elif (choice == "r") or (choice == "R"):

                self.remove_screen()

            # Exit on any other selection
            else:

                sys.exit(0)

    # Prints search screen
    def search_screen(self):

        while True:

            # Clear Screen
            os.system('cls' if os.name == 'nt' else 'clear')

            print
            print "HEMS -> Search"
            print
            print "(E)mployee Identification Number (EIN)"
            print "(S)SN"
            print "(F)irst Name"
            print "(L)ast Name"
            print "(P)ayrate"
            print "(A)ll Employees"
            print
            print "(B)ack"
            print

            choice = raw_input('Selection: ')

            # Input Sanitation
            good_choices = {"e", "E", "s", "S", "f", "F", "l", "L", "p", "P", "a", "A", "b", "B"}

            while choice not in good_choices:

                print "Input Error!"

                choice = raw_input("Selection: ")

            # Clear Screen
            os.system('cls' if os.name == 'nt' else 'clear')

            # Employee Identification Number (EIN)
            if (choice == "e") or (choice == "E"):

                input = raw_input("Employee Identification Number (EIN): ")

                # Input Sanitation
                input = self.sanitize_digits(input)

                # Perform Database search
                employees = self.search('ein', input)

                self.search_results(employees)

            # SSN
            elif (choice == "s") or (choice == "S"):

                input = raw_input("SSN (555-55-5555): ")

                # Input Sanitation
                input = self.sanitize_ssn(input)

                # Perform Database search
                employees = self.search('ssn', input)

                self.search_results(employees)

            # First Name
            elif (choice == "f") or (choice == "F"):

                input = raw_input("First Name: ")

                # Input Sanitation
                input = self.sanitize_letters(input)

                # Perform Database search
                employees = self.search('first', input)

                self.search_results(employees)

            # Last Name
            elif (choice == "l") or (choice == "L"):

                input = raw_input("Last name: ")

                # Input Sanitation
                input = self.sanitize_letters(input)

                # Perform Database search
                employees = self.search('last', input)

                self.search_results(employees)

            # Payrate
            elif (choice == "p") or (choice == "P"):

                input = raw_input("Payrate: ")

                # Input Sanitation
                input = self.sanitize_digits(input)

                # Perform Database search
                employees = self.search('payrate', input)

                self.search_results(employees)

            # All Employees
            elif (choice == "a") or (choice == "A"):

                # Perform Database search
                employees = self.search_all()

                self.search_results(employees)

            # Exit on any other selection
            else:

                # Break out of while and go back to main screen
                break

    # Searches Database based on given fields
    def search(self, column, query):

        return self.database_handler.search(column, query)

    # Searches Database based on given fields
    def search_all(self):

        return self.database_handler.search_all()

    # Sanitizes inputs to digits (really integers)
    def sanitize_digits(self, input):

        # If the input isn't all digits
        while not input.isdigit():

            # Ask the user to try again
            print "Input Error! Not an Integer!"
            input = raw_input("Input: ")

        return input

    # Sanitizes input to letters (a-z,A-Z)
    def sanitize_letters(self, input):

        # If the string isn't all alphabetic characters
        while not input.isalpha():

            # Ask the user to try again
            print "Input Error! Not all Letters!"
            input = raw_input("Input: ")

        return input

    # Sanitizes inputs to SSNs (555-55-5555)
    def sanitize_ssn(self, input):

        # Run till they put it in right
        while True:

            # Regex magic that matches an SSN
            ssn_matcher = re.compile('\d{3}-\d{2}-\d{4}')

            # A list of all valid SSN's in the input
            matches = ssn_matcher.findall(input)

            # If the list is non-empty
            if matches:

                # Retun the first valid SSN
                return matches[0]

            # Ask the user to try again
            print "Input Error! Not a Valid SSN (555-55-5555)!"
            input = raw_input("Input: ")

    # Prints add screen
    def add_screen(self):

        # Clear Screen
        os.system('cls' if os.name == 'nt' else 'clear')

        print
        print "HEMS -> Add"
        print

        # Create new Employee object
        employee = Employee()

        # Get info from user + sanitize
        employee.ein = self.sanitize_digits(raw_input("Employee Identification Number (EIN): "))

        # Check if EIN is already in the system
        employee_list = self.search('ein', employee.ein)

        # While there are employees whom match that EIN
        while employee_list:

            # Try again
            print "Input Error! Employee already exists!"
            employee.ein = self.sanitize_digits(raw_input("Employee Identification Number (EIN): "))

            # And re-check
            employee_list = self.search('ein', employee.ein)

        employee.ssn = self.sanitize_ssn(raw_input("SSN: "))
        employee.first_name = self.sanitize_letters(raw_input("First Name: "))
        employee.last_name = self.sanitize_letters(raw_input("Last Name: "))
        employee.payrate = self.sanitize_digits(raw_input("Payrate: "))

        # Add employee to database
        self.add(employee)

        print
        print "Employee Added"
        print

        raw_input("Back (Enter): ")

    # Adds employee to database
    def add(self, employee):

        self.database_handler.add(employee)

    # Prints remove screen
    def remove_screen(self):

        # Clear Screen
        os.system('cls' if os.name == 'nt' else 'clear')

        print
        print "HEMS -> Remove"
        print

        # Create new Employee object
        employee = Employee()

        # Get info from user + sanitize
        employee.ein = self.sanitize_digits(raw_input("Employee Identification Number (EIN): "))

        print "ARE YOU SURE YOU WISH TO REMOVE THIS USER?"
        print "YES - Remove User"
        print "NO - Do Nothing"
        print

        choice = raw_input('Selection (YES[Remove]/NO[Do Nothing]): ')

        # Input Sanitation
        good_choices = {"YES", "NO", "N", "no", "n", "0"}

        while choice not in good_choices:
            print "Input Error!"

            choice = raw_input("Selection (YES[Remove]/NO[Do Nothing]): ")

        # Remove
        if choice == "YES":

            # Remove employee from database
            self.remove(employee.ein)

            print
            print "Employee Removed"
            print

        else:

            print

        raw_input("Back (Enter): ")

    # Removes employee from database
    def remove(self, ein):

        self.database_handler.remove(ein)

    # Prints update screen
    def update_screen(self):

        # Clear Screen
        os.system('cls' if os.name == 'nt' else 'clear')

        print
        print "HEMS -> Update"
        print

        # Create new Employee object
        employee = Employee()

        # Get info from user + sanitize
        employee.ein = self.sanitize_digits(raw_input("Employee Identification Number (EIN): "))

        # Check if EIN is already in the system
        employee_list = self.search('ein', employee.ein)

        # While there are not employees whom match that EIN
        while not employee_list:
            # Try again
            print "Input Error! No Employees match that EIN!"
            employee.ein = self.sanitize_digits(raw_input("Employee Identification Number (EIN): "))

            # And re-check
            employee_list = self.search('ein', employee.ein)

        employee.ssn = self.sanitize_ssn(raw_input("SSN: "))
        employee.first_name = self.sanitize_letters(raw_input("First Name: "))
        employee.last_name = self.sanitize_letters(raw_input("Last Name: "))
        employee.payrate = self.sanitize_digits(raw_input("Payrate: "))

        # Add employee to database
        self.update(employee)

        print
        print "Employee Updated"
        print

        raw_input("Back (Enter): ")

    # Updates employee in database
    def update(self, employee):

        self.database_handler.update(employee)

    # Prints employee information to the screen
    def employee_print(self, employee):

        print "EIN:\t " + str(employee.ein)
        print "SSN:\t " + str(employee.ssn)
        print "First:\t " + str(employee.first_name)
        print "Last:\t " + str(employee.last_name)
        print "Payrate: " + str(employee.payrate)

    # Prints the results of a search
    def search_results(self, employees):

        print "Results: "

        # For each employee found, print details
        for employee in employees:
            self.employee_print(employee)
            print

        # If there were none found
        if not employees:
            print "No Results Found."
            print

        raw_input("Back (Enter): ")

HEMS()
