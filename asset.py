__author__ = 'chris'import pandas as pdfrom datetime import datetimeimport numpy as npdef preparedates(startdate, enddate, freq='M'):    """    prepareDates produces a series of dates with an irregular commencement date and an irregular end date.    """    dates = []    dates.append(pd.index.Timestamp(startdate))    currentdate = startdate    if freq == 'M':        roll = True        while roll:            nextdate = pd.tseries.offsets.MonthEnd() + currentdate            dates.append(nextdate)            currentdate = nextdate + pd.tseries.offsets.DateOffset(days=1)            if currentdate > enddate:                roll = False    return datesclass PowerPlant():    """    This is an operating asset that has numerous proporties that define it, including whether it is operating or under    construction, what kind of asset it is, etc.    The program logic is to create facilities that have different properties.  Each property will have its own costs,    dates and application rules referred to as an 'application methods'.  The anticipated macro properties are:        construction schedules        production schedules        revenue schedules        expense schedules        maintenance schedules    These combined will produce a series of operatng cash flows.    An 'application method' can be either fixed, calendar, or volumetrically applied.  Application methods can    include cut in dates, cut out dates, or blackout dates.    Then, a "facility" will be rolled up into a portfolio to be combined together into a series of    cash flows that will be evaluated under a set of financing rules.    """    def __init__(self, name, type=None, description=None, location=None, latitude=None, longitude=None, dates=None):        """        Initializes a power plant asset for valuation purposes.        """        self.info = {}        self.info['name'] = name        self.info['type'] = type        self.info['description'] = description        self.info['location'] = location        self.info['latitude'] = latitude        self.info['longitude'] = longitude    def setupframe(self, dates, dfname):        setattr(self, dfname, pd.DataFrame(index=dates))        x = getattr(self, dfname)        x['timespan'] = x.index        x['timespan'] = x['timespan'] - x['timespan'].shift(1)def periodadjust(self, column):        """        Make an adjustment to a column quantities based upon the span of time in the period from the previous period        """        passclass WindPowerPlant(PowerPlant):    def __init__(self, name):        PowerPlant.__init__(self, name, type='Offshore Wind')    def setupproductionschedule(self, prodschedule, dfname='ops', dfcolumn='production'):        #first get the object DataFrame we want to work on        x = getattr(self, dfname)        # then get the column we want to utilize. If it errors then the column probably hasn't been created yet.        try:            getattr(x,dfcolumn)        # failed, so create the column        except:            x[dfcolumn] = None        # proceed down the index        for row in x.index:            #get the column we want to actually work on            y = getattr(x,dfcolumn)            z = getattr(x,'timespan')            #now we calculate the percentage of the month we are actually operating            #will need to come back and fix this so it is "smart" based upon the convetion.            #for now we will leave this at a month            monthforward = pd.tseries.offsets.MonthEnd()            monthback = pd.tseries.offsets.MonthBegin()            #total days in the timespan            maximum  = (monthforward.rollforward(row) - monthback.rollback(row)).days + 1            # percentage of period            try:                percentage = ((z[row] / np.timedelta64(1,'D') ) / maximum)            except:                percentage = 0            #actual time span            y[row] = prodschedule[row.month] * percentageclass BiomassPowerPlant(PowerPlant):    passclass NuclearPowerPlant(PowerPlant):    passclass CoalPowerPlant(PowerPlant):    pass