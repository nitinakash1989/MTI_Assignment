# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 02:21:40 2018

@author: nitin
"""
# Importing the libraries
import pandas as pd

#Task-1

def load_data(fileName, header=False):
    """load_data function to load file into system
    having filtered data containing only visible wavelength spectrum which is 390nm - 700nm.
    Parameters
    ----------
    fileName : str
        The first parameter.
    header : bool
        The second parameter.

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