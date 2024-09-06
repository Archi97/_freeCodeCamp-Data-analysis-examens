import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    extended_years = pd.concat([df['Year'], pd.Series(range(2014,2051))], ignore_index=True)
    plt.plot(extended_years, res.intercept + res.slope*extended_years, 'r', label='upto 2050 line')

    #from 2000 
    #Second line
    df_2000 = df.loc[df['Year']>1999]
    df_2000.shape
    reg_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    extended_years = pd.Series(range(2000,2051))
    y = reg_2000.intercept + reg_2000.slope*extended_years

    plt.plot(extended_years, y, 'y', label='2000+ line')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()