#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    # Insert tickets into hash table
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # Check the hash table for the initial destination and get the first destination
    ticket = hash_table_retrieve(hashtable, 'NONE')

    # Insert into the route list and grab the next ticket
    for i in range(length):
        route[i] = ticket
        ticket = hash_table_retrieve(hashtable, ticket)

    return route
