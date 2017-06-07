Welcome to HEMS, or the Handy Employee Management System!

This program is designed to be a basic employee management system
capable of storing basic information about employees in an easily
searchable database with a clean command-line interface for quick
employee administration. Users can Search for, Add, Update, and
Remove employees from the system. The system stores such useful
information as employees Employee Identification Number (an Integer),
Social Security Number, First and Last names, and Payrate (also an
Integer).

It can be run from a python2 interpreter with the simple command:
>$ python main.py

The database is a single-file (database.db) sqlite3 database, generated
on demand if non-existent.

The program itself is composed of a series of menus navigated by
single-letter short-cuts. It is resistant to many forms of SQL-injection
attacks as it uses prepared statements, though no program is impenetrable.

I hope you enjoy my program as much as I enjoyed writing it!

Thanks,
Chris Bugg