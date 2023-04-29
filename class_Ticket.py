class Ticket:
    def __init__(self, staff_id, creator_name, email, description):
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.email = email
        self.description = description
        self.ticket_number = None
        self.status = None
        self.response = "Not Yet Provided"

    def __repr__(self):
        return f"Ticket {self.ticket_number} - {self.status}"

    def close(self, response):
        self.response = response
        self.status = "Closed"

    def reopen(self):
        self.status = "Open"

    @classmethod
    def create(cls, staff_id, creator_name, email, description, starting_number=2000):
        ticket = cls(staff_id, creator_name, email, description)
        ticket.ticket_number = starting_number
        ticket.status = "Open"
        return ticket

    @staticmethod
    def get_ticket_by_number(ticket_number, tickets):
        for ticket in tickets:
            if ticket.ticket_number == ticket_number:
                return ticket
        return None

    @staticmethod
    def filter_by_status(status, tickets):
        return [ticket for ticket in tickets if ticket.status == status]

    @staticmethod
    def count_by_status(status, tickets):
        return len(Ticket.filter_by_status(status, tickets))

    @staticmethod
    def show_ticket_statistics(tickets):
        total_tickets = len(tickets)
        resolved_tickets = Ticket.count_by_status("Closed", tickets)
        open_tickets = total_tickets - resolved_tickets
        print("\nTotal Tickets Created: ", total_tickets)
        print("Total Tickets Resolved: ", resolved_tickets)
        print("Total Tickets To Solve: ", open_tickets)

    @staticmethod
    def display_all_tickets(tickets):
        for ticket in tickets:
            print("\nTicket Number: ", ticket.ticket_number)
            print("Ticket Creator: ", ticket.creator_name)
            print("Staff ID: ", ticket.staff_id)
            print("Email Address: ", ticket.email)
            print("Description: ", ticket.description)
            print("Response: ", ticket.response)
            print("Ticket Status: ", ticket.status)

    @staticmethod
    def display_ticket_details(ticket):
        print("\nTicket Number: ", ticket.ticket_number)
        print("Ticket Creator: ", ticket.creator_name)
        print("Staff ID: ", ticket.staff_id)
        print("Email Address: ", ticket.email)
        print("Description: ", ticket.description)
        print("Response: ", ticket.response)
        print("Ticket Status: ", ticket.status)

    @staticmethod
    def display_ticket_stats(tickets):
        Ticket.show_ticket_statistics(tickets)

    @staticmethod
    def end_program():
        print("\nThank you for using !!!")

def main():
    tickets = []
    starting_number = 2000

    while True:
        print("\n---XXXXXXXXXXXXXX---Welcome to the Ticket Management System---XXXXXXXXXXXXXX---\n")
        print("Please choose an option from the list given below:-")
        print("1. Create a ticket")
        print("2. Reopen a ticket")
        print("3. Respond to a ticket")
        print("4. Display all of the Tickets")
        print("5. Display details of a Ticket")
        print("6. Display Ticket Statistics")
        print("7. Exit")
        input_data = int(input("Enter your choice (1-7): "))

        if input_data == 1:
            staff_id = input("Please Enter the Staff_ID: ")
            creator_name = input("Please Enter the Creator's Name: ")
            email = input("Please Enter Email address: ")
            description = input("Please Enter the Problem Description: ")
            starting_number=len(tickets) + 2000

            ticket = Ticket.create(staff_id, creator_name, email, description, starting_number)
            tickets.append(ticket)
            print(f"\nTicket created successfully with Ticket Number {ticket.ticket_number}.")
	
        elif input_data == 2:
            ticket_number = int(input("Enter Ticket Number to Reopen: "))
            ticket = Ticket.get_ticket_by_number(ticket_number, tickets)


            if ticket:
                ticket.reopen()
                print(f"\nTicket {ticket_number} has been reopened.")
            else:
                print(f"\nTicket {ticket_number} does not exist.")

        elif input_data == 3:
            ticket_number = int(input("Enter Ticket Number to Respond: "))
            ticket = Ticket.get_ticket_by_number(ticket_number, tickets)

            if ticket and ticket.status == "Open":
                if ticket.description.lower() == "password change":
                # If the ticket description is "password change", set the response and status accordingly
                    ticket.response = "New Password : "+ ticket.staff_id[:2]+ticket.creator_name[:3]
                    ticket.status = "Closed"
                    print("The ticket is resolved automatically because of new password request")
                
                else:
                    response = input("Enter Response: ")
                    ticket.close(response)
                    print(f"\nTicket {ticket_number} has been resolved.")

            elif ticket and ticket.status == "Closed":
                print(f"\nTicket {ticket_number} is already resolved.")
            else:
                print(f"\nTicket {ticket_number} does not exist.")

        elif input_data == 4:
            if tickets:
                Ticket.display_all_tickets(tickets)
            else:
                print("\nNo tickets found.")

        elif input_data == 5:
            ticket_number = int(input("Enter Ticket Number to display details: "))
            ticket = Ticket.get_ticket_by_number(ticket_number, tickets)

            if ticket:
                Ticket.display_ticket_details(ticket)
            else:
                print(f"\nTicket {ticket_number} does not exist.")

        elif input_data == 6:
            if tickets:
                Ticket.display_ticket_stats(tickets)
            else:
                print("\nNo tickets found.")

        elif input_data == 7:
            Ticket.end_program()
            break

        else:
            print("Invalid Input. Please choose a valid option (1-7).")
    
if __name__ == "__main__":
    main()
