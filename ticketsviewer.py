import requests
import math
import time
# Set the request parameters
count = 0
user = 'kaleabunited@gmail.com' +'/token'
pwd = 'lwpUCXiRmglWwug5EBLrpcM41SCza0awetv5AJmb'
print("\nWelcome to our advanced Ticket Viewer")

def init():
    # Set the request parameters
    counturl = 'https://zccsenior.zendesk.com/api/v2/tickets/count.json'
    response = requests.get(counturl, auth=(user, pwd))
    global count
    
    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting....')
        exit()
    
    # Do the HTTP get request
    count = response.json()['count']

def fetchTickets(url, page):
    print("\nPage " + str(page) + " of " + str(math.ceil(count['value']/25)) + "\n")

    # Do the HTTP get request
    start = time.time()
    response = requests.get(url, auth=(user, pwd))
    end = time.time()
    print("\nAPI response time %.2f" % ((end-start)*1000) + " microseconds.\n")
    
    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting....')
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    return data

def fetchTicket(id):
    # Set the request parameters
    url = 'https://zccsenior.zendesk.com/api/v2/tickets/' + str(id) + '.json'
    
    # Do the HTTP get request
    start = time.time()
    response = requests.get(url, auth=(user, pwd))
    end = time.time()
    print("\nAPI response time %.2f" % ((end-start)*1000) + " microseconds.\n")    
    
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting....')
        exit()
    
    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    return data

def displayTicket(ticket):
    print("\nTicket: " + str(ticket['id']) + "\n\nSubject: " + str(ticket['subject']))
    print("\nDescription: " + str(ticket['description']) + "\n\nCreated on: " + ticket['created_at'])


def menu():
    #display menu and facilitate user based on choices
    while(1):
        print("\nPlease enter choice from options below\n1. Display all tickets.")
        choice = int(input("2. Display a ticket \n3. Quit\n\n"))
        if(choice == 1):
            print("\nThis user has " + str(count['value']) + " tickets currently registered. Refreshed at: " + str(count['refreshed_at']))
            url = 'https://zccsenior.zendesk.com/api/v2/tickets.json?page[size]=25'
            currentPage = 1
            currentPageDetails = fetchTickets(url, currentPage)
            displayTickets(currentPageDetails['tickets'])
            lastPage = math.ceil(count['value']/25)
            print("\nPage " + str(currentPage) + " of " + str(math.ceil(count['value']/25)))
            
            while(1):
                print("\nPlease choose from the following options")
            #first page choices
                if(currentPage == 1):
                    choice = int(input("1. Next Page.\n2. Display a ticket.\n3. Quit\n\n"))
                    if (choice == 1):
                        currentPage += 1
                        url = currentPageDetails['links']['next']
                        currentPageDetails = fetchTickets(url, currentPage)
                        displayTickets(currentPageDetails['tickets'])
                        print("\nPage " + str(currentPage) + " of " + str(math.ceil(count['value']/25)))
                    elif(choice == 2):
                        id = int(input("Please enter ticket ID of ticket: "))
                        if(id > count['value'] and id < 1):
                            print("Invalid id number. Returning to main menu.")
                        else: displayTicket(fetchTicket(id)['ticket'])
                    elif(choice == 3):
                        print("\nExiting...\n\n")
                        exit()                    
                    else: print("Invalid choice.")
            #last page choices            
                elif(currentPage == lastPage):
                    choice = int(input("1. Previous Page.\n2. Display a ticket.\n3. Quit\n\n"))
                    if (choice == 1):
                        currentPage -= 1
                        url = currentPageDetails['links']['prev']
                        currentPageDetails = fetchTickets(url, currentPage)
                        displayTickets(currentPageDetails['tickets'])
                        print("\nPage " + str(currentPage) + " of " + str(math.ceil(count['value']/25)))
        
                    elif(choice == 2):
                        id = int(input("Please enter ticket ID of ticket: "))
                        if(id > count['value'] and id < 1):
                            print("Invalid id number. Returning to main menu.")
                        else: displayTicket(fetchTicket(id)['ticket'])
                    
                    elif(choice == 3):
                        print("\nExiting...\n\n")
                        exit()
                    else: print("Invalid choice.") 
            #mid page choices
                else: 
                    choice = int(input("1. Previous page.\n2. Next Page.\n3. Display a ticket.\n4. Quit\n\n"))
                    if (choice == 1):
                        currentPage -= 1
                        url = currentPageDetails['links']['prev']
                        currentPageDetails = fetchTickets(url, currentPage)
                        displayTickets(currentPageDetails['tickets'])
                    elif (choice == 2):
                        currentPage += 1
                        url = currentPageDetails['links']['next']
                        currentPageDetails = fetchTickets(url, currentPage)
                        displayTickets(currentPageDetails['tickets'])
                    elif (choice == 3):
                        id = int(input("Please enter ticket ID of ticket: "))
                        if(id > count['value'] and id < 1):
                            print("Invalid id number. Returning to main menu.")
                        else: displayTicket(fetchTicket(id)['ticket'])
                    elif(choice == 4):
                        print("\nExiting...\n\n")
                        exit()
                    else: print("Invalid choice.")

        elif(choice == 2):
            id = int(input("Please enter ticket ID of ticket: "))
            if(id > count['value'] and id < 1):
                print("Invalid id number. Returning to main menu.")
            else: displayTicket(fetchTicket(id)['ticket'])
        elif(choice == 3):
            print("\nExiting...\n\n")
            exit()
        else: print("\nChoice not available!", end=" ")

def displayTickets(tickets):
    if(len(tickets) <= 25):
        for ticket in tickets:
            print("Ticket ID: " + str(ticket['id']) + " subject '" + ticket['subject'] + "' created on " + ticket['created_at'])

init()
menu()
