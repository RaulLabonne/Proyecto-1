
from unicodedata import normalize
from src.database.readDB import dataCity

def levenstein(str1, str2):
    """Calculate the Levenshtein distance between two strings.
    
    Parameters
    ----------
    str1 : str
        the first string
    str2 : str
        the second string
        
    Returns
    -------
    int
        the Levenshtein distance between the two strings
    """
    
    d=dict()
    for i in range(len(str1)+1):
        d[i]=dict()
        d[i][0]=i
    for i in range(len(str2)+1):
        d[0][i] = i
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1]+(not str1[i-1] == str2[j-1]))
    return d[len(str1)][len(str2)]

def searchLev(code):
    
    """Search for a given code in the dataCity dataset using the Levenshtein distance algorithm. 

    
     Parameters
    ----------
    code : str 
        the string to search
        
    Returns
    -------
    DataFrame
        the row in the dataset that match the code, or a empty row if no match is found
    """
    
    data = dataCity() 
    line = data[data['IATA']=='zzzz'] # line is a empty row 
    lowest = 99
    row = 0 # row index
    for i in range(len(data)):
        distance = levenstein(norm(data.loc[i,'cities']),norm(code))
        if(distance == 0):
          return data.iloc[[i]]  
        if(distance < lowest):
            lowest = distance
            row = i
    if(lowest>=len(code)/2):
        return line
    
    return data.iloc[[row]]

def norm(code):
    """Normalize the given code by applying the NFKD normalization form and converting it to lowercase.


     Parameters
    ----------
    code : str
        the code to be normalized
        
    Returns
    -------
    str
        the normalized code
    """
    return normalize('NFKD',code).lower()