import unittest
import ticketsviewer

'''
Ticket 1 is a sample ticket provided by Zendesk and we will be using that to test our fetchTicket(id) method.
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

if __name__ == '__main__':
    unittest.main()
    
