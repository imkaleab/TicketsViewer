import unittest
import ticketsviewer

'''
Ticket 1 is a sample ticket provided by Zendesk and we will be using that to test our fetchTicket(id) method.

The init() method makes a request to the API to check how many tickets are in the account and exits gracefully if the API returns anything other than a status code of 200

The menu() method facilitates the choices for the user.

    * UI is pretty clear and has rigorous test from within to ensure an error-free environment.
    * The currentPage variable (which keeps track of which page is being viewed) doesn't get updated unless a vaible input is inserted by the user which significantly reduces the margin for error.
    * If a user requests a specific page or ticket, extra tests are conducted to ensure that the ticket ID and page number is a valid number.

displayTicket(ticket) - displays the ticket parameter in great detail. Returns a null if ticket is null.
displayTickets(tickets) - displays the first 25 of the tickets or the total number of tickets, whichever is lesser. Returns null if tickets is null.

'''

class TestTicketsviewer (unittest.TestCase):
    
    def test_fetchTicket(self):
        ticket = ticketsviewer.fetchTicket(1)
        self.assertEqual(ticket['ticket']['subject'], 'Sample ticket: Meet the ticket')
        self.assertEqual(ticket['ticket']['id'], 1)
    
    def test_fetchPage(self):
        tickets = ticketsviewer.fetchPage(1)
        self.assertEqual(len(tickets), 25)  
        self.assertEqual(tickets[0] ['id'], 1)
        tickets = ticketsviewer.fetchPage(4)
        self.assertEqual(tickets[0]['id'], 76)
    
    def test_displayTicket(self):
        self.assertEqual(ticketsviewer.displayTicket(None), -1)
        self.assertEqual(ticketsviewer.displayTicket(ticketsviewer.fetchTicket(1)['ticket']), None)

    
    def test_displayTickets(self):
        tickets = ticketsviewer.fetchPage(1)
        self.assertEqual(ticketsviewer.displayTickets(tickets), None)

if __name__ == '__main__':
    unittest.main()
    
