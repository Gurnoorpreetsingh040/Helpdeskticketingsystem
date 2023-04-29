# Helpdesk Ticket Management System
This is a simple ticket management system written in Python using Object Oriented Programming (OOP) concepts. The system can create, display, and update tickets.

Installation
To run the code, Python 3.6 or higher is required. There are no additional dependencies.

Usage
The code can be run from the command line or from a Python IDE.
python ticket_system.py


When the code is executed, the user will be presented with a menu of options:

Create a ticket
Reopen a ticket
Respond to a ticket
Display all of the Tickets
Display details of a Ticket
Display Ticket Statistics
Exit
The user can choose an option by entering the corresponding number. The system will then prompt the user for any required information and perform the requested action.

Creating a ticket
To create a ticket, the user must enter the staff ID, creator's name, email address, and problem description. The ticket number will be assigned automatically, and the ticket status will be set to "Open".

Reopening a ticket
To reopen a ticket, the user must enter the ticket number. If the ticket exists and is closed, it will be reopened and the status will be set to "Open".

Responding to a ticket
To respond to a ticket, the user must enter the ticket number. If the ticket exists and is open, the user can enter a response. The ticket will then be closed and the status will be set to "Closed". If the ticket description is "password change", the response and status will be set automatically.

Displaying all tickets
To display all tickets, the user can choose option 4. The system will display the ticket number, creator's name, staff ID, email address, problem description, response, and status for all tickets.

Displaying details of a ticket
To display the details of a ticket, the user can choose option 5 and enter the ticket number. The system will display the ticket number, creator's name, staff ID, email address, problem description, response, and status for the specified ticket.

Displaying ticket statistics
To display ticket statistics, the user can choose option 6. The system will display the total number of tickets created, the total number of tickets resolved, and the total number of tickets that still need to be solved.

Exiting the program
To exit the program, the user can choose option 7.
