import pandas as pd
import os

def dataDB():
    current_dir = os.path.dirname(os.path.realpath(__file__)) 
    filename=os.path.join(current_dir,"dataset2.csv")
    data = pd.read_csv(filename,header=0)
    return data

def dataCity():
    current_dir = os.path.dirname(os.path.realpath(__file__)) 
    filename=os.path.join(current_dir,"cities3.csv")
    data = pd.read_csv(filename,header=0)
    return data