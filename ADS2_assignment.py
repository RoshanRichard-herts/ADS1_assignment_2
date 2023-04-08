#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 11:16:08 2023

@author: roshanrichard
"""

import pandas as pd
import matplotlib.pyplot as plt


def get_data(filename):
    """ 
    This function takes filename as argument and
    reads the data file into dataframes 
    
    """
    data=pd.read_csv(filename)
    datatranspose=data.set_index('Country Name').transpose()
    return data,datatranspose

def filter_line_plot(data):
    """
    Defining function for filtering years and 
    countries for plotting line plot and returning the data
    
    """
    data=data[['Country Name','Indicator Name', '1991', '1997', '2004', '2010', '2016', '2019']]
    data=data[(data["Country Name"]=="Denmark")|
              (data["Country Name"]=="China")|
              (data["Country Name"]=="Germany")|
              (data["Country Name"]=="India")|
              (data["Country Name"]=="Spain")|
              (data["Country Name"]=="United States")]
    return data

def line_plot(data, label1, label2):
    plt.figure(figsize=(26, 10))
    data_index=data.set_index('Country Name')
    transpose_data=data_index.transpose()
    transpose_data=transpose_data.drop(index=['Indicator Name'])
    for i in range(len(country_list)):
        plt.plot(transpose_data.index, transpose_data[country_list[i]], label=country_list[i])
    plt.title(label2, size=18)
    plt.xlabel("Years", size=12)
    plt.ylabel(label1, size=12)
    plt.xticks(rotation=90)
    plt.legend(fontsize=10)
    plt.savefig("lineplot.png")#Saving Lineplot
    plt.show()

country_list =['Denmark', 'China', 'Germany', 'India', 'Spain', 'United States']

co2_data, cos_data_Transpose = get_data('co2_emm.csv')
co2_data = filter_line_plot(co2_data)
line_plot(co2_data, "CO2 Emission ", "CO2 Emission")



