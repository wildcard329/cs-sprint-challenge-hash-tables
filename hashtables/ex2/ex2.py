#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    itinerary = {}
    route = []
    for ticket in tickets:
        # print(ticket.source, ticket.destination)
        itinerary[ticket.source] = ticket.destination
    print(itinerary)

    start = itinerary.get('NONE')
    route.append(start)
    next_location = itinerary.get(start)
    while next_location != 'NONE':
        route.append(next_location)
        next_location = itinerary.get(next_location)
    route.append(next_location)

    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

reconstruct_trip(tickets, 3)