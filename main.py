__author__ = 'Christopher Smith'

import asset as asset
import numpy as np
from asset import preparedates
from datetime import datetime
import pandas as pd


#constants are declared here. To be moved into a user configuration file or front end later.

prodschedule = {12: 34450, 11: 23424, 10: 22424, 9: 24343, 8: 23423, 7: 11433, 6: 23432, 5: 23535, 4: 19191, 3: 23432,
    2: 23423, 1: 23423}





# instantiate the asset
test = asset.WindPowerPlant(name='test')


# first we must must properly setup the dates that we will.  This is a critiacl first step as the date ranges will drive
# the balance of the programming and modeling required

#first setup the frame for operations
dates = preparedates(datetime(2015, 1, 15), datetime(2017, 1, 27), 'M')
test.setupframe(dates, dfname='ops')

#then setup the frame for construction
dates = preparedates(datetime(2015, 1, 27), datetime(2035, 1, 26), 'M')
test.setupframe(dates, dfname='construction')

print(x)
test.setupproductionschedule(prodschedule, dfname='ops', dfcolumn='production')