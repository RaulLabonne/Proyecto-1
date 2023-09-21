import pandas as pd
from src.models import search_weather as sw
from src.database.readDB import dataDB


def read(ticket):
    """
    Read the ticket information from the database based on the ticket number provided.
    @param ticket: the ticket number
    @return: the weather information for the origin and destination cities of the ticket
    """
    data = dataDB()
    dataTicket = data[data['num_ticket'] == ticket]
    dataTicket.reset_index(inplace=True, drop=False)
    if(dataTicket.empty):
        return TypeError
    city1 =dataTicket.loc[0,'origin']
    city2 = dataTicket.loc[0,'destination']
    weather=[sw.search(city1),sw.search(city2)]
    return weather


    