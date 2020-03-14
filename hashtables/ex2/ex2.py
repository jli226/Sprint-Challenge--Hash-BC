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
    #insert tickets into hash table
    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)
    
    #check the hash table for the initial destination and get the first destination
    route[0] = hash_table_retrieve(hashtable, "NONE")

    current = 1
    
    #insert into the route list and grab the next ticket
    while route[-2] == None:
        route[current] = hash_table_retrieve(hashtable, route[current-1])
        current += 1

    route.pop()



    return route   
