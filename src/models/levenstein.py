
from unicodedata import normalize
from src.database.readDB import dataCity

def levenstein(str1, str2):
    """
    Calculate the Levenshtein distance between two strings.
    @param str1: the first string
    @param str2: the second string
    @return: the Levenshtein distance between the two strings
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
    """
    Search for a given code in the dataCity dataset using the Levenshtein distance algorithm. 
    @param code: the string to search
    @return: the row in the dataset that match the code, or a empty rowf no match is found
    """
    data = dataCity() 
    line = data[data['IATA']=='zzzz'] # line is a empty row 
    lowest = 99
    row = 0 # row index
    for i in range(len(data)):
        distance = levenstein(norm(data.loc[i,'IATA']),norm(code))
        distance2 = levenstein(norm(data.loc[i,'cities']),norm(code))
        if(distance == 0|distance2==0):
          return data.iloc[[i]]  
        if(distance < lowest):
            lowest = distance
            row = i
        if(distance2 < lowest):
            lowest = distance2
            row = i
    if(lowest>10):
        return line
    return data.iloc[[row]]

def norm(code):
    """
    Normalize the given code by applying the NFKD normalization form and converting it to lowercase.
    @param code: the code to be normalized
    @return: the normalized code
    """
    
    return normalize('NFKD',code).lower()