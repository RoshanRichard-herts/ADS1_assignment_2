#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 11:16:08 2023

@author: roshanrichard
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



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

def filter_bar_data(df):
    """
    
    Parameters
    ----------
    df : dataframe with years as columns
    Returns
    -------
    df : filtered dataframe to plot the bar chart of selected countries
    """
    df = df[['Country Name','Indicator Name','2010','2011','2012','2013','2014']]
    df = df[(df["Country Name"]=="Belgium")|
            (df["Country Name"]=="Italy")|
            (df["Country Name"]=="Denmark")|
            (df["Country Name"]=="Spain")|
            (df["Country Name"]=="Finland")|
            (df["Country Name"]=="Jamaica")]
    return df

def line_plot(data, label1, label2):
    plt.figure(figsize=(15, 10))
    data_index=data.set_index('Country Name')
    transpose_data=data_index.transpose()
    transpose_data=transpose_data.drop(index=['Indicator Name'])
    for i in range(len(country_list1)):
        plt.plot(transpose_data.index, transpose_data[country_list1[i]], label=country_list1[i])
    plt.title(label2, size=18)
    plt.xlabel("Years", size=12)
    plt.ylabel(label1, size=12)
    plt.xticks(rotation=90)
    plt.legend(fontsize=10)
    if temp1:
        plt.savefig("lineplot_1.png")#Saving Lineplot
    else:
        plt.savefig("lineplot_2.png")
    plt.show()
    
def barplot(df,lab1,lab2):
    """
    
    Parameters
    ----------
    df : dataframe to plot bar chart of the chosen countries
    lab1 : to label y-axis
    lab2 : to get the title of the bar graph
    Returns
    -------
    None.
    """
    plt.figure(figsize=(25,18))
    dx= plt.subplot(1,1,1)
    x = np.arange(6)
    width= 0.2
    
    bar1= dx.bar(x, df["2010"],width,label=2010)
    bar2= dx.bar(x+width, df["2011"],width,label=2011)
    bar3= dx.bar(x+width*2, df["2012"],width,label=2012)
    
    dx.set_xlabel("Countries", fontsize=40)
    dx.set_ylabel(lab1, fontsize=40)
    dx.set_title(lab2, fontsize=40)
    dx.set_xticks(x,country_list2,fontsize=30,rotation=90)
    dx.legend(fontsize=30)
    dx.bar_label(bar1,padding=2,rotation=90,fontsize=18)
    dx.bar_label(bar2,padding=2,rotation=90,fontsize=18)
    dx.bar_label(bar3,padding=2,rotation=90,fontsize=18)
    if temp2:
        plt.savefig("barplot_1.png")
    else:
        plt.savefig("barplot_2.png")
    plt.show()

temp1 = 0
temp2 = 0
country_list1 =['Denmark', 'China', 'Germany', 'India', 'Spain', 'United States']
country_list2 = ['Belgium', 'Italy', 'Denmark', 'Spain', 'Finland', 'Jamaica']

co2_data, cos_data_Transpose = get_data('co2_emm.csv')
energy_cons, energy_cons_Transpose = get_data('energy_con.csv')

co2_data = filter_line_plot(co2_data)
energy_cons = filter_line_plot(energy_cons)

lit_rate, lit_rate_transpose = get_data('lit_rate.csv')
lit_rate = filter_bar_data(lit_rate)

unemp_rate, unemp_rate_transpose = get_data('unemp_rate.csv')
unemp_rate = filter_bar_data(unemp_rate)

line_plot(co2_data, "CO2 Emission ", "CO2 Emission")
temp1 += 1
line_plot(energy_cons, "Energy Consuption", "Energy Consuption")

barplot(lit_rate, 'Literacy Rate', 'Literacy Rate')
temp2 += 1
barplot(unemp_rate, 'Unemployment percentage', 'Unemployment percentage')

