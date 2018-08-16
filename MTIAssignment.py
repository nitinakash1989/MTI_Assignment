# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 02:21:40 2018

@author: nitin
"""
# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import shapely.geometry as SG
#Task-1

def load_data(fileName, header=False):
    """load_data function to load file into system
    having filtered data containing only visible wavelength spectrum which is 390nm - 700nm.
    Parameters
    ----------
    fileName : str
        The first parameter: Name of the file
    header : bool
        The second parameter: Whether header should be returned or not.

    Returns
    if header == True:
        return tuple having dataframe containing wavelength, transmission
                            and header of file as metadata
    else:
        return only dataframe containing wavelength, transmission
    """
    with open(fileName, 'r') as myfile:
        metadata=''.join([next(myfile) for x in range(3)])

    data = pd.read_csv(fileName, skiprows=4, sep='\t', header = None,
                   names = ["Wavelength","Transmission"])

    data = data[(data['Wavelength']>=390) & (data['Wavelength']<=700)]
    if(header==False):
        return(data)
    else:
        return(data, metadata)

#Task 2
def getCenterAndDistance(fileName):
    """
    Function to calculates the spectral position of the notch centre and the width of the 
    notch at 50% transmission.
    
     ----------
    data : dataframe
        The data frane with only visible length frequency.

    Returns
    if header == True:
        return tuple having distance and notch centre
    """
    data= load_data(fileName, header=False)
    x = list(data.iloc[:, 0].values)
    y = list(data.iloc[:, 1].values)
    center = data[data["Transmission"]==min(data["Transmission"])].iloc[0].at["Wavelength"]
    line = SG.LineString(list(zip(x,y)))
    intersectLine = data["Transmission"].median()/2
    yline = SG.LineString([(min(x), intersectLine), (max(x), intersectLine)])
    coords = np.array(line.intersection(yline))
    intersectPoint = pd.Series(coords[:,0])
    lowPoint = intersectPoint[intersectPoint<center].max()
    highPoint = intersectPoint[intersectPoint>center].min()
    distance = highPoint - lowPoint
    print(distance)
    return distance
