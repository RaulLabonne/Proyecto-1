from src.database.readDB import dataCity
from src.models.levenstein import searchLev

def request_iatacode(cityData):
    """Given city data, extract the latitude and longitude coordinates of the city.


     Parameters
    ----------
    cityData : DataFrame
        the dataFrame containing latitude and longitude information
        
    Returns
    -------
    list[int]
        the latitude and longitude coordinates of the city
    """
    coord=[cityData.loc[0,'latitude'],cityData.loc[0,'longitude']]
    return coord

def cityRow(code):
    """Given a city code, retrieve the corresponding city data from a search function.


     Parameters
    ----------
    code : str 
        the city code
        
    Returns
    -------
    DataFrame
        the city data as a pandas DataFrame. If no data is found, return a TypeError.

    """
    if(len(code)>3):
        cityData =searchLev(code)
    else:
        data = dataCity()
        cityData = data[data["IATA"]==code.upper()]
    if(cityData.empty):
        raise TypeError
    cityData.reset_index(inplace=True, drop=False)
    return cityData