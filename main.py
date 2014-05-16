__author__ = 'Christopher Smith'

import asset as asset
import numpy as np
from asset import preparedates
from datetime import datetime
import pandas as pd



prodschedulemonthly = {12: 34450, 11: 23424, 10: 22424, 9: 24343, 8: 23423, 7: 11433, 6: 23432, 5: 23535, 4: 19191, 3: 23432,
    2: 23423, 1: 23423}

prodschedulequarterly = asset.monthlytoquarterly(prodschedulemonthly,firstquarterendingmonth=3)




# instantiate the asset
test = asset.WindPowerPlant(name='test', periods='Q', type='OffshoreWind')


# first we must must properly setup the dates that we will.  This is a critiacl first step as the date ranges will drive
# the balance of the programming and modeling required

#then setup the frame for construction
dates = preparedates(startdate=datetime(2015, 1, 27), enddate=datetime(2017, 1, 27), freq='M')
test.setup_frame(dates, dfname='construction')

#first setup the frame for operations
dates = preparedates(startdate=datetime(2017, 1, 27), enddate=datetime(2035, 1, 27), freq='Q')
test.setup_frame(dates, dfname='ops')

test.setup_production_schedule(prodschedulequarterly, dfname='ops', dfcolumn='production')
