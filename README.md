# TicketsViewer

Welcome to the Zendesk Ticket Viewer Python Application.

This application uses Command Line Interface (CLI) to communicate with user and collect the user's choices. It is a lightweight python application that requests users' ticket data from Zendesk's API. It displays tickets paginated with a maximum of 25 tickets per page. It also has the option to view a single ticket in great detail. API calls are slightly costly (performance wise) and it's preferred to minimize them; however, the maximum number of tickets returned from our API requests is 100, which greatly reduces overhead and results in better performance. The average response time for an API request is <800ms. The application could be improved by caching data from previous API calls to minimize API requests. Additionally, if there was a way to use cursor pagination and offset pagination in conjunction, or if there was a hybrid of the two, the efficiency of the application could be significantly increased.

To run the application all that one need to do is to install python and a python library called requests by using the command "$pip3 install requests" After installing python and the requests library, all we need to do to run the application is run the command "$python3 ticketsviewer.py"

The application consists of 7 major methods. The init(), menu(), fetchTicket(id), fetchQuarter(page)[jump branch], fetchTickets(url, page), displayTicket(ticket), and displayTickets(tickets). 

init() - initializes the API parameters and makes an API request to figure out the how many number of tickets are registered for that user.

menu() - it's an integral part of the application that administers the main menu by displaying choices for the user and adhering to user's choices by facilitating the demands.

fetchTicket(id) - receives a ticket id argument, and makes an API request for details about that ticket which will be returned as a python dict to where the function was invoked.

fetchQuarter(page) [jump branch] - receives a page number argument and makes an API request for the 100 ticket chunk and slices it up to return the quarter which the page number designates as a python dict.

fetchTickets(url, page) - receives a url and page argument to make an API request to fetch 25 tickets belonging to that page and returns the tickets as a python dict. 

displayTicket(ticket) - accepts a python dict single ticket argument and displays the details of that ticket.

displayTickets(tickets) - accepts a python dict argument of tickets and displays them in a list. 
