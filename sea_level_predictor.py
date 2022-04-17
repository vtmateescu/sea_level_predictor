import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy import stats
import os

def draw_plot():
    # Read data from file
    cwd = os.getcwd()
    csv_dir = "{}/epa-sea-level.csv".format(cwd)
    data_input = pd.read_csv(csv_dir)
    year_array = data_input["Year"]
    CASL_array= data_input["CSIRO Adjusted Sea Level"]

    # Create scatter plot
    plt.scatter(year_array, CASL_array, label="Original data")

    # Create first line of best fit
    slope, intercept, r, p, se = linregress(year_array, CASL_array)
    regression_xaxis_array = pd.Series(range(year_array[0], 2051))
    #regression_yaxis_array = [CASL_array[0]+(regression_xaxis_array[i]-regression_xaxis_array[0])*slope for i in range(len(regression_xaxis_array))]
    regression_yaxis_array = [intercept+regression_xaxis_array[i]*slope for i in range(len(regression_xaxis_array))]

    plt.plot(regression_xaxis_array, regression_yaxis_array, label='Linear Regression all data', color='r')

    # Create second line of best fit
    reduced_input_array = data_input[data_input['Year']>=2000]
    reduced_year_array = reduced_input_array["Year"]
    reduced_CASL_array= reduced_input_array["CSIRO Adjusted Sea Level"]
    slope_r, intercept_r, r_r, p_r, se_r = linregress(reduced_year_array, reduced_CASL_array)
    regression_reduced_xaxis_array = pd.Series(range(reduced_year_array.iloc[0], 2051))
    #regression_reduced_yaxis_array = [reduced_CASL_array.iloc[0] + (regression_reduced_xaxis_array.iloc[i]-reduced_year_array.iloc[0])*slope_r \
    #                                                                           for i in range (len(regression_reduced_xaxis_array))]
    regression_reduced_yaxis_array = [intercept_r + regression_reduced_xaxis_array.iloc[i]*slope_r \
                                                                                for i in range (len(regression_reduced_xaxis_array))]

    plt.plot(regression_reduced_xaxis_array, regression_reduced_yaxis_array, label='Linear Regression reduced data', color='g')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
