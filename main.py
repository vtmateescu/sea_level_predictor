 #This entrypoint file to be used in development. Start by reading README.md
from turtle import color
import sea_level_predictor
from unittest import main
 
# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy import stats

#os.environ['MPLCONFIGDIR'] = '/opt/myapplication/.config/matplotlib'


#* Use matplotlib to create a scatter plot using the "Year" column as the x-axis and the "CSIRO Adjusted Sea Level" column as the y-axix.
#* Use the `linregress` function from `scipy.stats` to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
#* Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
#* The x label should be "Year", the y label should be "Sea Level (inches)", and the title should be "Rise in Sea Level".

# Test your function by calling it here
sea_level_predictor.draw_plot()

# Run unit tests automatically
main(module='test_module', exit=False)