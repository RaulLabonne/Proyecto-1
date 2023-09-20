
from unicodedata import normalize
from src.database.readDB import dataCity

def levenstein(str1, str2):
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
    data = dataCity()
    line = data[data['IATA']=='zzzz']
    lowest = 99
    row = 0
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
    return normalize('NFKD',code).lower()