#Name: Kaleab Alemu
#Zendesk Coding Challenge
#Date: 07/31/2021

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
    global urls
    
    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting....')
        exit()
    
    # Do the HTTP get request
    count = response.json()['count']

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

def fetchQuarter(page):
    print("\nPage " + str(page) + " of " + str(math.ceil(count['value']/25)))
    
    pageNum = ((page%4)-1) * 25
    url = 'https://zccsenior.zendesk.com/api/v2/tickets.json?page=' + str(math.ceil(page/4))

    # Do the HTTP get request
    start = time.time()
    response = requests.get(url, auth=(user, pwd))
    end = time.time()
    print("\nAPI response time %.2f" % ((end-start)*1000) + " microseconds.\n") 
    
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting....')
        exit()
    
    data = response.json()['tickets'][pageNum:count['value'] if count['value'] <= pageNum+25 else pageNum+25] 
    return data

def displayTicket(ticket):
    print("\nTicket: " + str(ticket['id']) + "\n\nSubject: " + str(ticket['subject']))
    print("\nDescription: " + str(ticket['description']) + "\n\nCreated on: " + ticket['created_at'])

def displayTickets(tickets):
    if(len(tickets) <= 25):
        for ticket in tickets:
            print("Ticket ID: " + str(ticket['id']) + " subject '" + ticket['subject'] + "' created on " + ticket['created_at'])

def menu():
    #display menu and facilitate user based on choices
    while(1):
        print("\nPlease enter choice from options below\n1. Display all tickets.")
        choice = int(input("2. Display a ticket \n3. Quit\n\n"))
        if(choice == 1):
            print("\nThis user has " + str(count['value']) + " tickets currently registered. Refreshed at: " + str(count['refreshed_at']))
            currentPage = 1
            displayTickets(fetchQuarter(1))
            lastPage = math.ceil(count['value']/25)
            print("\nPage " + str(currentPage) + " of " + str(math.ceil(count['value']/25)))
            
            while(1):
                print("\nPlease choose from the following options")
            #first page choices
                if(currentPage == 1):
                    choice = int(input("1. Next Page.\n2. Jump to Page.\n3. Display a ticket.\n4. Quit\n\n"))
                    if (choice == 1):
                        currentPage += 1
                        displayTickets(fetchQuarter(currentPage))
                        print("\nPage " + str(currentPage) + " of " + str(math.ceil(count['value']/25)))
                    
                    elif(choice == 2):
                        pageNum = int(input("Enter page number: "))
                        if(pageNum >= 1 and pageNum <= lastPage):
                            currentPage = pageNum
                            displayTickets(fetchQuarter(currentPage))
                            print("\nPage " + str(currentPage) + " of " + str(lastPage))
                        
                        else: print("\nInvalid Page Number.")
        
                    elif(choice == 3):
                        id = int(input("Please enter ticket ID of ticket: "))
                        if(id > count['value'] and id < 1):
                            print("Invalid id number.")
                        else: displayTicket(fetchTicket(id)['ticket'])
                    elif(choice == 4):
                        print("\nExiting. . . Goodbye:)")
                        exit()
                    else: print("Invalid choice.")
            #last page choices            
                elif(currentPage == lastPage):
                    choice = int(input("1. Previous Page.\n2. Jump to Page.\n3. Display a ticket.\n4. Quit\n\n"))
                    if (choice == 1):
                        currentPage -= 1
                        displayTickets(fetchQuarter(currentPage))
                        print("\nPage " + str(currentPage) + " of " + str(math.ceil(count['value']/25)))
                    
                    elif(choice == 2):
                        pageNum = int(input("Enter page number: "))
                        if(pageNum >= 1 and pageNum <= lastPage):
                            currentPage = pageNum
                            displayTickets(fetchQuarter(currentPage))
                            print("\nPage " + str(currentPage) + " of " + str(lastPage))
                        
                        else: print("\nInvalid Page Number.")
        
                    elif(choice == 3):
                        id = int(input("Please enter ticket ID of ticket: "))
                        if(id > count['value'] and id < 1):
                            print("Invalid id number.")
                        else: displayTicket(fetchTicket(id)['ticket'])
                    elif(choice == 4):
                        print("\nExiting. . . Goodbye:)")
                        exit()
                    else: print("Invalid choice.") 
            #mid page choices
                else: 
                    choice = int(input("1. Previous page.\n2. Next Page.\n3. Jump to Page.\n4. Display a ticket.\n5. Quit\n\n"))
                    if (choice == 1):
                        currentPage -= 1
                        displayTickets(fetchQuarter(currentPage))
                        print("\nPage " + str(currentPage) + " of " + str(lastPage))
                    elif (choice == 2):
                        currentPage += 1
                        displayTickets(fetchQuarter(currentPage))
                        print("\nPage " + str(currentPage) + " of " + str(lastPage))
                    elif (choice == 3):
                        pageNum = int(input("Enter page number: "))
                        if(pageNum >= 1 and pageNum <= lastPage):
                            currentPage = pageNum
                            displayTickets(fetchQuarter(currentPage))
                            print("\nPage " + str(currentPage) + " of " + str(lastPage))
                        
                        else: print("\nInvalid Page Number.")
                    
                    elif (choice == 4):
                        id = int(input("Please enter ticket ID of ticket: "))
                        if(id > count['value'] and id < 1):
                            print("Invalid id number.")
                        else: displayTicket(fetchTicket(id)['ticket'])
                    elif(choice == 5):
                        print("\nExiting. . . Goodbye:)")
                        exit()
                    else: print("Invalid choice.")

        elif(choice == 2):
            id = int(input("Please enter ticket ID of ticket: "))
            if(id > count['value'] and id < 1):
                print("Invalid id number. Returning to main menu.")
            else: displayTicket(fetchTicket(id)['ticket'])
        elif(choice == 3):
            print("\nExiting. . . Goodbye:)")
            exit()
        else: print("\nChoice not available!", end=" ")

init()
menu()
