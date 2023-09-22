import pandas as pd
import os

def dataDB():
    """
    Load the dataset from a CSV file named "dataset2.csv" located in the same directory as the script.
    @return: the loaded dataset as a pandas DataFrame.
    """
   
    current_dir = os.path.dirname(os.path.realpath(__file__)) 
    filename=os.path.join(current_dir,"dataset2.csv")
    data = pd.read_csv(filename,header=0)
    return data

def dataCity():
    """
    Load city data from a CSV file named "cities3.csv" located in the same directory as the script.
    @return: a pandas DataFrame containing the city data.
    """
    
    current_dir = os.path.dirname(os.path.realpath(__file__)) 
    filename=os.path.join(current_dir,"cities3.csv")
    data = pd.read_csv(filename,header=0)
    return data